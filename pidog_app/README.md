# pidog_app — AI-driven feature architecture for the Pidog robot dog

This project is the application layer that turns the SunFounder Pidog
hardware into an AI-driven robot dog. It uses an Ollama model running on
your laptop to decide, turn by turn, whether to **answer a question** or
**perform a feature** (wake from stasis, find an object, recognize a
person, check the water bowl, ...).

The dog also has a **sleep/wake mode**: after a configurable idle period
it lies down, dims its chest light, and plays a looping snoring sound.
Petting its head (a front-to-rear touch) wakes it back up and stops the
snoring.

The three SunFounder libraries — `pidog/`, `robot-hat/`, `vilib/` — are
treated as **untouched dependencies**. All application code lives in
`pidog_app/` and talks to the hardware through thin facades, so the
libraries can be updated from upstream without breaking the app.

---

## Architecture

```
                 ┌──────────────────────────────┐
                 │            app.py            │  dependency injection + main loop
                 │   (builds & wires everything)│
                 └──────────────┬───────────────┘
                                │
        ┌───────────┬───────────┼───────────┬────────────┐
        ▼           ▼           ▼           ▼            ▼
     ┌──────┐   ┌──────┐   ┌────────┐   ┌────────┐   ┌────────┐
     │ dog  │   │vision│   │features│   │ brain  │   │   io   │
     │      │   │      │   │        │   │        │   │        │
     │ Body │   │Camera│   │Feature │   │ Brain  │   │TextIO  │
     │Senses│   │      │   │Registry│   │ Prompt │   │VoiceIO │
     └──┬───┘   └──┬───┘   └───┬────┘   └───┬────┘   └────────┘
        │          │           │            │
        │  wraps   │  wraps    │ uses       │ uses
        ▼          ▼           ▼            ▼
   pidog.Pidog  vilib.Vilib   dog/vision   pidog.llm
   ActionFlow                  facades      (Ollama)
   (SunFounder)              (this repo)
```

### Layer responsibilities

| Layer | Folder | Role |
|-------|--------|------|
| **Config** | `config.py`, `config.yaml` | YAML + env-var overrides; single source of truth for IP, model, IO mode, sensor thresholds |
| **Dog facade** | `dog/` | `Body` (movement, posture, head, tail, chest light) and `Senses` (ultrasonic, touch, IMU, sound direction) wrapping `Pidog`/`ActionFlow` |
| **Vision facade** | `vision/` | `Camera` wrapping `Vilib` (capture + face/color/QR/traffic/object/hand/pose detection) |
| **Features** | `features/` | `Feature` base class, `FeatureRegistry`, and one module per capability in `features/instances/` |
| **Brain** | `brain/` | `Brain` runs the LLM tool-calling loop; `prompt.py` builds the system prompt |
| **IO** | `io/` | `IO` interface with `TextIO` (REPL) and `VoiceIO` (Vosk STT + Piper TTS + wake word + sound playback) |
| **App** | `app.py` | Builds the object graph, runs the conversation loop, and manages sleep/wake via background watcher threads |

### The decision flow (chat vs. feature)

The brain uses **OpenAI-style tool/function calling**. Each feature
exposes a `build_schema()` describing itself; the registry collects them
into the `tools` array sent to Ollama. On each user turn:

1. The user message is added to the conversation.
2. The brain calls `llm.chat(tools=...)` against the OpenAI-compatible
   `/v1/chat/completions` endpoint on Ollama.
3. If the model emits a `tool_calls` entry, the brain dispatches it to
   the matching feature, feeds the result back as a `tool` message, and
   loops so the model can compose a reply.
4. If the model replies with plain text, that's the dog's answer — no
   feature runs.

This means **the LLM decides** whether your message is a question (plain
reply) or a feature request (tool call). You don't hand-code intents.

---

## Project layout

```
pidog_app/
├── config.yaml                  # edit me: Ollama IP, model, IO mode, ...
├── pyproject.toml
├── README.md
└── pidog_app/
    ├── __init__.py
    ├── __main__.py              # entry point: python -m pidog_app
    ├── app.py                   # dependency injection + main loop
    ├── config.py                # YAML + env-var config loader
    ├── dog/
    │   ├── __init__.py
    │   ├── body.py              # Body facade (actuators + chest light)
    │   └── senses.py            # Senses facade (sensors, read-only)
    ├── vision/
    │   ├── __init__.py
    │   └── camera.py            # Camera facade over Vilib
    ├── features/
    │   ├── __init__.py
    │   ├── base.py              # Feature ABC + FeatureResult
    │   ├── registry.py          # FeatureRegistry
    │   └── instances/
    │       ├── __init__.py
    │       ├── wake_from_stasis.py
    │       ├── find_object.py
    │       ├── recognize_person.py
    │       └── check_water_bowl.py
    ├── brain/
    │   ├── __init__.py
    │   ├── brain.py             # LLM tool-calling loop
    │   └── prompt.py            # system prompt builder
    ├── io/
    │   ├── __init__.py
    │   ├── base.py              # IO interface (listen, speak, play_sound, stop_sound)
    │   ├── text_io.py           # REPL
    │   └── voice_io.py          # Vosk + Piper + wake word + sound playback
    └── test_hardware.py         # hardware smoke test
```

---

## Setup

The SunFounder libraries must already be installed (editable) on the Pi:

```bash
cd ~/robot-hat  && pip install -e .
cd ~/vilib      && pip install -e .
cd ~/pidog      && pip install -e .
```

Then install this app:

```bash
cd ~/pidog_app
pip install -e .
```

## Configuration

Edit `config.yaml`:

