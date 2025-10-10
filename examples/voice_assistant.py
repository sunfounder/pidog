from pidog.llm import OpenAI as LLM
from pidog.stt import Vosk as STT
from pidog.tts import Piper as TTS

import time
import threading
import random
import json

# Robot name
NAME = "Buddy"

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

class VoiceAssistant:
    VOICE_ACTIONS = ["bark", "bark harder", "pant",  "howling"]

    def __init__(self,
            llm: LLM,
            name: str = NAME,
            with_image: bool = False,
            tts_model: str = TTS_MODEL,
            stt_language: str = STT_LANGUAGE,
            wake_enable: bool = True,
            wake_word: list = WAKE_WORD,
            answer_on_wake: str = ANSWER_ON_WAKE,
            welcome: str = WELCOME,
            instructions: str = INSTRUCTIONS,
            disable_think: bool = False,
        ):
        self.llm = llm
        self.name = name
        self.with_image = with_image
        self.wake_enable = wake_enable
        self.wake_word = wake_word
        self.answer_on_wake = answer_on_wake
        self.welcome = welcome
        self.disable_think = disable_think
        self.instructions = instructions.format(name=name)

        self.tts = TTS(model=tts_model)
        self.stt = STT(language=stt_language)
        self.llm.set_instructions(self.instructions)
        self.stt.set_wake_words(self.wake_word)

        self.waked = False
        self.running = False
        self.wake_waiting = False
        self.wait_wake_thread = None
        self.triggers = []

        if self.wake_enable:
            self.add_trigger(self.is_waked)

        if self.with_image:
            self.init_image_sensor()

    def before_listen(self):
        pass

    def after_listen(self, stt_result):
        pass

    def before_think(self, text):
        pass

    def after_think(self, text):
        pass

    def on_start(self):
        pass

    def on_wake(self):
        pass

    def on_heard(self, text):
        pass

    def parse_response(self, text):
        return text

    def add_trigger(self, trigger_function):
        self.triggers.append(trigger_function)

    def before_say(self, text):
        pass

    def after_say(self, text):
        pass

    def on_stop(self):
        pass

    def on_finish_a_round(self, response_text):
        pass

    def is_waked(self) -> tuple[bool, bool, str]:
        triggered = False
        disable_image = False
        message = ''

        if self.stt.is_waked():
            # listen
            self.stt.stop_listening()
            self.on_wake()
            print("Waked, Listening ...")
            message = self.listen()
            self.on_heard(message)
            self.waked = False
            triggered = True
        return triggered, disable_image, message

    def init_image_sensor(self):
        from vilib import Vilib
        import cv2

        self.vilib = Vilib
        self.cv2 = cv2

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=False,web=True)

        while True:
            if Vilib.flask_start:
                break
            time.sleep(0.01)

        time.sleep(.5)
        print('\n')

    def listen(self):
        self.before_listen()

        stt_result = ""
        for result in self.stt.listen(stream=True):
            if self.running == False:
                break
            if result["done"]:
                print(f"heard: {result['final']}")
                stt_result = result['final']
            else:
                print(f"heard: {result['partial']}", end="\r", flush=True)
        print("")

        if stt_result == False or stt_result == "":
            stt_result = None

        self.after_listen(stt_result)
        return stt_result

    def think(self, text, disable_image=False):
        self.before_think(text)

        if self.with_image and not disable_image:
            image_path = './img_input.jpg'
            self.cv2.imwrite(image_path, self.vilib.img)
        else:
            image_path = None
        kwargs = {
            'image_path': image_path,
            'stream': True,
        }
        if self.disable_think:
            kwargs['think'] = False
        response = self.llm.prompt(text, **kwargs)
        llm_text = ""
        for next_word in response:
            if self.running == False:
                break
            if next_word:
                print(next_word, end="", flush=True)
                llm_text += next_word
        print('')
        result = llm_text.strip()
        self.after_think(result)
        return result

    def main(self):

        self.running = True
        self.on_start()
        self.tts.say(self.welcome)

        # Main loop
        while self.running:
            triggered = False
            message = ''
            disable_image = False

            # Start listening wake words if wake enabled
            if self.wake_enable:
                self.stt.start_listening_wake_words()
            
            # Wait for triggers
            while self.running:

                for trigger in self.triggers:
                    triggered, disable_image, message = trigger()
                    if triggered:
                        break
                if triggered:
                    break
                time.sleep(0.01)

            # Stop listening wake words if wake enabled
            if self.wake_enable:
                self.stt.stop_listening()

            # think
            result = self.think(message, disable_image=disable_image)
            response_text = self.parse_response(result)

            # tts
            _status = False
            if response_text != '':
                self.before_say(response_text)
                self.tts.say(response_text)

            # on finish a round
            self.on_finish_a_round()

            # Wait a second before next round
            time.sleep(1)

    def run(self):
        try:
            self.main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"\033[31mERROR: {e}\033[m")
        finally:
            self.running = False
            self.stt.close()
            if self.with_image:
                self.vilib.camera_close()
            self.on_stop()
