# `pidog/preset_actions.py` — Detailed Documentation

This document explains `pidog/preset_actions.py` in depth: the conventions every
routine follows, what each of the 24 functions does frame by frame, the shared
angle vocabulary, and the sharp edges / latent bugs in the current
implementation.

Companion documents: [`pidog.md`](./pidog.md) (the hardware driver these
routines call) and [`action_flow.md`](./action_flow.md) (the scheduler that
invokes them by name).

---

## 1. Purpose and place in the codebase

`preset_actions.py` is the **choreography library**: a flat collection of
module-level functions, each of which plays one hand-authored, multi-step
animation on a `Pidog` instance.

```
examples/*.py                       <- import individual routines directly
        |
pidog/action_flow.py (ActionFlow)   <- maps names like "high five" -> these functions
        |
        v
pidog/preset_actions.py   <<< THIS FILE >>>
        |
        v
pidog/pidog.py (Pidog)              <- legs_move / head_move / do_action / speak
        |
        v
pidog/actions_dictionary.py         <- named single poses ('sit', 'stand', 'push_up', …)
```

The division of labour is worth stating precisely:

| Layer | Owns |
| --- | --- |
| `actions_dictionary.py` | **Static poses and generated gaits** — a name maps to a list of joint-angle frames plus the body part. No sequencing, no sound, no timing. |
| `preset_actions.py` | **Sequences** — several poses in order, mixing legs + head + tail, interleaved with sounds, `sleep()`s, randomness and repetition. |
| `action_flow.py` | **Behaviour selection** — which sequence to play, posture preconditions, queueing. |

Everything here is a plain function taking the `Pidog` object as its first
argument (conventionally named `my_dog`). There is no class, no state (with one
vestigial exception, §4.4), and no return values — these are pure side-effect
routines.

---

## 2. Imports and module surface (lines 1–4)

```python
from time import sleep
import random
from math import sin, cos, pi
```

* `sleep` — inter-phase pauses that cannot be expressed as servo motion (letting
  a sound finish, holding a pose).
* `random` — used by `waiting()` and `feet_shake()` to make idle behaviour
  non-repetitive.
* `sin`, `cos`, `pi` — used by the four *procedural* animations
  (`shake_head_smooth`, `relax_neck`, `nod`) that generate smooth frame
  sequences instead of listing poses by hand.

There is **no `__all__`**, which matters: `action_flow.py` does
`from .preset_actions import *`, so it also inherits `sleep`, `random`, `sin`,
`cos` and `pi` into its namespace — and it *depends* on that, because
`ActionFlow.action_handler` calls `random.choices()` / `random.randint()`
without importing `random` itself. Adding an `__all__` here would break
`action_flow.py` unless that module gains its own `import random`.

---

## 3. Shared conventions

Understanding these five conventions makes every function in the file readable.

### 3.1 Leg angle frames — 8 values

Every leg frame is an 8-element list in **leg-pin order**, matching
`Pidog.DEFAULT_LEGS_PINS = [2, 3, 7, 8, 0, 1, 10, 11]`:

```
index:  0        1        2        3        4        5        6        7
       LF hip  LF knee  RF hip  RF knee  LH hip  LH knee  RH hip  RH knee
       \___ left front ___/  \__ right front __/  \__ left hind __/  \__ right hind __/
```

Left and right are **mirrored**, so a symmetric pose has `[a, b, -a, -b, c, d, -c, -d]`.
The canonical sit pose from `actions_dictionary.py` is exactly that:

```python
sit = [30, 60, -30, -60, 80, -45, -80, 45]
```

Almost every frame in this file is a small perturbation of `sit`, which is why
the constant `80, -45, -80, 45` tail-half appears over and over: **the hind legs
stay in the sit pose while the front legs perform the trick**.

Note 1 in the source (`# Note 1`, lines 11–16, 28) documents one such tweak:

