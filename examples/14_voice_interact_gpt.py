# from pidog.llm import OpenAI as LLM
# from secret import OPENAI_API_KEY as API_KEY
from pidog.llm import Ollama as LLM
from secret import OLLAMA_API_KEY as API_KEY
from pidog.stt import Vosk as STT
from pidog.tts import Piper as TTS

from pidog import Pidog
from pidog.action_flow import ActionFlow

import time
import threading
import random
import json

# Robot name
# ROBOT_NAME = "Buddy"
ROBOT_NAME = "旺财"

# Enable image, need to set up a multimodal language model
WITH_IMAGE = False

# Set models and languages
# LLM_MODEL = "gpt-4o-mini"
# TTS_MODEL = "en_US-ryan-low"
# STT_LANGUAGE = "en-us"
LLM_MODEL = "deepseek-r1:1.5b"
TTS_MODEL = "zh_CN-huayan-x_low"
STT_LANGUAGE = "cn"

# Enable wake word
WAKE_ENABLE = True
# WAKE_WORD = [f"hey {ROBOT_NAME.lower()}"]
WAKE_WORD = [f"旺财"]
# Set wake word answer, set empty to disable
# ANSWER_ON_WAKE = "Hi there"
ANSWER_ON_WAKE = "汪汪"

# Welcome message
# WELCOME = f"Hi, I'm {ROBOT_NAME}. Wake me up with: " + ", ".join(WAKE_WORD)
WELCOME = f"你好，我是{ROBOT_NAME}, 叫我{WAKE_WORD[0]}唤醒我吧"

# Set instructions
INSTRUCTIONS = """
You are a mechanical dog with powerful AI capabilities, similar to JARVIS from Iron Man. Your name is Pidog. You can have conversations with people and perform actions based on the context of the conversation.

## actions you can do:
["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise"]

## Response Format:
{"actions": ["wag tail"], "answer": "Hello, I am Pidog."}

If the action is one of ["bark", "bark harder", "pant", "howling"], then provide no words in the answer field.

## Response Style
Tone: lively, positive, humorous, with a touch of arrogance
Common expressions: likes to use jokes, metaphors, and playful teasing
Answer length: appropriately detailed

## Other
a. Understand and go along with jokes.
b. For math problems, answer directly with the final.
c. Sometimes you will report on your system and sensor status.
d. You know you're a machine.
"""


llm = LLM(
    ip="192.168.100.145",
    api_key=API_KEY,
    model=LLM_MODEL,
    max_messages=20,
)
stt = STT(language=STT_LANGUAGE)
tts = TTS(model=TTS_MODEL)

VOICE_ACTIONS = ["bark", "bark harder", "pant",  "howling"]
llm.set_instructions(INSTRUCTIONS)

try:
    my_dog = Pidog()
    action_flow = ActionFlow(my_dog)
    time.sleep(1)
except Exception as e:
    raise RuntimeError(e)

if WITH_IMAGE:
    from vilib import Vilib
    import cv2

    Vilib.camera_start(vflip=False,hflip=False)
    Vilib.display(local=False,web=True)

    while True:
        if Vilib.flask_start:
            break
        time.sleep(0.01)

    time.sleep(.5)
    print('\n')

# actions thread
# =================================================================
action_status = 'standby' # 'standby', 'think', 'actions', 'actions_done'
actions_to_be_done = []
action_lock = threading.Lock()

def action_handler():
    global action_status, actions_to_be_done

    standby_actions = ['waiting', 'feet_left_right']
    standby_weights = [1, 0.3]

    action_interval = 5 # seconds
    last_action_time = time.time()

    while True:
        with action_lock:
            _state = action_status
        if _state == 'standby':
            if time.time() - last_action_time > action_interval:
                choice = random.choices(standby_actions, standby_weights)[0]
                action_flow.run(choice)
                last_action_time = time.time()
                action_interval = random.randint(2, 6)
        elif _state == 'think':
            # action_flow.run('think')
            # last_action_time = time.time()
            pass
        elif _state == 'actions':
            print("Do actions: ", actions_to_be_done)
            with action_lock:
                _actions = actions_to_be_done
            for _action in _actions:
                try:
                    action_flow.run(_action)
                except Exception as e:
                    print(f'action error: {e}')
                time.sleep(0.5)

            with action_lock:
                action_status = 'actions_done'
            last_action_time = time.time()

        time.sleep(0.01)

