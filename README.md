# Pidog

Pidog Python library for Raspberry Pi.

Quick Links:

- [Pidog](#pidog)
  - [Docs](#docs)
  - [Installation](#installation)
    - [install tool](#install-tool)
    - [robot-hat library](#robot-hat-library)
    - [vilib library](#vilib-library)
    - [pidog library](#pidog-library)
    - [i2samp](#i2samp)
  - [Debug records](#debug-records)
  - [About SunFounder](#about-sunfounder)
  - [Contact us](#contact-us)
  - [Credit](#credit)

----------------------------------------------

## Docs

- <https://docs.sunfounder.com/projects/pidog/en/latest/>

----------------------------------------------

## Installation

- <https://docs.sunfounder.com/projects/pidog/en/latest/python/python_start/install_all_modules.html>

### install tool

```bash
sudo apt install git python3-pip python3-setuptools python3-smbus
```

### robot-hat library

```bash
cd ~/
git clone -b 2.5.x --depth=1 https://github.com/sunfounder/robot-hat.git
cd robot-hat
sudo python3 install.py
```

### vilib library

```bash
cd ~/
git clone --depth=1 https://github.com/sunfounder/vilib.git
cd vilib
sudo python3 install.py
```

### pidog library

```bash
cd ~/
git clone --depth=1 https://github.com/sunfounder/pidog.git
sudo pip3 install ~/pidog --break-system-packages
```

### i2samp

```
cd ~/pidog
sudo bash i2samp.sh
```

## Debug records

```bash
sudo pip3 uninstall pidog --break -y && cd ~/pidog && sudo pip3 install . --break --no-deps --no-build-isolation
sudo pip3 uninstall robot_hat --break -y && cd ~/robot-hat && sudo pip3 install . --break --no-deps --no-build-isolation
sudo python3 ~/pidog/examples/14_voice_active_dog_gpt.py
```

----------------------------------------------

## About SunFounder

SunFounder is a technology company focused on Raspberry Pi and Arduino open source community development. Committed to the promotion of open source culture, we strives to bring the fun of electronics making to people all around the world and enable everyone to be a maker. Our products include learning kits, development boards, robots, sensor modules and development tools. In addition to high quality products, SunFounder also offers video tutorials to help you make your own project. If you have interest in open source or making something cool, welcome to join us!

----------------------------------------------

## Contact us

website:
    www.sunfounder.com

E-mail:
    service@sunfounder.com, support@sunfounder.com

## Credit

Most sound effect are from [Zapsplat.com](https://www.zapsplat.com)


# Installation with one or more forked projects

git clone the repositories from there original git location or from a fork.  
Do not 'sudo python3 install.py' on any of them.

After cloning, perform:
Setup: System Python is externally-managed (PEP 668), so I created a venv with system-site-package inheritance (needed for hardware libs like RPi.GPIO, spidev, picamera2):

```
>_ bash

python3 -m venv --system-site-packages /home/pds/.venv
```

Editable installs — links directly to your source folders, so edits take effect immediately without reinstalling:




bash
```
>_ bash

/home/pds/.venv/bin/pip install -e /home/pds/robot-hat -e /home/pds/pidog -e /home/pds/vilib
```

Missing dependencies resolved:

python3-pyaudio (apt) — for robot_hat.music
python3-opencv (apt) — for vilib, matches existing libopencv410 system libs
flask (pip, in-venv) — for vilib's web streaming server
Verified: import pidog, robot_hat, vilib now resolves to __init__.py, __init__.py, __init__.py respectively.

# Python environment on raspberry PI

In a terminal type 'source .venv/bin/activate' otherwise you will receive a 'no permission' error message.