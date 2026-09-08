# `pidog/action_flow.py` — Detailed Documentation

This document explains `pidog/action_flow.py` line by line and concept by concept:
what each construct is, how the pieces interact with the rest of the `pidog`
package, the exact runtime semantics of the background thread, and the sharp
edges / latent bugs in the current implementation.

---

## 1. Purpose and place in the codebase

`action_flow.py` defines **`ActionFlow`**, a *behaviour scheduler* that sits one
level above the low-level robot driver `Pidog` (`pidog/pidog.py`) and the
library of hand-written motion routines in `pidog/preset_actions.py`.

Layering:

```
examples/voice_active_dog.py        <- application: LLM decides "sit", "wag tail", ...
        |
        v
pidog/action_flow.py  (ActionFlow)  <- names -> motion recipes, posture management,
        |                              queueing, idle/standby behaviour, worker thread
        v
pidog/preset_actions.py             <- composite routines (bark, stretch, howling, ...)
        |
        v
pidog/pidog.py (Pidog)              <- servo buffers + servo threads (legs/head/tail)
        |
        v
pidog/actions_dictionary.py         <- raw joint-angle tables ('stand', 'forward', ...)
```

`ActionFlow` gives the application a *string-based* API (`add_action('sit',
'wag tail')`) so an LLM (or any other high-level component) can trigger robot
behaviour by simply emitting action names, without knowing anything about
servo angles, posture pre-conditions or blocking semantics.

Only consumer in this repository: `examples/voice_active_dog.py`.

---

## 2. Imports (lines 1–5)

```python
from .preset_actions import *
import threading
import time
from enum import Enum, StrEnum
import queue
```

| Import | Why it is there |
| --- | --- |
| `from .preset_actions import *` | Pulls every public name of `preset_actions` into this module's namespace: `scratch`, `hand_shake`, `high_five`, `pant`, `body_twisting`, `bark_action`, `shake_head`, `bark`, `push_up`, `howling`, `attack_posture`, `lick_hand`, `waiting`, `feet_shake`, `sit_2_stand`, `relax_neck`, `nod`, `think`, `recall`, `fluster`, `surprise`, `stretch`, … These are referenced unqualified inside the `OPERATIONS` lambdas. |
| `threading` | The worker thread that drains the action queue. |
| `time` | `time.time()` timestamps for the idle timer, `time.sleep()` for the polling loops. |
| `enum.Enum`, `enum.StrEnum` | The `Posetures` and `ActionStatus` enumerations. |
| `queue` | `queue.Queue` — thread-safe FIFO carrying pending action names. |

**Side effect worth knowing:** `preset_actions.py` has no `__all__`, and it does
`import random` at module level. The star-import therefore also binds `random`
(and `sleep`, `sin`, `cos`, `pi`) inside `action_flow`. `ActionFlow.action_handler`
relies on this: it calls `random.choices(...)` / `random.randint(...)` even though
`action_flow.py` never imports `random` itself. Removing the star-import (or
adding `__all__` to `preset_actions`) would break this module with a
`NameError` unless `import random` is added.

**Python version requirement:** `enum.StrEnum` was added in **Python 3.11**.
`pyproject.toml` declares `requires-python = ">=3.7"`, so importing this module
on 3.10 or older fails with `ImportError: cannot import name 'StrEnum'`.
This is a genuine metadata/implementation mismatch.

---

## 3. `Posetures` (lines 7–10)

```python
class Posetures(Enum):
    STAND = 0
    SIT = 1
    LIE = 2
```

The three gross body postures of the robot. (The name is a misspelling of
"Postures"; it is part of the public API — `examples/voice_active_dog.py` does
`from pidog.action_flow import ActionFlow, ActionStatus, Posetures` — so it
cannot be renamed without a breaking change.)

Each posture implies a different neutral head pitch, which is why posture
changes and `head_pitch_init` are managed together (see `change_poseture`).

---

## 4. `ActionStatus` (lines 12–16)

```python
class ActionStatus(StrEnum):
    STANDBY = 'standby'
    THINK = 'think'
    ACTIONS = 'actions'
    ACTIONS_DONE = 'actions_done'
```