> Last servo (4th legs) original value is 45, change to 40 to push down a little
> bit to support the raising legs, prevent the dog from falling down.

i.e. index 7 is dropped from `45` → `38` in `scratch`, `hand_shake` and
`high_five` so the right hind leg braces against the tipping moment created by
lifting a front paw.

### 3.2 Head frames — 3 values

Head frames are `[yaw, roll, pitch]` in degrees, and there are **two different
APIs**, used deliberately:

| Call | Meaning |
| --- | --- |
| `my_dog.head_move(frames, pitch_comp=…)` | Goes through `Pidog.head_rpy_to_angle`, which blends roll/pitch as a function of yaw to compensate for the gimbal's cross-coupling. Use when the head is turned. |
| `my_dog.head_move_raw(frames)` | Bypasses that blend; the values go straight to the servos (still clamped and pitch-offset in the worker thread). Use for precomputed servo-space sequences. |

The procedural animations (`shake_head_smooth`, `relax_neck`, `nod`, `think`,
`recall`, `fluster`, `alert`, `surprise`) all use `head_move_raw` and fold
`pitch_comp` into the pitch value themselves (`p = … + pitch_comp`), because
they were tuned in servo space. The pose-based ones (`pant`, `bark`,
`bark_action`, `shake_head`) use `head_move` and pass `pitch_comp=` through.

`pitch_comp` is the posture compensation supplied by `ActionFlow`: `0` when
standing, `-35` when sitting (see `action_flow.md` §5).

### 3.3 `immediately=False` and the wait dance

Recall from [`pidog.md`](./pidog.md) that `legs_move`/`head_move` are
**non-blocking** — they append frames to per-group buffers that background
threads drain. Therefore:

```python
my_dog.legs_move(f_up, immediately=False, speed=80)   # queue, do not pre-empt
my_dog.wait_all_done()                                 # block until buffers empty
```

* `immediately=False` = *append* (chain onto whatever is queued).
  `immediately=True` = *pre-empt* (clear the buffer first). This file uses
  `False` almost everywhere; `bark_action` and `attack_posture` use `True`
  because a bark must interrupt whatever the dog was doing.
* Issuing legs **and** head before a single `wait_all_done()` is how the two are
  made to move *simultaneously*; issuing them with a wait in between makes them
  sequential. Read every routine with that in mind — the placement of the wait
  calls *is* the choreography.
* `wait_legs_done()` / `wait_head_done()` allow waiting on one group only, e.g.
  `lick_hand` waits on both explicitly rather than using `wait_all_done()`
  (equivalent, since the tail is idle).

### 3.4 Speed

`speed` is 0–100 and is **per group, not per frame** (see `pidog.md` §8):
the last value passed wins for everything currently in that buffer. Typical
values in this file: 50–68 for deliberate/slow motions, 80 for normal, 90–100
for snappy ones (scratching, high-fiving, barking, flustering).

### 3.5 Sound

`my_dog.speak(name, volume)` is **non-blocking** and resolves `name` against
`~/pidog/sounds/{name}.mp3|.wav`. Available clips in the repo's `sounds/`:
`angry.wav`, `confused_1..3.mp3`, `growl_1..2.mp3`, `howling.mp3`, `pant.mp3`,
`single_bark_1.mp3`, `single_bark_2.mp3`, `snoring.mp3`, `woohoo.mp3`.

Because playback is asynchronous, routines that need audio and motion to line up
either start the sound *first* and then move (`pant`, `bark`) or insert an
explicit `sleep()` sized to the clip (`howling`, §4.7).

---

## 4. The routines

24 functions, grouped by kind.

### 4.1 Front-paw tricks (sit-based)

These four share a skeleton: **raise a front paw → repeat a small oscillation →
withdraw → settle back into sit with the head lowered**. They all assume the dog
is (or will be put) sitting, and all keep the hind legs at the sit angles.

#### `scratch(my_dog)` (lines 7–28)

