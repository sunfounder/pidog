# PiDog V2 Standard Install Layout

This skill assumes a SunFounder PiDog V2 installed roughly like this under the user's home directory:

- `~/pidog`
- `~/robot-hat`
- `~/vilib`

Typical tutorial flow from SunFounder materials:

1. Install system dependencies such as `git`, `python3-pip`, `python3-setuptools`, `python3-smbus`
2. Clone and install `robot-hat`
3. Clone and install `vilib`
4. Clone and install `pidog`
5. Run the audio setup script if needed

For this skill, treat the local machine as the source of truth if actual paths or import names differ.

## Expected examples location

If the user followed the docs, examples are likely under:
- `~/pidog/examples/`

## Assumptions baked into the skill

- default system Python is used
- `pip3 install .` made `import pidog` work
- the user wants a broadly compatible skill, not a custom one-off for a single workstation

If these assumptions fail, adapt the skill only after confirming the user's local layout.