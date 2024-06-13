from openai_helper import OpenAiHelper
from keys import OPENAI_API_KEY, OPENAI_ASSISTANT_ID
from action_flow import ActionFlow
from utils import redirect_error_2_null, cancel_redirect_error, gray_print

import speech_recognition as sr
from vilib import Vilib
import cv2
from pidog import Pidog

import time
import threading
import random

# openai assistant init
# =================================================================
openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'PiDog')

# dog init 
# =================================================================
try:
    my_dog = Pidog()
    time.sleep(1)
except Exception as e:
    raise RuntimeError(e)

action_flow = ActionFlow(my_dog)

# Vilib start
# =================================================================
Vilib.camera_start(vflip=False,hflip=False)
Vilib.display(local=False,web=True)

while True:
    if Vilib.flask_start:
        break
    time.sleep(0.01)

time.sleep(.5)
print('\n')

# speech_recognition init
# =================================================================
'''
self.energy_threshold = 300  # minimum audio energy to consider for recording
self.dynamic_energy_threshold = True
self.dynamic_energy_adjustment_damping = 0.15
self.dynamic_energy_ratio = 1.5
self.pause_threshold = 0.8  # seconds of non-speaking audio before a phrase is considered complete
self.operation_timeout = None  # seconds after an internal operation (e.g., an API request) starts before it times out, or ``None`` for no timeout

self.phrase_threshold = 0.3  # minimum seconds of speaking audio before we consider the speaking audio a phrase - values below this are ignored (for filtering out clicks and pops)
self.non_speaking_duration = 0.5  # seconds of non-speaking audio to keep on both sides of the recording

'''
recognizer = sr.Recognizer()
recognizer.dynamic_energy_adjustment_damping = 0.3
recognizer.dynamic_energy_ratio = 2.2


# speak_hanlder
# =================================================================
speech_loaded = False
speech_lock = threading.Lock()

def speak_hanlder():
    global speech_loaded
    while True:
        with speech_lock:
            _isloaded = speech_loaded
        if _isloaded:
            gray_print('speak start')
            # sound_play(openai_helper.TTS_OUTPUT_FILE)
            my_dog.speak_block(openai_helper.TTS_OUTPUT_FILE)
            gray_print('speak done')
            with speech_lock:
                speech_loaded = False
        time.sleep(0.05)

speak_thread = threading.Thread(target=speak_hanlder)
speak_thread.daemon = True


# actions thread
# =================================================================
action_state = 'standby' # 'standby', 'think', 'actions', 'actions_done'
actions_to_be_done = []
action_lock = threading.Lock()

def action_handler():
    global action_state, actions_to_be_done

    standby_actions = ['waiting', 'feet_left_right']
    standby_weights = [1, 0.3]

    action_interval = 5 # seconds
    last_action_time = time.time()

    while True:
        with action_lock:
            _state = action_state
        if _state == 'standby':
            if time.time() - last_action_time > action_interval:
                choice = random.choices(standby_actions, standby_weights)[0]
                action_flow.run(choice)
                last_action_time = time.time()
                action_interval = random.randint(3, 8)
        elif _state == 'think':
            # my_dog.do_action('tilting_head_left', speed=80)
            # last_action_time = time.time()
            # action_interval = random.randint(3, 8)
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
                action_state = 'actions_done'
            last_action_time = time.time()

        time.sleep(0.01)

action_thread = threading.Thread(target=action_handler)
action_thread.daemon = True

# main
# =================================================================
def main():
    global current_feeling, last_feeling
    global speech_loaded
    global action_state, actions_to_be_done

    my_dog.rgb_strip.close()
    action_flow.change_status(action_flow.STATUS_SIT)

    speak_thread.start()
    action_thread.start()

    while True:
        # listen
        # ----------------------------------------------------------------
        gray_print("listening ...")

        with action_lock:
            action_state = 'standby'
        my_dog.rgb_strip.set_mode('listen', 'cyan', 1)

        _stderr_back = redirect_error_2_null() # ignore error print to ignore ALSA errors
        # If the chunk_size is set too small (default_size=1024), it may cause the program to freeze
        with sr.Microphone(chunk_size=8192) as source:
            cancel_redirect_error(_stderr_back) # restore error print
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
        # stt
        # ----------------------------------------------------------------
        with action_lock:
            action_state = 'think'
        my_dog.rgb_strip.set_mode('boom', 'yellow', 0.5)

        st = time.time()
        _result = openai_helper.stt(audio, language=['zh', 'en'])
        gray_print(f"stt takes: {time.time() - st:.3f} s")

        if _result == False or _result == "":
            print() # new line
            continue

        # chat-gpt
        # ---------------------------------------------------------------- 
        response = {}
        # response = openai_helper.dialogue(_result)

        img_path = './img_imput.jpg'
        cv2.imwrite(img_path, Vilib.img_array[0])

        st = time.time()
        response = openai_helper.dialogue_with_img(_result, img_path)
        gray_print(f'chat takes: {time.time() - st:.3f} s')

        # actions & TTS
        # ---------------------------------------------------------------- 
        try:
            if 'Feeling' in response:
                feeling = response['Feeling']
            else:
                feeling = 'calm'

            if 'actions' in response:
                actions = list(response['actions'])
            else:
                actions = ['stop']

            if 'answer' in response:
                answer = response['answer']
                current_feeling = feeling
            else:
                answer = ''
        except:
            feeling = 'calm'
            actions = ['stop']
            answer = ''
    
        try:
            # ---- tts ----
            _status = False
            if answer != '':
                st = time.time()
                _status = openai_helper.text_to_speech(answer, openai_helper.TTS_OUTPUT_FILE, 'shimmer') # onyx
                gray_print(f'tts takes: {time.time() - st:.3f} s')

                if _status:
                    with speech_lock:
                        speech_loaded = True
                    my_dog.rgb_strip.set_mode('speak', 'pink', 1)
            else:
                my_dog.rgb_strip.set_mode('breath', 'blue', 1)

            # ---- actions ----
            with action_lock:
                # actions_to_be_done = ['bark', 'howling']
                actions_to_be_done = actions
                gray_print(f'actions: {actions_to_be_done}')
                action_state = 'actions'

            # ---- wait speak done ----
            if _status:
                while True:
                    with speech_lock:
                        if not speech_loaded:
                            break
                    time.sleep(.01)


            # ---- wait actions done ----
            while True:
                with action_lock:
                    if action_state != 'actions':
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
        Vilib.camera_close()
        my_dog.close()