```python
h1 = [[0, 0, -40]]         # head level-ish, looking down
h2 = [[30, 70, -10]]       # head turned+rolled toward the scratching paw
f_up      = [[30, 60, 50, 50, 80, -45, -80, 38]]
f_scratch = [[30, 60, 40, 40, 80, -45, -80, 38],
             [30, 60, 50, 50, 80, -45, -80, 38]]
```

1. `do_action('sit', speed=80)` — establish the base pose.
2. Head to `h2` and front-right paw up (`f_up`) **together**, then wait. The
   large roll (`70`) tilts the head toward the raised paw — this is what sells
   the "scratching my ear" read.
3. **10 iterations** of the two-frame `f_scratch` oscillation at `speed=94`
   (knee 50↔40 = a 10° flutter). Waiting inside the loop means each pair
   completes before the next is queued.
4. Head back to `h1`, re-issue `sit`, wait.

Note index 7 is `38` throughout (Note 1 bracing) but the final `sit` restores it
to `45`.

#### `hand_shake(my_dog)` (lines 31–62)

```python
f_up        = [[30, 60, -20,  65, 80, -45, -80, 38]]   # paw offered
f_handshake = [[30, 60,  10, -25, 80, -45, -80, 38],
               [30, 60,  10, -35, 80, -45, -80, 38]]   # 10° pump
f_withdraw  = [[30, 60, -40,  30, 80, -45, -80, 38]]
```

Offer the paw, `sleep(0.1)` (a beat, so a human can grab it), pump **8 times**
at `speed=90`, withdraw, then a **4-frame** descent
(`-40 → -50 → -58 → -60` on the right-front knee) which lands the paw gently
instead of dropping it, issued together with `head_move([[0, 0, -35]])`.

That 4-frame `hand_down_angs` block is copy-pasted verbatim into `high_five` and
`lick_hand` — the obvious extraction candidate in this file.

#### `high_five(my_dog)` (lines 65–93)

Same skeleton with three poses instead of a loop: paw up (`f_up`), a fast
slap down (`f_down`, `speed=94`), `sleep(0.5)` to hold the contact, withdraw,
then the same 4-frame gentle descent. The `speed=94` on the down stroke versus
`80` elsewhere is the whole gag.

#### `lick_hand(my_dog)` (lines 234–271)

```python
leg1  = [[30, 45, 70, -32, 80, -55, -80, 45]]
head1 = [[-22, -23, -45],
         [-22, -23, -35]]          # 10° pitch bob = the "lick"
leg2  = [[30, 45, 70, -32, 80, -55, -80, 45],
         [30, 45, 66, -36, 80, -55, -80, 45]]
```

Sit, head down (`immediately=True` — pre-empt whatever the head was doing), then
raise the paw toward the muzzle (`leg1`) while the head bobs (`head1`), then
**3 repetitions** of paw-and-head bobbing together, then the shared 4-frame
descent. The negative yaw/roll on the head (`-22, -23`) tilts it toward the
raised paw, mirroring the trick in `scratch`.

Note this routine waits with `wait_head_done()` + `wait_legs_done()` rather than
`wait_all_done()`; functionally the same here.

### 4.2 Full-body motions

#### `body_twisting(my_dog)` (lines 109–124)

```python
f1 = [-80, 70, 80, -70, -20, 64, 20, -64]     # the stretch pose (== actions_dict['stretch'])
f2 = [-70, 50, 80, -90, 10, 20, 20, -64]      # twisted left
f3 = [-80, 90, 70, -50, -20, 64, -10, -20]    # twisted right
f  = [f2, f1, f3, f1]                          # left → centre → right → centre
```

A slow (`speed=50`) four-frame twist about the long axis from the sprawled
stretch pose, then `sleep(.3)` and a **two-stage** return to sit
(`_2_sit_angs`: an intermediate half-crouch, then the sit pose) at `speed=68`,
with the head raised to `-35` via `head_move_raw`. The intermediate frame
matters — going straight from the sprawl to sit makes the legs scrape.