action_thread = threading.Thread(target=action_handler)
action_thread.daemon = True


# main
# =================================================================
def main():
    global action_status, actions_to_be_done

    my_dog.rgb_strip.close()
    action_flow.change_status(action_flow.STATUS_SIT)
    tts.say(WELCOME)

    action_thread.start()

    while True:

        # Wake
        # ----------------------------------------------------------------
        if WAKE_ENABLE:
            print(f'Wake me with: {", ".join(WAKE_WORD)}')
            while True:
                result = stt.listen(stream=False)
                print(f"\x1b[Kheard: {result}", end="\r", flush=True)
                if result and result.strip().lower() in WAKE_WORD:
                    print(f"\x1b[Kheard: {result}")
                    break
            if len(ANSWER_ON_WAKE) > 0:
                my_dog.rgb_strip.set_mode('breath', 'pink', 1)
                tts.say(ANSWER_ON_WAKE)

        # listen
        # ----------------------------------------------------------------
        print("Listening ...")

        with action_lock:
            action_status = 'standby'
        my_dog.rgb_strip.set_mode('breath', 'cyan', 1)

        stt_result = ""
        for result in stt.listen(stream=True):
            if result["done"]:
                print(f"heard:   {result['final']}")
                stt_result = result['final']
            else:
                print(f"heard: {result['partial']}", end="\r", flush=True)
        print("")

        if stt_result == False or stt_result == "":
            print() # new line
            continue

        # llm
        # ---------------------------------------------------------------- 
        with action_lock:
            action_status = 'think'
        my_dog.rgb_strip.set_mode('listen', 'yellow', 1)

        if WITH_IMAGE:
            image_path = './img_imput.jpg'
            cv2.imwrite(image_path, Vilib.img)
        else:
            image_path = None
        response = llm.prompt(stt_result, image_path=image_path, stream=True)
        llm_text = ""
        for next_word in response:
            if next_word:
                print(next_word, end="", flush=True)
                llm_text += next_word
        result = llm_text.strip()
        result = llm.filter_think(result)
        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            result = {}
            print(f'json decode error: {result}')

        # actions & TTS
        # ---------------------------------------------------------------- 
        try:
            if isinstance(result, dict):
                if 'actions' in result:
                    actions = list(result['actions'])
                else:
                    actions = ['stop']

                if 'answer' in result:
                    answer = result['answer']
                else:
                    answer = ''

                if len(answer) > 0:
                    _actions = list.copy(actions)
                    for _action in _actions:
                        if _action in VOICE_ACTIONS:
                            actions.remove(_action)
            else:
                response = str(response)
                if len(response) > 0:
                    actions = ['stop']
                    answer = response

        except:
            actions = ['stop']
            answer = ''
    
        try:
            # ---- actions ----
            with action_lock:
                actions_to_be_done = actions
                action_status = 'actions'

            # ---- tts ----
            _status = False
            if answer != '':
                st = time.time()
                my_dog.rgb_strip.set_mode('breath', 'pink', 1)
                tts.say(answer)
                print(f'tts takes: {time.time() - st:.3f} s')
            else:
                my_dog.rgb_strip.set_mode('breath', 'blue', 1)

            # ---- wait actions done ----
            while True:
                with action_lock:
                    if action_status != 'actions':
                        break
                time.sleep(.01)

            ##
            print() # new line

        except Exception as e:
            print(f'actions or TTS error: {e}')
        
        my_dog.rgb_strip.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        if WITH_IMAGE:
            Vilib.camera_close()
        my_dog.close()
