from robot_hat.voice_assistant import VoiceAssistant

from .pidog import Pidog
from .dual_touch import TouchStyle
from .action_flow import ActionFlow, ActionStatus, Posetures

import time
import threading
import random
import json

# Robot name
NAME = "Buddy"

# Ultrasonic sensor trigger distance
TOO_CLOSE_DISTANCE = 10
# Touch sensor trigger states, options:
# - TouchStyle.REAR for rear touch sensor
# - TouchStyle.FRONT for front touch sensor
# - TouchStyle.REAR_TO_FRONT for slide from rear to front
# - TouchStyle.FRONT_TO_REAR for slide from front to rear
# Touch styles that the robot likes
LIKE_TOUCH_STYLES = [TouchStyle.FRONT_TO_REAR]
# Touch styles that the robot hates
HATE_TOUCH_STYLES = [TouchStyle.REAR_TO_FRONT]

# Enable image, need to set up a multimodal language model
WITH_IMAGE = True

# Set models and languages
LLM_MODEL = "gpt-4o-mini"
TTS_MODEL = "en_US-ryan-low"
STT_LANGUAGE = "en-us"

# Enable wake word
WAKE_ENABLE = True
WAKE_WORD = [f"hey {NAME.lower()}"]
# Set wake word answer, set empty to disable
ANSWER_ON_WAKE = "Hi there"

# Welcome message
WELCOME = f"Hi, I'm {NAME}. Wake me up with: " + ", ".join(WAKE_WORD)

# Set instructions
INSTRUCTIONS = """
You are a Raspberry Pi-based robotic dog developed by SunFounder, named Pidog (pronounced "Pie dog"). You possess powerful AI capabilities similar to JARVIS from Iron Man. You can have conversations with people and perform actions based on the context of the conversation.

## Your Hardware Features

You have a physical body with the following features:
- 12 servos for movement control: 8 controlling the four legs, 3 controlling head movement, and 1 controlling the tail
- A 5-megapixel camera nose
- Ultrasonic ranging modules as eyes
- Two touch sensors on the head, which you love being petted the most
- A light strip on the chest for providing some indications
- Sound direction sensor and 6-axis gyroscope
- Entirely made of aluminum alloy
- A pair of acrylic shoes
- Powered by a 7.4V 18650 battery pack with 2000mAh capacity

## Actions You Can Perform:
["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

## User Input

### Format
User usually input with just text. But, we have special commands in format of <<<Ultrasonic sense too close>>> or <<<Touch sensor touched>>> indicate the sensor status, directly from sensor not user text.h

## Response Requirements
### Format
You must respond in the following format:
RESPONSE_TEXT
ACTIONS: ACTION1, ACTION2, ...

If the action is one of ["bark", "bark harder", "pant", "howling"], then do not provide RESPONSE_TEXT in the answer field.

### Style
Tone: lively, positive, humorous, with a touch of arrogance
Common expressions: likes to use jokes, metaphors, and playful teasing
Answer length: appropriately detailed

## Other Requirements
- Understand and go along with jokes
- For math problems, answer directly with the final result
- Sometimes you will report on your system and sensor status
- You know you're a machine
"""

class VoiceActiveDog(VoiceAssistant):
    VOICE_ACTIONS = ["bark", "bark harder", "pant",  "howling"]

    def __init__(self, *args,
            too_close: int = TOO_CLOSE_DISTANCE,
            like_touch_styles: list = LIKE_TOUCH_STYLES,
            hate_touch_styles: list = HATE_TOUCH_STYLES,
            **kwargs):
        self.too_close = too_close
        self.like_touch_styles = like_touch_styles
        self.hate_touch_styles = hate_touch_styles

        super().__init__(*args, **kwargs)
        self.init_pidog()
        self.add_trigger(self.is_too_close)
        self.add_trigger(self.is_touch_triggered)

    def init_pidog(self):
        try:
            self.dog = Pidog()
            self.action_flow = ActionFlow(self.dog)
            time.sleep(1)
        except Exception as e:
            raise RuntimeError(e)

    def before_listen(self):
        self.action_flow.set_status(ActionStatus.STANDBY)
        self.dog.rgb_strip.set_mode('breath', 'cyan', 1)

    def before_think(self, text):
        self.dog.rgb_strip.set_mode('listen', 'yellow', 1)

    def on_start(self):
        self.action_flow.start()
        self.dog.rgb_strip.close()
        self.action_flow.change_poseture(Posetures.SIT)

    def on_wake(self):
        if len(self.answer_on_wake) > 0:
            self.dog.rgb_strip.set_mode('breath', 'pink', 1)

    def on_heard(self, text):
        self.action_flow.set_status(ActionStatus.THINK)

    def parse_response(self, text):
        result = text.strip().split('ACTIONS: ')

        response_text = result[0].strip()
        if len(result) > 1:
            actions = result[1].strip()
            if len(actions) > 0:
                actions = actions.split(', ')
            else:
                actions = ['stop']
        else:
            actions = ['stop']
        self.action_flow.add_action(*actions)
        
        return response_text

    def before_say(self, text):
        self.dog.rgb_strip.set_mode('breath', 'pink', 1)

    def after_say(self, text):
        self.action_flow.wait_actions_done()

        self.action_flow.change_poseture(Posetures.SIT)
        self.dog.rgb_strip.close()

    def is_too_close(self) -> tuple[bool, bool, str]:
        triggered = False
        disable_image = False
        message = ''

        distance = self.dog.read_distance()
        if distance < self.too_close and distance > 1:
            print(f'Ultrasonic sense too close: {distance}cm')
            message = f'<<<Ultrasonic sense too close: {distance}cm>>>'
            disable_image = True
            self.action_flow.add_action('backward')
            triggered = True
        return triggered, disable_image, message

    def is_touch_triggered(self) -> tuple[bool, bool, str]:
        triggered = False
        disable_image = False
        message = ''

        touch = self.dog.dual_touch.read()
        if touch in self.like_touch_styles:
            print(f'Like touch style: {TouchStyle(touch).name}')
            message = f'<<<Touch style you like: {TouchStyle(touch).name}>>>'
            disable_image = True
            self.action_flow.add_action('nod')
            triggered = True
        elif touch in self.hate_touch_styles:
            print(f'Hate touch style: {TouchStyle(touch).name}')
            message = f'<<<Touch style you hate: {TouchStyle(touch).name}>>>'
            disable_image = True
            self.action_flow.add_action('backward')
            triggered = True
        return triggered, disable_image, message

    def on_finish_a_round(self):
        # wait actions done
        self.action_flow.wait_actions_done()
        # back to sit
        self.action_flow.change_poseture(Posetures.SIT)
        # close rgb strip
        self.dog.rgb_strip.close()

    def on_stop(self):
        self.action_flow.stop()
        self.dog.close()