#### `stretch(my_dog)` (lines 529–552)

The classic dog stretch ("play bow"): five leg frames alternating the front-hip
angle `-80 → -80 → -65 → -80 → -65` at `speed=55`, i.e. a couple of slow
pushes deeper into the stretch, with the head lifted to pitch `25`. Then the
same `sleep(.3)` + two-stage `_2_sit_angs` return as `body_twisting` (the two
functions share that ending verbatim).

#### `push_up(my_dog, speed=80)` (lines 195–198)

```python
my_dog.head_move([[0, 0, -80], [0, 0, -40]], speed=speed-10)
my_dog.do_action('push_up', speed=speed)
my_dog.wait_all_done()
```

Delegates the leg work to `actions_dict['push_up']` (two frames) and adds a head
dip/lift, deliberately **10 slower** than the legs so the head lags — the head
"follows" the body rather than snapping with it. Note `-80` pitch is far outside
`HEAD_PITCH_MIN = -45` and gets clamped to `-45` in the worker thread; the frame
is effectively "head fully down".

#### `sit_2_stand(my_dog, speed=75)` (lines 326–340)

```python
sit_angles   = my_dog.actions_dict['sit'][0][0]      # fetched, unused
stand_angles = my_dog.actions_dict['stand'][0][0]
L1 = [25, 25, -25, -25, 70, -25, -70, 25]            # brace pose
my_dog.legs_move([L1, stand_angles], immediately=False, speed=speed)
```

Standing up from a sit cannot be a single interpolation — the feet would slip
and the dog would fall backwards. `L1` is an intermediate pose that tucks the
front legs under the body first; only then does it extend to `stand_angles`.
`ActionFlow.change_poseture` calls this with `speed=75` and the comment
`# speed > 70`, because below ~70 the servos are too slow to overcome the body
weight mid-transition.

`sit_angles` is read and never used — the commented-out first frame on line 334
shows it used to be the sequence's starting frame.

Note `stand_angles` is *computed*, not a literal: `actions_dictionary.stand`
calls `Pidog.legs_angle_calculation(...)` with the current barycentre and
height, so this routine automatically respects
`ActionDict.set_height()` / `set_barycenter()`.

#### `feet_shake(my_dog, step=None)` (lines 285–323)

The only routine that builds its frames **relative to the current pose**:

```python
current_legs = list.copy(my_dog.leg_current_angles)
L1 = list.copy(current_legs);  L1[0] += 10;  L1[1] -= 25   # left front shakes
L2 = list.copy(current_legs);  L2[2] -= 10;  L2[3] += 25   # right front shakes
```

Then it randomly picks one of three sequences — `[L1, L1, L2, L2]` (both paws),
`[L1, current]` (left only), `[L2, current]` (right only) — repeats it
`step` times (`random.randint(1, 2)` if not given) at a lazy `speed=45`, and
finally returns to `sit` with the head at `-40`.

Two consequences of the relative construction: it only looks right if
`leg_current_angles` is a sit-like pose when called, and `leg_current_angles` is
the *commanded* angle from the driver's worker thread, so calling this mid-motion
snapshots an intermediate pose.

### 4.3 Bark / alert family

#### `bark(my_dog, yrp=None, pitch_comp=0, roll_comp=0, volume=100)` (lines 178–192)

Head-only bark:

```python
head_up   = [0+yrp[0], 0+yrp[1], 25+yrp[2]]
head_down = [0+yrp[0], 0+yrp[1],  0+yrp[2]]
my_dog.wait_head_done()                  # let any prior head motion settle
head_move([head_up], …, immediately=True, speed=100)
my_dog.speak('single_bark_1', volume)    # fire the sound as the head snaps up
my_dog.wait_head_done(); sleep(0.08)
head_move([head_down], …, immediately=True, speed=100)
my_dog.wait_head_done(); sleep(0.5)      # refractory gap between barks
```

