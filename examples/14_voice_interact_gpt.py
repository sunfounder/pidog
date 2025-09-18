from pidog.llm import OpenAI
from pidog.stt import Vosk as STT
from pidog.tts import Piper as TTS
from secret import OPENAI_API_KEY

from pidog import Pidog
from pidog.action_flow import ActionFlow

import time
import threading
import random

WITH_IMAGE = True
WAKE_ENABLE = True
WAKE_WORD = ["doggie"]

llm = OpenAI(api_key=OPENAI_API_KEY, model="gpt-4o-mini")
stt = STT(language="en-us")
tts = TTS(voice="en-us-ryan-low")

VOICE_ACTIONS = ["bark", "bark harder", "pant",  "howling"]

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
    global speech_loaded
    global action_status, actions_to_be_done
    global tts_file

    my_dog.rgb_strip.close()
    action_flow.change_status(action_flow.STATUS_SIT)

    speak_thread.start()
    action_thread.start()

    while True:

        # Wake
        if WAKE_ENABLE:
            result = stt.wait_until_heard(WAKE_WORD)
            if result:
                print(f"wake word heard: {result}")

        # listen
        # ----------------------------------------------------------------
        print("Listening ...")

        with action_lock:
            action_status = 'standby'
        my_dog.rgb_strip.set_mode('listen', 'cyan', 1)

        stt_result = ""
        for result in stt.listen(stream=True):
            if result["done"]:
                print(f"final:   {result['final']}")
                stt_result = result['final']
            else:
                print(f"partial: {result['partial']}", end="\r", flush=True)

        if stt_result == False or stt_result == "":
            print() # new line
            continue

        # llm
        # ---------------------------------------------------------------- 
        with action_lock:
            action_status = 'think'

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
            # ---- tts ----
            _status = False
            if answer != '':
                st = time.time()
                my_dog.rgb_strip.set_mode('speak', 'pink', 1)
                tts.say(answer)
                print(f'tts takes: {time.time() - st:.3f} s')
            else:
                my_dog.rgb_strip.set_mode('breath', 'blue', 1)

            # ---- actions ----
            with action_lock:
                actions_to_be_done = actions
                print(f'actions: {actions_to_be_done}')
                action_status = 'actions'

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