The state of the background worker thread. `StrEnum` means the members *are*
`str` instances, so `ActionStatus.STANDBY == 'standby'` is `True`. That is
essential here because `__init__` initialises the state with the raw string
`'standby'` rather than the enum member; with a plain `Enum` the comparison in
`action_handler` would silently never match and the robot would never perform
its idle behaviour.

| Member | Meaning | Set by |
| --- | --- | --- |
| `STANDBY` | Nothing queued; the worker plays random idle "alive" motions. | `start()`, `action_handler` when the queue drains |
| `THINK` | Suspend all motion (used by the app while the LLM is generating a reply, so servo noise doesn't pollute the microphone / the dog holds a "thinking" pose). | Application, via `set_status()` |
| `ACTIONS` | There is at least one queued action; the worker drains the queue. | `add_action()` |
| `ACTIONS_DONE` | Declared but **never used** anywhere in the codebase. Dead member. | — |

---

## 5. `ActionFlow` class attributes (lines 18–29)

```python
class ActionFlow():
    SIT_HEAD_PITCH = -35
    STAND_HEAD_PITCH = 0
    HEAD_SPEED = 80
    HEAD_ANGLE = 20
    CHANGE_STATUS_SPEED = 60

    dog_obj = None
    head_yrp = [0, 0, 0]
    head_pitch_init = 0
    posture = Posetures.STAND
    last_actions = None
```

Tuning constants:

* `SIT_HEAD_PITCH = -35` — when sitting, the body leans back, so the head servo
  needs −35° of pitch compensation to keep the head looking level.
* `STAND_HEAD_PITCH = 0` — standing/lying needs no compensation.
* `HEAD_SPEED = 80` — speed used for the compensation head move.
* `HEAD_ANGLE = 20` — **unused** in this file (leftover).
* `CHANGE_STATUS_SPEED = 60` — speed for posture transitions.

Class-level *state* (`dog_obj`, `head_yrp`, `head_pitch_init`, `posture`,
`last_actions`) exists mostly so the `OPERATIONS` lambdas can be written against
attribute names that are guaranteed to resolve. `__init__` shadows all of them
with per-instance attributes **except `last_actions`**, which therefore stays a
*class* attribute until first written. Since `run()` assigns
`self.last_actions = action`, the first write creates an instance attribute and
the class attribute is untouched — so in practice there is no cross-instance
leak, but the mutable class-level `head_yrp` list would be shared if `__init__`
did not rebind it. Prefer instance state; the class-level copies are a smell.

* `head_yrp` — the current head target as `[yaw, roll, pitch]` in degrees. It is
  passed to the preset routines that need a base orientation to animate around.
  Nothing in this file ever changes it from `[0, 0, 0]`; it is effectively a hook
  for a head-tracking feature (e.g. sound-direction following) that would write
  into it.
* `head_pitch_init` — the current pitch compensation for the active posture. It
  is passed as `pitch_comp=` to the preset routines so head animations remain
  correct whether the dog is sitting or standing.
* `posture` — the posture the scheduler believes the robot is in.
* `last_actions` — the name of the last action that triggered a posture change;
  used as a de-duplication guard (see §8).

---

## 6. The `OPERATIONS` table (lines 31–156)

The heart of the module: a **declarative mapping from action name → recipe**.

```python
OPERATIONS = {
    "<action name>": {
        "poseture":  Posetures.X,        # optional: required body posture
        "before":    <name or callable>, # optional: run first
        "function":  <callable>,         # the action itself
        "after":     <name or callable>, # optional: run last
        "head_pitch": <int>,             # present once, never read
    },
    ...
}
```

### 6.1 Key semantics (as implemented by `run()`)

| Key | Type | Semantics |
| --- | --- | --- |
| `poseture` | `Posetures` | Pre-condition. Before the action runs, the body is transitioned into this posture (subject to the `last_actions` guard). |
| `before` | either an action name (`str`) present in `OPERATIONS`, or a `callable(self)` | Executed, then blocks until all servos are idle. |
| `function` | `callable(self)` | The action body. Executed, then blocks until all servos are idle. |
| `after` | either an action name (`str`) or `callable(self)` | Executed after `function`, then blocks. Typically used to return to a resting posture, or to repeat the action once more. |
| `head_pitch` | `int` | Present only on `"nod"`. **Never read by any code** — dead configuration. |

All callables take exactly one argument, the `ActionFlow` instance, and are
written as `lambda self: ...`. Because they live inside the class body's dict,
they are *plain functions* stored in a dict, not bound methods, so `run()` must
pass `self` explicitly: `operation["function"](self)`.

Two dispatch styles appear in the table:

1. **Driver-level actions** — `lambda self: self.dog_obj.do_action('forward', speed=98)`.
   `Pidog.do_action(name, step_count=1, speed=50, pitch_comp=0)` looks the name up
   in `actions_dictionary.py`, gets `(angle_frames, part)` where `part` is
   `'legs' | 'head' | 'tail'`, and appends the frames to the corresponding buffer
   with `immediately=False` (i.e. *queued*, not interrupting).
2. **Composite routines** — `lambda self: stretch(self.dog_obj)` etc., calling
   the hand-authored multi-step animations in `preset_actions.py`. These often
   also play a sound via `Pidog.speak(...)`.

### 6.2 Complete catalogue

Locomotion (all require `STAND`, all at `speed=98` — near-maximum, gait needs it):

| Name | Effect |
| --- | --- |
| `forward` | `do_action('forward', speed=98)` — one gait cycle forward |
| `backward` | `do_action('backward', speed=98)` |
| `turn left` | `do_action('turn_left', speed=98)` |
| `turn right` | `do_action('turn_right', speed=98)` |

Posture:

| Name | Effect | Posture |
| --- | --- | --- |
| `stop` | **empty dict** — no posture, no function. `run()` matches the key, finds no `function`/`before`/`after`/`poseture` and does nothing at all. It is a *documented no-op*: it exists so the LLM can emit `"stop"` without producing an `unknown action` path. Note it does **not** call `Pidog.body_stop()`; queued motion continues. | — |
| `lie` | `do_action('lie', speed=70)` | `LIE` |
| `stand` | `do_action('stand', speed=65)` | `STAND` |
| `sit` | `do_action('sit', speed=70)` | `SIT` |

Note the double motion: for `sit`, `run()` first calls `change_poseture(SIT)`
(which itself performs `do_action('sit', speed=CHANGE_STATUS_SPEED)`) and then
the operation's own `do_action('sit', speed=70)`. The second one is effectively
a no-op re-issue at a different speed.

Vocal / expressive:

| Name | Recipe | Notes |
| --- | --- | --- |
| `bark` | `bark(dog, head_yrp, pitch_comp=head_pitch_init)` | Head up (+25° pitch) → `speak('single_bark_1')` → head down |
| `bark harder` | `before=attack_posture`, then `bark_action(dog, head_yrp, 'single_bark_1')`; posture `STAND` | The only entry using a **callable** `before` |
| `pant` | `pant(dog, head_yrp, pitch_comp=head_pitch_init)` | Panting sound + head bob |
| `howling` | `howling(dog)`, `after='sit'`, posture `SIT` | |
| `shake head` | `shake_head(dog, [yaw, roll, pitch + head_pitch_init])` | Compensation is folded into the third element manually rather than via a `pitch_comp` argument, because `shake_head()` has no `pitch_comp` parameter |

Body / tricks:

| Name | Recipe | Posture | `after` |
| --- | --- | --- | --- |
| `wag tail` | `do_action('wag_tail', speed=100)` | — | `'wag tail'` (self-reference ⇒ runs twice) |
| `stretch` | `stretch(dog)` | `SIT` | `'sit'` |
| `doze off` | `do_action('doze_off', speed=95)` | `LIE` | `'doze off'` (self-reference ⇒ twice) |
| `push up` | `push_up(dog)` | `STAND` | — |
| `twist body` | `body_twisting(dog)` | `STAND` | `'sit'` (note: posture is STAND but it ends sitting) |
| `scratch` | `scratch(dog)` | `SIT` | `'sit'` |
| `handshake` | `hand_shake(dog)` | `SIT` | `'sit'` |
| `high five` | `high_five(dog)` | `SIT` | `'sit'` |
| `lick hand` | `lick_hand(dog)` | `SIT` | — |
| `feet shake` | `feet_shake(dog)` | `SIT` | — |
| `waiting` | `waiting(dog, pitch_comp=head_pitch_init)` | — | Small random head drift; the primary idle animation |

Emotional head animations (all `SIT`, all take `pitch_comp=head_pitch_init`):
`relax neck`, `nod`, `think`, `recall`, `fluster`, `surprise`.

Self-referencing `after` (`wag tail`, `doze off`) is the idiom used to make a
short animation last roughly twice as long, since `run()` resolves the string
against `OPERATIONS` and calls that entry's `function` — it does **not** recurse
through `run()`, so no infinite loop occurs and the `after`'s own `after` is
ignored.

---

## 7. `__init__` (lines 158–169)

```python
def __init__(self, dog_obj):
    self.dog_obj = dog_obj
    self.head_yrp = [0, 0, 0]
    self.head_pitch_init = 0
    self.posture = Posetures.LIE
    self.thread = None
    self.thread_running = False
    self.thread_action_state = 'standby'
    self.action_queue = queue.Queue()
```

* `dog_obj` — an initialised `Pidog` instance. `ActionFlow` never constructs or
  owns the hardware; the application does and injects it.
* Initial posture is assumed to be **`LIE`**, which is the physical rest position
  a Pidog is left in when powered off (legs folded). This differs from the class
  attribute default (`STAND`) — the instance value wins.
* `thread_action_state` is initialised to the raw string `'standby'`; equal to
  `ActionStatus.STANDBY` thanks to `StrEnum`.
* The queue is created here *and again* in `start()` (so a restart begins with an
  empty queue).

No thread is started by the constructor; `start()` must be called explicitly.

---

## 8. Head / posture management

### `set_head_pitch_init(self, pitch)` (lines 171–174)

```python
self.head_pitch_init = pitch
self.dog_obj.head_move([self.head_yrp], pitch_comp=pitch,
                       immediately=True, speed=self.HEAD_SPEED)
```

Records the new pitch compensation and immediately re-issues the current head
target with it. `Pidog.head_move` takes a **list of** `[yaw, roll, pitch]`
frames, hence `[self.head_yrp]` (a one-frame list). `immediately=True` calls
`head_stop()` first, clearing any queued head frames, so the head snaps to the
new compensated orientation instead of finishing an old animation.

`Pidog.head_rpy_to_angle` then converts yaw/roll/pitch into the three servo
angles, blending roll and pitch by the yaw ratio (the head gimbal is not
orthogonal), and adds `pitch_comp` to the pitch servo.

### `change_poseture(self, poseture)` (lines 176–191)

```python
if poseture == Posetures.STAND:
    self.set_head_pitch_init(self.STAND_HEAD_PITCH)
    if self.posture != Posetures.STAND:
        sit_2_stand(self.dog_obj, speed=75)   # speed > 70
    else:
        self.dog_obj.do_action('stand', speed=self.CHANGE_STATUS_SPEED)
elif poseture == Posetures.SIT:
    self.set_head_pitch_init(self.SIT_HEAD_PITCH)
    self.dog_obj.do_action('sit', speed=self.CHANGE_STATUS_SPEED)
elif poseture == Posetures.LIE:
    self.set_head_pitch_init(self.STAND_HEAD_PITCH)
    self.dog_obj.do_action('lie', speed=self.CHANGE_STATUS_SPEED)

self.posture = poseture
self.dog_obj.wait_all_done()
```

Key points:

1. **Head compensation is applied first**, before the body moves, so the head is
   already aimed correctly as the body transitions.
2. **Standing up is special.** Going from sit/lie to stand cannot be done with a
   single target pose — the legs would slip. `sit_2_stand()` in
   `preset_actions.py` moves the legs through an intermediate brace pose `L1`
   before the `stand` angles. The inline
   comment `# speed > 70` records a hardware constraint: below ~70 the servos
   move too slowly to overcome the robot's weight and it fails to rise. If the
   dog is *already* standing, the cheaper `do_action('stand')` re-levels it.
3. `LIE` uses `STAND_HEAD_PITCH` (0), not a dedicated lie value.
4. The posture field is updated **unconditionally**, even if the underlying
   `do_action` failed (e.g. unknown action name — `Pidog.do_action` swallows
   `KeyError` and only prints).
5. `wait_all_done()` blocks the *calling* thread (normally the worker thread)
   until the legs, head and tail buffers in `Pidog` are all empty — i.e. until
   the servo threads have consumed every queued frame. This is what makes
   `ActionFlow` sequential despite `Pidog` being asynchronous.

---

## 9. `run(self, action)` — the recipe interpreter (lines 194–228)

```python
def run(self, action):
    try:
        if action in self.OPERATIONS:
            operation = self.OPERATIONS[action]
            # poseture
            if "poseture" in operation and operation["poseture"] != None:
                if self.last_actions != action:
                    self.last_actions = action
                    self.change_poseture(operation["poseture"])
            # before
            if "before" in operation and operation["before"] != None:
                before = operation["before"]
                if before in self.OPERATIONS and self.OPERATIONS[before]["function"] != None:
                    self.OPERATIONS[before]["function"](self)
                    self.dog_obj.wait_all_done()
                else:
                    before(self)
                    self.dog_obj.wait_all_done()
            # function
            if "function" in operation and operation["function"] != None:
                operation["function"](self)
                self.dog_obj.wait_all_done()
            # after
            if "after" in operation and operation["after"] != None:
                after = operation["after"]
                if after in self.OPERATIONS and self.OPERATIONS[after]["function"] != None:
                    self.OPERATIONS[after]["function"](self)
                    self.dog_obj.wait_all_done()
                else:
                    after(self)
                    self.dog_obj.wait_all_done()
    except Exception as e:
        print(f'action error: {e}')
```

### Execution order

```
posture pre-condition  ->  before  ->  function  ->  after
        (each stage followed by wait_all_done(), i.e. fully blocking)
```

### Behaviour details

* **Unknown action names are silently ignored.** `if action in self.OPERATIONS`
  with no `else`. This matters because the LLM in `voice_active_dog.py` is free
  to hallucinate action names, and because the standby list contains
  `'feet_left_right'`, which is *not* a key in `OPERATIONS` (see §10).
* **The posture guard is `last_actions`, not `posture`.** The commented-out line
  `# if self.posture != operation["poseture"]:` shows the original intent: skip
  the transition if already in the right posture. The shipped code instead skips
  it when *the same action is repeated back-to-back*. Consequences:
  * Repeating `sit` twice in a row does not re-issue the sit transition — good.
  * Alternating `handshake`, `high five` (both `SIT`) re-runs the full sit
    transition every time — wasteful, and visibly jerky.
  * `last_actions` is only updated inside this branch, so actions without a
    `poseture` key (e.g. `bark`, `pant`, `wag tail`) never update it. After
    `sit` → `bark` → `sit`, the second `sit` is still considered a repeat and
    the posture transition is skipped, even though `bark` may have disturbed the
    pose. This is a latent bug, though usually harmless.
* **String-vs-callable dispatch for `before`/`after`** is done with
  `if before in self.OPERATIONS`. Two hazards:
  * `X in dict` on a *callable* is a hash lookup of a function object — safe,
    returns `False`, falls through to `before(self)`. Fine.
  * `self.OPERATIONS[before]["function"]` raises **`KeyError: 'function'`** if the
    referenced entry has no `function` key. Today the only such entry is
    `"stop"`, and nothing references it as `before`/`after`, so the bug is
    unreachable — but adding `"after": "stop"` anywhere would trip it. The
    `KeyError` would be caught by the outer `except` and printed as
    `action error: 'function'`.
* **Blanket `except Exception`.** Any hardware error, I2C failure, missing sound
  file or programming mistake inside an action becomes a printed line and the
  scheduler carries on. Good for robot uptime, bad for debuggability — failures
  are invisible to callers, and `run()` never signals success/failure.
* **`run()` is synchronous and blocking.** It returns only when every servo
  buffer is drained. It is normally called from the worker thread, but nothing
  prevents an application from calling it directly from the main thread — doing
  so concurrently with a running worker would interleave two action recipes on
  the same servo buffers, with no locking.

---

## 10. `action_handler(self)` — the worker loop (lines 230–259)

```python
def action_handler(self):
    standby_actions = ['waiting', 'feet_left_right']
    standby_weights = [1, 0.3]

    action_interval = 5  # seconds
    last_action_time = time.time()

    while self.thread_running:
        if self.thread_action_state == ActionStatus.STANDBY:
            if time.time() - last_action_time > action_interval:
                choice = random.choices(standby_actions, standby_weights)[0]
                self.run(choice)
                last_action_time = time.time()
                action_interval = random.randint(2, 6)
        elif self.thread_action_state == ActionStatus.THINK:
            pass
        elif self.thread_action_state == ActionStatus.ACTIONS:
            _action = self.action_queue.get()
            try:
                self.run(_action)
            except Exception as e:
                print(f'action error: {e}')

            if self.action_queue.empty():
                self.thread_action_state = ActionStatus.STANDBY
                last_action_time = time.time()

            time.sleep(0.5)

        time.sleep(0.01)
```

This is the body of the thread created in `start()`. It polls the state at
~100 Hz.

### `STANDBY` — idle "alive" behaviour

Every `action_interval` seconds (initially 5, then a random 2–6) it plays a
random idle motion, weighted 1 : 0.3 between `'waiting'` and
`'feet_left_right'`. `random.choices` accepts unnormalised weights, so the
effective probabilities are 1/1.3 ≈ 77 % and 0.3/1.3 ≈ 23 %.

**`'feet_left_right'` is not a key in `OPERATIONS`.** `run()` therefore does
nothing for it. The practical effect is that ~23 % of idle ticks are silent
no-ops — the dog just pauses. The intended action almost certainly was
`'feet shake'` (`feet_shake` in `preset_actions.py`). This is a real bug, and a
good example of why `run()` silently ignoring unknown names is dangerous.

Note also that idle actions are *not* affected by the `last_actions` guard,
because `'waiting'` has no `poseture` key.

### `THINK` — suspended

Explicit `pass`. The loop keeps spinning at 100 Hz but issues no motion and,
importantly, **does not drain the queue**. The idle timer is not reset either,
so on the first transition back to `STANDBY` an idle action fires almost
immediately (`time.time() - last_action_time` is already large).

### `ACTIONS` — draining the queue

`self.action_queue.get()` is a **blocking** call with no timeout. If the state is
`ACTIONS` but the queue is empty, the worker thread parks inside `get()`
indefinitely; `self.thread_running = False` will not wake it, so `stop()` would
hang on `thread.join()`. In practice the state is only set to `ACTIONS` by
`add_action()`, which always enqueues at least one item first, and the state is
flipped back to `STANDBY` as soon as the queue drains — so the window is small
but real: if `add_action()` is called concurrently and the state is re-set to
`ACTIONS` just after the worker's emptiness check, or if `set_status(ACTIONS)`
is called by hand, the thread can block forever.

After each action there is a deliberate `time.sleep(0.5)` — a short pause
between chained actions so the sequence reads as distinct gestures rather than
one continuous blur.

The trailing `time.sleep(0.01)` is the poll interval for all states.

---

## 11. Public control API (lines 261–283)

### `add_action(self, *actions)`

```python
for action in actions:
    self.action_queue.put(action)
self.thread_action_state = ActionStatus.ACTIONS
```

Enqueues one or more action names and switches the worker into `ACTIONS`.
Enqueue-then-set-state is the correct order (the reverse would expose the
blocking-`get()` window described above). Names are not validated.

Usage in `voice_active_dog.py`: `self.action_flow.add_action(*actions)` where
`actions` is the list the LLM returned in its JSON response.

### `set_status(self, status)`

Direct assignment of the worker state. Used by the application to enter `THINK`
while the LLM is generating and `STANDBY` afterwards. No validation, no locking
(fine in CPython for a single attribute assignment).

### `wait_actions_done(self)`

```python
while self.thread_action_state != ActionStatus.STANDBY:
    time.sleep(0.01)
```

Blocks the caller until the worker returns to `STANDBY` — i.e. until the queue
is empty and the last action finished. Note it waits for the **state**, not the
queue, so it also blocks forever if the state is `THINK`. Callers must therefore
leave `THINK` before waiting. 100 Hz busy-poll rather than an `Event`/`join`.

### `start(self)`

```python
self.thread_running = True
self.thread_action_state = ActionStatus.STANDBY
self.action_queue = queue.Queue()
self.thread = threading.Thread(name="action_handler", target=self.action_handler)
self.thread.start()
```

Resets state, discards any previously queued actions, and launches the worker.
The thread is **non-daemon**, so an application that forgets `stop()` will not
exit until the thread ends. Calling `start()` twice leaks the first thread (the
old thread keeps running because `thread_running` was set back to `True`).

### `stop(self)`

```python
self.thread_running = False
if self.thread != None:
    self.thread.join()
```

Requests shutdown and waits. Shutdown latency is bounded by the *current
action*: `run()` blocks until all servo frames are consumed, so `stop()` can take
seconds. If the worker is parked in `action_queue.get()`, `join()` never returns
(see §10).

---

## 12. End-to-end example (from `examples/voice_active_dog.py`)

```python
from pidog.pidog import Pidog
from pidog.action_flow import ActionFlow, ActionStatus, Posetures

dog = Pidog()
action_flow = ActionFlow(dog)

action_flow.set_status(ActionStatus.STANDBY)
action_flow.start()                       # worker begins idle "waiting" motions
action_flow.change_poseture(Posetures.SIT)

# user speaks -> app suspends motion while the LLM thinks
action_flow.set_status(ActionStatus.THINK)

# LLM returns {"actions": ["wag tail", "bark"], "answer": "..."}
action_flow.add_action("wag tail", "bark")   # state -> ACTIONS
action_flow.wait_actions_done()              # blocks until back in STANDBY

action_flow.change_poseture(Posetures.SIT)
action_flow.stop()
```

What happens for `add_action("wag tail", "bark")`:

1. `"wag tail"`, `"bark"` are pushed onto the FIFO; state becomes `ACTIONS`.
2. Worker pops `"wag tail"`. No `poseture` key ⇒ no posture change.
   No `before`. `function` ⇒ `do_action('wag_tail', speed=100)`, then
   `wait_all_done()`. `after` is `"wag tail"` ⇒ the same function runs a second
   time, then `wait_all_done()`.
3. Queue not empty ⇒ stay in `ACTIONS`; sleep 0.5 s.
4. Worker pops `"bark"`. No posture, no before. `function` ⇒
   `bark(dog, [0,0,0], pitch_comp=head_pitch_init)` — head lunge plus the
   the `single_bark_1` sound. `wait_all_done()`. No `after`.
5. Queue now empty ⇒ state back to `STANDBY`, idle timer reset, sleep 0.5 s.
6. `wait_actions_done()` in the app returns.

---

## 13. Concurrency model summary

| Thread | Runs | Touches |
| --- | --- | --- |
| Application / main | `add_action`, `set_status`, `wait_actions_done`, `change_poseture`, `start`, `stop` | `thread_action_state`, `action_queue`, and (via `change_poseture`) the servo buffers |
| `action_handler` worker | `run()` and everything below it | servo buffers, `posture`, `head_pitch_init`, `last_actions`, `thread_action_state` |
| `Pidog` servo threads (legs/head/tail) | consume the frame buffers | hardware |

Synchronisation primitives actually used: only `queue.Queue` (for the action
names) and the locks *inside* `Pidog` (for the buffers). `thread_action_state`,
`posture`, `head_pitch_init` and `head_yrp` are unguarded shared state; the
design relies on the GIL making single attribute reads/writes atomic and on the
application not issuing motion commands while the worker is active. Notably
`change_poseture()` called from the main thread **can** race with an action
running on the worker thread.

---

## 14. Known issues / improvement candidates

1. `'feet_left_right'` in `standby_actions` is not a defined operation — dead
   idle branch (~23 % of idle ticks do nothing). Likely meant `'feet shake'`.
2. `StrEnum` requires Python ≥ 3.11 while `pyproject.toml` says `>= 3.7`.
3. `run()` silently ignores unknown action names — no logging, so issue #1 is
   invisible at runtime.
4. Posture guard keys off `last_actions` (last action name) instead of the
   current `posture`, causing both redundant transitions and skipped ones.
5. `self.OPERATIONS[before]["function"]` assumes a `"function"` key exists —
   `KeyError` for entries like `"stop"`.
6. `action_queue.get()` has no timeout ⇒ possible permanent block, which turns
   `stop()`/`join()` into a hang.
7. `wait_actions_done()` and the worker loop busy-poll; `queue.join()` /
   `threading.Event` would be cheaper and race-free.
8. Dead code: `HEAD_ANGLE`, `ActionStatus.ACTIONS_DONE`, the `head_pitch` key on
   `"nod"`, the class-level state duplicates.
9. `"stop"` does not stop anything — it does not call `Pidog.body_stop()`.
10. `run()` depends on `random` being leaked in by
    `from .preset_actions import *`; an explicit `import random` would be safer.
11. Spelling: `Posetures` / `poseture` (public API, so renaming is breaking).