`yrp` is a base orientation the whole gesture is offset by — `ActionFlow` passes
`self.head_yrp` so the bark happens *wherever the head is currently aimed*
(e.g. at a tracked face) rather than always straight ahead. The `sleep(0.08)`
is the snap-and-hold at the top; the trailing `sleep(0.5)` prevents machine-gun
barking when called in a loop.

Note the hard-coded sound: unlike `bark_action`, `bark` always plays
`single_bark_1`.

#### `bark_action(my_dog, yrp=None, speak=None, volume=100)` (lines 127–147)

Whole-body bark — the front end lunges as the head snaps up:

```python
f1 = my_dog.legs_angle_calculation([[0, 100], [0, 100], [30, 90], [30, 90]])
f2 = my_dog.legs_angle_calculation([[-20, 90], [-20, 90], [0, 90], [0, 90]])
```

These are the only frames in the file expressed as **foot coordinates**
(`[y, z]` in mm per leg) and run through the inverse kinematics
(`Pidog.legs_angle_calculation`, a classmethod — see `pidog.md` §12.7) instead of
being hand-tuned joint angles. `f1` = tall and rocked back (z = 100 front,
90 hind); `f2` = front feet pulled 20 mm backwards and lowered = the lunge.

Legs and head are moved together with `immediately=True` (pre-empt), the sound
is optional (`speak=None` ⇒ silent lunge). `ActionFlow` maps `"bark harder"` to
`bark_action(..., 'single_bark_1')` preceded by `attack_posture`.

#### `attack_posture(my_dog)` (lines 225–231)

Just the `f2` pose from `bark_action` (the crouched lunge stance), held. Used as
the `before` step of `"bark harder"` so the dog coils before it barks.

#### `alert(my_dog, pitch_comp=0)` (lines 465–486)

Two-frame body startle (legs stiffen: hind hips `80 → 88`; head dips 5° then
lifts 10°) at `speed=100`, then a slow scan: yaw `+30`, `sleep(1)`, yaw `-30`,
`sleep(1)`, back to centre. The one-second holds are what make it read as
"looking around for the source" rather than a twitch.

Not referenced by `ActionFlow`; available for direct use by examples.

### 4.4 Idle / breathing

#### `waiting(my_dog, pitch_comp)` (lines 273–283)

```python
global last_wait            # vestigial: declared, never assigned or read
p0..p3 = [0, ±7, pitch_comp±5]
choice = random.choices(p, [1,1,1,1])[0]
my_dog.head_move([choice], immediately=False, speed=5)
my_dog.wait_head_done()
```

Picks one of four tiny head offsets (±7° roll, ±5° pitch around the compensated
neutral) and drifts to it at **`speed=5`** — the slowest speed used anywhere in
the package. This is the "idling / breathing" motion `ActionFlow` plays every
2–6 seconds while in `STANDBY`. Uniform weights make `random.choices` here
equivalent to `random.choice`.

The `global last_wait` statement is dead: nothing in the package defines or
assigns `last_wait`. It presumably once prevented picking the same offset twice
in a row.

`pitch_comp` is **positional and required** here, unlike every other routine
where it is a keyword with a default.

### 4.5 Procedural head animations (sin/cos generated)

These four build a dense list of frames from a trigonometric expression and hand
the whole list to `head_move_raw` in one call, so the driver interpolates
through them back-to-back — that is what makes them look smooth rather than
stepped.

#### `shake_head_smooth(my_dog, pitch_comp=0, amplitude=40, speed=90)` (lines 162–175)

```python
for i in range(0, 31, 2):
    y = round(amplitude * sin(pi/10 * i), 2)
    angs.append([y, 0, pitch_comp])
```

