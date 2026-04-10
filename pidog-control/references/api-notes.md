# PiDog API Notes from the Public Repository

These notes are distilled from the public `sunfounder/pidog` repository.

## Package entry point

`pidog/__init__.py` exports:

```python
from .pidog import Pidog
```

So the canonical import is:

```python
from pidog import Pidog
```

## Confirmed high-level APIs

From the repository examples and `pidog/pidog.py`:

### Actions
Use:

```python
dog.do_action(name, ...)
```

Examples in the official demos include:
- `stand`
- `sit`
- `lie`
- `stretch`
- `wag_tail`
- `forward`
- `backward`
- `turn_left`
- `turn_right`
- `push_up`

This skill intentionally exposes only a conservative subset for broad compatibility.

### Sound
Use:

```python
dog.speak(name, volume=80)
```

The repository's demo UI lists sound names from the `sounds/` directory.
In practice, availability depends on the installed sound files. Real-device testing showed that `speak('bark')` may not exist on a given installation, so callers should treat a false return as failure.
For this skill's default bark-like sound, use `single_bark_1`.

### Light board
Use:

```python
dog.rgb_strip.set_mode(mode, color=..., bps=..., brightness=...)
```

Examples show at least:
- `listen`
- `breath`
- `boom`

### Waiting
Use:

```python
dog.wait_all_done()
```

### Shutdown
Use:

```python
dog.close()
```

## Why the skill stays narrow

The full PiDog API is richer than this skill needs right now. For a reusable public-facing skill, it is better to:
- expose a small, stable action set
- use officially demonstrated interfaces
- expand only when a new capability is needed