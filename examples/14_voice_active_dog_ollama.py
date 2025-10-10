from pidog.llm import Ollama as LLM

from pidog.dual_touch import TouchStyle
from voice_active_dog import VoiceActiveDog

llm = LLM(
    ip="localhost",
    model="deepseek-r1:1.5b",
)

# Robot name
NAME = "Buddy"

# Ultrasonic sensor sense too close distance in cm
TOO_CLOSE = 10
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
WITH_IMAGE = False

# Set models and languages
TTS_MODEL = "en_US-ryan-low"
STT_LANGUAGE = "en-us"

# Enable keyboard input
KEYBOARD_ENABLE = True

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

vad = VoiceActiveDog(
    llm,
    name=NAME,
    too_close=TOO_CLOSE,
    like_touch_styles=LIKE_TOUCH_STYLES,
    hate_touch_styles=HATE_TOUCH_STYLES,
    with_image=WITH_IMAGE,
    stt_language=STT_LANGUAGE,
    tts_model=TTS_MODEL,
    keyboard_enable=KEYBOARD_ENABLE,
    wake_enable=WAKE_ENABLE,
    wake_word=WAKE_WORD,
    answer_on_wake=ANSWER_ON_WAKE,
    welcome=WELCOME,
    instructions=INSTRUCTIONS,
    disable_think=True,
)

if __name__ == '__main__':
    vad.run()