`sin(π·i/10)` has period `i = 20`, so `i` from 0 to 30 in steps of 2 gives
**1.5 full cycles** in 16 frames: right, left, right, ending mid-swing at
`sin(3π) = 0` — i.e. back at centre. Pure yaw; roll fixed at 0 and pitch fixed
at the compensation value.

#### `shake_head(my_dog, yrp=None)` (lines 150–159)

The non-procedural version: three discrete poses (`+40`, `-40`, `0` yaw) at
`speed=92`, queued back-to-back. Default `yrp = [0, 0, -20]`, i.e. a slightly
lowered head — note this default differs from every other routine's `[0, 0, 0]`.
`ActionFlow` calls this one, adding `head_pitch_init` into the pitch element
manually because `shake_head` has no `pitch_comp` parameter.

#### `nod(my_dog, pitch_comp=-35, amplitude=20, step=2, speed=90)` (lines 387–400)

```python
for i in range(0, 20*step+1, 2):
    p = round(amplitude * cos(pi/10 * i) - amplitude + pitch_comp, 2)
    angs.append([0, 0, p])
```

`cos(π·i/10) − amplitude` maps the cosine into `[-2·amplitude, 0]`, so the head
**starts at neutral and only ever dips downwards** — a nod, not an oscillation
about centre. `step` is the number of nods (`20·step` covers `step` full
cosine periods).

#### `relax_neck(my_dog, pitch_comp=-35)` (lines 342–384)

Two phases.

*Phase 1 — a rolling neck circle*, 21 procedurally generated frames:

```python
y_ang = round(10 * sin(pi/10*i), 2)
r_ang = round(45 * sin(pi/10*i), 2)
p_ang = round(20 * sin(pi/10*i - pi/2) + pitch_comp, 2)
```

Yaw and roll are in phase (amplitudes 10 and 45), pitch is **90° out of phase**
(`−π/2`) with amplitude 20 — a phase offset between orthogonal axes is exactly
what traces a circle, so the muzzle sweeps a cone. `i` from 0 to 20 = one full
period.

*Phase 2 — discrete side stretches*: roll to `+45`, back off to `+25`, again,
return to centre, hold two frames, then the mirror image on `-45`/`-25`. The
duplicated `[0, 0, 5+pitch_comp]` frames are the hold at centre; the trailing
frame drops the `+5` to end at exactly `pitch_comp`. Commented-out `±35` frames
show the original, gentler tuning.

### 4.6 Expressive head poses (single frame)

Four near-identical one-liners; each queues a single `head_move_raw` frame at
`speed=80` and waits:

| Function | Frame `[yaw, roll, pitch]` | Reads as |
| --- | --- | --- |
| `think(pitch_comp=0)` | `[20, -15, 15+pitch_comp]` | head cocked up-and-left |
| `recall(pitch_comp=0)` | `[-20, 15, 15+pitch_comp]` | the mirror image — looking up-and-right |
| `head_down_left(pitch_comp=0)` | `[25, 0, -35+pitch_comp]` | looking down-left |
| `head_down_right(pitch_comp=0)` | `[-25, 0, -35+pitch_comp]` | looking down-right |

`think`/`recall` are wired into `ActionFlow`; the two `head_down_*` are not, and
have no callers in the repo.

#### `fluster(my_dog, pitch_comp=0)` (lines 437–463)

Five fast repetitions (`speed=100`) of a four-frame yaw jitter
(`-10 → 0 → +10 → 0`). The leg half of the routine is **fully commented out**:

```python
# current_legs = list.copy(my_dog.leg_current_angles)
current_legs = [30, 60, -30, -60, 80, -45, -80, 45]
L1 = …; L2 = …; leg1 = [L1, L1, L2, L2]
for _ in range(5):
    # my_dog.legs_move(leg1, immediately=False, speed=100)
    my_dog.head_move_raw(h_l, speed=100)
```

