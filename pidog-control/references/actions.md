# PiDog Actions

This skill intentionally exposes a small, stable subset of PiDog actions that are clearly present in the public repository and suitable for a general-purpose V2 skill.

## Exposed actions

### stand

```python
dog.do_action('stand', speed=...)
```

Use this to bring PiDog into a stable standing posture.
If using the helper script, prefer `action stand --hold` when the user wants PiDog to remain standing after the command exits. The helper now attempts to stop the previous hold owner automatically before taking over.

### sit

```python
dog.do_action('sit', speed=...)
```

Use this for a safe, expressive idle posture.
If using the helper script, prefer `action sit --hold` when the user wants the posture to remain after the command exits. The helper now attempts to stop the previous hold owner automatically before taking over.

### lie

```python
dog.do_action('lie', speed=...)
```

Use this to return PiDog to a low, safe resting posture.
If using the helper script, prefer `action lie --hold` when the user wants the posture to remain after the command exits. The helper now attempts to stop the previous hold owner automatically before taking over.

### wag-tail

```python
dog.do_action('wag_tail', speed=...)
```

Use this for a short friendly expression.

### bark

```python
dog.speak('single_bark_1')
```

Use a named built-in sound effect instead of a motion action.
The default bark mapping in this skill uses `single_bark_1`, because real-device validation showed that a generic `bark` sound name is not guaranteed to exist.

## Why this subset

The upstream examples demonstrate many additional actions, including movement and show actions. This skill keeps the default public interface narrow because:
- posture actions are safer than roaming actions
- they are easier for users to test on first run
- they create fewer assumptions about floor space and calibration

## Candidate future additions

If the skill is expanded later, likely next actions are:
- `stretch`
- `forward`
- `backward`
- `turn-left`
- `turn-right`

Add them only if the user asks for them or after real-device validation.