```yaml
dog:
  name: "Scooby Doo"
  sleep_delay: 10              # seconds idle before going to sleep

llm:
  ip: "192.168.0.136"          # your laptop's LAN IP
  port: 11434
  model: "qwen2.5:7b"          # must support tool calling
  max_messages: 20             # conversation history window

io:
  mode: "text"                 # "text" or "voice"
  voice:
    stt_language: "en-us"
    tts_model: "en_US-ryan-low" # Piper model
    wake_enable: true
    wake_word: ["hey scooby"]
    answer_on_wake: "Hi there buddy"
  sounds_path: "/home/pds/pidog/sounds/"  # sound files for play_sound

sensors:
  too_close_cm: 15
  like_touch_styles: ["RS"]    # front-to-rear slide (wakes the dog)
  hate_touch_styles: ["LS"]    # rear-to-front slide

vision:
  camera_vflip: false
  camera_hflip: false

logging:
  level: INFO
  filename: app.log
```

Any value can be overridden with an env var using the prefix `PIDOG_`
and underscores for dots, e.g. `PIDOG_LLM_IP=10.0.0.5`.

> **Note on the LLM endpoint:** the app uses the OpenAI-compatible
> `/v1/chat/completions` endpoint (not Ollama's native `/api/chat`),
> because tool calling requires the standard `choices[0].message.tool_calls`
> response shape. Make sure "Expose Ollama to the network" is enabled in
> your Ollama settings, and that the model you pick supports tool calling
> (`llama3.1`, `qwen2.5`, `mistral-nemo`, ...).

## Running

```bash
# text mode (default)
python -m pidog_app

# voice mode (set io.mode: voice in config.yaml, or:)
PIDOG_IO_MODE=voice python -m pidog_app
```

In text mode you'll get a `>>> ` prompt. Type `quit` to exit. Try:

- *"hey, wake up"* → triggers `wake_from_stasis`
- *"can you find something red?"* → triggers `find_object` with `target=red`
- *"do you see anyone?"* → triggers `recognize_person`
- *"is my water bowl empty?"* → triggers `check_water_bowl`
- *"what's 7 times 8?"* → plain chat reply (no tool)

---

## Sleep & wake mode

The dog automatically goes to sleep after `dog.sleep_delay` seconds of
inactivity (no text/voice input). Two background watcher threads manage
this:

- **Sleep watcher** (`_sleep_watcher`): polls every second. When the
  idle timer exceeds `sleep_delay`, it pauses the action-flow standby
  loop (`ActionStatus.THINK`), lies the dog down, dims the chest light
  to breath-pink at 25% brightness, and plays a looping snoring sound.
- **Wake watcher** (`_wake_watcher`): polls the head touch sensor every
  0.1s while the dog is sleeping. When a `like_touch_styles` touch is
  detected (e.g. front-to-rear petting), it stops the snoring sound,
  sets the chest light to listen-yellow, resumes the action-flow standby
  loop (`ActionStatus.STANDBY`), and clears the sleeping state.

Text or voice input while sleeping does **not** wake the dog — only
physical petting does. The main loop rejects text input with a "pet my
head to wake me up" message while `_sleeping` is true.

---

## Adding a new feature

1. Create `pidog_app/features/instances/my_feature.py`:

   ```python
   from ..base import Feature, FeatureResult

   class MyFeature(Feature):
       name = "my_feature"
       description = "What it does, so the LLM knows when to call it."

       def build_schema(self):
           return {
               "type": "function",
               "function": {
                   "name": self.name,
                   "description": self.description,
                   "parameters": {
                       "type": "object",
                       "properties": {
                           "foo": {"type": "string", "description": "..."},
                       },
                       "required": ["foo"],
                   },
               },
           }

       def run(self, foo: str = "", **kwargs) -> FeatureResult:
           self.body.do("nod")           # use the facades, not Pidog directly
           self.body.wait_done()
           return FeatureResult(text=f"Done with {foo}")
   ```

2. Register it in `pidog_app/app.py` → `build_features()`:

   ```python
   from .features.instances import MyFeature
   return [..., MyFeature(body, senses, camera)]
   ```

That's it — the brain picks it up automatically on the next run.

---

## Why this shape

- **Facades over the SunFounder libs** keep the app decoupled from
  upstream API churn and make features testable without hardware.
- **One class per feature** + a registry means features are isolated and
  additive (no giant `if/elif` chain).
- **Tool calling (not JSON parsing)** lets the model itself choose chat
  vs. action, which generalizes far better than hand-written intents and
  matches how modern LLM frameworks work.
- **IO abstraction** lets you develop with text and ship with voice
  without touching the brain or features.


## Start on boot

### Useful commands to manage the service

systemctl --user start pidog-app —> start now  
systemctl --user stop pidog-app —> stop  
systemctl --user status pidog-app —> check status  
journalctl --user -u pidog-app -f —> live logs  
systemctl --user disable pidog-app —> disable autostart

### Location of the service file

/home/pds/.config/systemd/user/pidog-app.service

### Content of service file

[Unit]
Description=Pidog AI robot dog application  
After=graphical-session.target

[Service]
Type=simple  
WorkingDirectory=/home/pds  
ExecStart=/home/pds/.venv/bin/python -m pidog_app /home/pds/pidog/pidog_app/config.yaml  
Restart=on-failure  
RestartSec=10

[Install]
WantedBy=default.target


## Connect to the PiDog

To connect to the PiDog, you can use the following command to connect to the host:

```bash
ssh user@<pi_dog_ip_address> or ssh user@<hostname>.local

ssh pds@192.168.0.197 or ssh pds@nova.local
```

If you started your application via a service and you want to connect and be able to type input you:
- install tmux on the Pi first
- update the pidog-app.service file to use Type=forking and launch the app inside a detached tmux session named pidog.
- the app now has a real TTY, so input() works normally

To connect to the app after connecting to the host:

```bash
tmux attach -t pidog
```