So `current_legs`, `L1`, `L2` and `leg1` are all computed and discarded every
call — dead code. Note also `L2[3]` is never adjusted here, unlike the
equivalent block in `feet_shake`, which suggests the leg half was abandoned
mid-tuning.

#### `surprise(my_dog, pitch_comp=0, status='sit')` (lines 489–526)

The only routine with a posture parameter, because a startle looks different
sitting versus standing:

* `status='sit'` — front knees snap `50 → 80`, hind hips `80 → 88` (the body
  rears back), head dips 5° then lifts 10°, all at `speed=100`; `sleep(1)` to
  hold the reaction; then a `speed=80` relax back to the plain sit pose.
* `status='stand'` — a smaller version from the stand pose, at `speed=80`
  throughout (a standing dog cannot snap as hard without falling).

`ActionFlow` always calls it with the default `'sit'`.

### 4.7 Sound-led routines

#### `pant(my_dog, yrp=None, pitch_comp=0, speed=80, volume=100)` (lines 96–107)

```python
h = [h1, h2, h1]                     # neutral, -10° pitch, neutral
my_dog.speak('pant', volume)         # start the audio first (non-blocking)
sleep(0.01)
for _ in range(6):
    my_dog.head_move(h, pitch_comp=pitch_comp, immediately=False, speed=speed)
    my_dog.wait_head_done()
```

Six head bobs synchronised *by construction* to `pant.mp3` — the sound is
started first and the 6 × 3-frame motion is tuned to run for about as long. The
`sleep(0.01)` yields long enough for the audio thread to actually begin.

#### `howling(my_dog, volume=100)` (lines 201–222)

The most elaborate sequence, and the only one that drives the **RGB chest
strip**:

1. Sit, head to pitch `-30` (`speed=95`).
2. `rgb_strip.set_mode('speak', color='cyan', bps=0.6)` — the chest light
   pulses in "speak" style at 0.6 beats/s for the duration of the howl.
3. `half_sit` (a crouch, from `actions_dictionary`) with the head dropped to
   `-60` — winding up.
4. `speak('howling', volume)` and simultaneously rise back to `sit` with the head
   thrown up to `+10` — the howl itself.
5. The same sit + head-up pose is issued **a second time** (lines 215–217) at a
   different head speed; since the pose is already reached this is effectively a
   no-op hold.
6. `sleep(2.34)` — a magic number: the remaining length of `howling.mp3`, held
   with the head up so the pose lasts as long as the audio.
7. Return to sit with the head down at `-40`.

The RGB mode is **never reset** — the chest strip stays in cyan "speak" mode
after the routine ends; the caller has to set it back. Note also that `-60`
pitch is clamped to `HEAD_PITCH_MIN = -45` by the driver.

---

## 5. The `__main__` block (lines 554–655)

```python
if __name__ == "__main__":
    from pidog import Pidog
    import readchar
    yrp = [0, 0, -40]
    my_dog = Pidog()
    my_dog.rgb_strip.set_mode('listen', 'cyan', 1)
    my_dog.do_action('sit', speed=80)
    my_dog.head_move_raw([[0, 0, -25]], immediately=False, speed=68)
    my_dog.wait_all_done()
    sleep(.5)
    # scratch(my_dog)
    # while True: nod(my_dog, …)
    …
```

A **developer scratchpad**, not a demo. Running
`python3 -m pidog.preset_actions` initialises the robot, sets the chest strip to
cyan "listen", sits it down with the head at `-25`, waits half a second — and
then does nothing, because every actual test invocation below is commented out.
The pattern (`while True: <routine>; sleep(2)`) is how each animation was tuned:
uncomment one block, run, adjust the constants, repeat.

Consequences: `readchar` is imported but unused (an extra dependency for anyone
running the module directly), `yrp` is assigned and unused, `my_dog.close()` is
commented out so the process never exits cleanly (the ultrasonic threads are
non-daemon — see `pidog.md` §9), and the file has no `-h`/argument handling.

---

## 6. Cross-reference: who calls what

| Routine | `ActionFlow` name | Direct example users |
| --- | --- | --- |
| `bark` | `bark` | `3_patrol.py`, `7_face_track.py`, `8_pushup.py`, `13_ball_track.py` |
| `bark_action` | `bark harder` | `4_response.py` |
| `attack_posture` | `bark harder` (as `before`) | — |
| `pant` | `pant` | `1_wake_up.py` |
| `body_twisting` | `twist body` | `1_wake_up.py` |
| `shake_head` | `shake head` | `5_rest.py` |
| `push_up` | `push up` | `8_pushup.py` |
| `howling` | `howling` | `9_howling.py` |
| `stretch` | `stretch` | — |
| `scratch`, `hand_shake`, `high_five`, `lick_hand`, `feet_shake`, `waiting`, `relax_neck`, `nod`, `think`, `recall`, `fluster`, `surprise` | same-named entries | via `11_keyboard_control.py` / `12_app_control.py` star-imports |
| `sit_2_stand` | used by `change_poseture`, not an action | — |
| `shake_head_smooth`, `alert`, `head_down_left`, `head_down_right` | **not wired in** | only the commented `__main__` blocks |

---

## 7. Known issues / improvement candidates

1. **No `__all__`** — the star-import in `action_flow.py` silently re-exports
   `random`, `sleep`, `sin`, `cos`, `pi`, and `ActionFlow` *depends* on the
   `random` leak. Adding `__all__` without adding `import random` to
   `action_flow.py` breaks the idle loop.
2. **`fluster` computes `current_legs`, `L1`, `L2`, `leg1` and discards them** —
   the leg half is commented out. Either restore it or delete the dead code.
3. **`global last_wait` in `waiting()`** refers to a variable that does not
   exist anywhere in the package.
4. **`sit_2_stand` fetches `sit_angles` and never uses it.**
5. **The 4-frame `hand_down_angs` block is duplicated verbatim three times**
   (`hand_shake`, `high_five`, `lick_hand`), and the `_2_sit_angs` ending twice
   (`body_twisting`, `stretch`). Both are extraction candidates.
6. **Magic sleeps tied to audio length** — `sleep(2.34)` in `howling`, the
   6-iteration loop in `pant`. Any change to the sound files silently desyncs
   the animation; there is no query of the clip duration.
7. **`howling` leaves the RGB strip in `'speak'`/cyan mode** and never restores
   the previous mode.
8. **Out-of-range head angles are relied upon to be clamped** by the driver:
   `push_up` commands pitch `-80` and `howling` commands `-60`, both clamped to
   `HEAD_PITCH_MIN = -45`. Works, but the intent ("as far down as possible")
   is not explicit.
9. **`waiting(my_dog, pitch_comp)` takes `pitch_comp` positionally with no
   default**, inconsistent with every other routine.
10. **`shake_head` defaults to `yrp=[0, 0, -20]`** while all its siblings default
    to `[0, 0, 0]`, and it has no `pitch_comp` parameter — callers must fold the
    compensation into the pitch element themselves.
11. **`feet_shake` reads `my_dog.leg_current_angles`**, the *commanded* pose from
    the driver's worker thread; calling it mid-motion produces a distorted
    animation. It also assumes a sit-like starting pose.
12. **No error handling anywhere** — a missing sound file only produces a warning
    from `Pidog.speak`, but a hardware fault mid-routine propagates to the
    caller (`ActionFlow.run` catches and prints it).
13. **`__main__` imports `readchar` without using it** and never calls
    `my_dog.close()`, so running the module directly leaves the process hanging.
14. **Repetition counts are hard-coded** (`range(10)` in `scratch`, `range(8)` in
    `hand_shake`, `range(3)` in `lick_hand`, `range(5)` in `fluster`,
    `range(6)` in `pant`) — unlike `nod`/`feet_shake`, which take a `step`
    parameter.
