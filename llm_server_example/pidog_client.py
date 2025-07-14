# from local_llm_helper import LocalLLMHelper # Removed: LLM is now on server
import requests # Added for HTTP requests
from action_flow import ActionFlow
from utils import *

import readline # optimize keyboard input, only need to import

import speech_recognition as sr
import pyttsx3
from pidog import Pidog

import time
import threading
import random
import argparse
import json # Added for constructing JSON payloads

import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

# --- Configuration ---
# MODEL_PATH_DEFAULT, N_THREADS_DEFAULT, N_CTX_DEFAULT, N_GPU_LAYERS_DEFAULT removed - server responsibility
SERVER_URL_DEFAULT = "http://localhost:5000/process_command" # Default server URL

VOLUME_DB = 3
VOICE_ACTIONS = ["bark", "bark harder", "pant",  "howling"]

# --- Argument Parsing ---
# Changed description to reflect client role
parser = argparse.ArgumentParser(description="Pidog client to interact with an LLM server.")
parser.add_argument(
    '--server_url',
    type=str,
    default=SERVER_URL_DEFAULT,
    help=f'URL of the LLM server (default: {SERVER_URL_DEFAULT})'
)
parser.add_argument(
    '--input_mode',
    type=str,
    default='voice',
    choices=['voice', 'keyboard'],
    help='Input mode: "voice" or "keyboard" (default: voice)'
)
# --model_path, --n_threads, --n_ctx, --n_gpu_layers arguments removed
parser.add_argument(
    '--stt_engine',
    type=str,
    default='sphinx',
    choices=['sphinx', 'google'],
    help='STT engine: "sphinx" (offline) or "google" (online)'
)

cli_args = parser.parse_args()

# Local LLM init section removed
# =================================================================

# dog init
# =================================================================
try:
    my_dog = Pidog()
    time.sleep(1)
except Exception as e:
    print(f"\033[31mERROR: Failed to initialize PiDog: {e}\033[m")
    sys.exit(1)

action_flow = ActionFlow(my_dog)

# speech_recognition init
# =================================================================
recognizer = sr.Recognizer()
recognizer.dynamic_energy_adjustment_damping = 0.16
recognizer.dynamic_energy_ratio = 1.6
recognizer.pause_threshold = 1.0

# TTS init (pyttsx3)
# =================================================================
try:
    tts_engine = pyttsx3.init()
except Exception as e:
    print(f"\033[33mWARNING: Failed to initialize pyttsx3 TTS engine: {e}. TTS will not work.\033[m")
    tts_engine = None

# speak_handler (no changes needed from local_llm_dog.py)
# =================================================================
speech_loaded = False
speech_lock = threading.Lock()
tts_file_to_play = None

def speak_handler():
    global speech_loaded, tts_file_to_play
    while True:
        with speech_lock:
            _isloaded = speech_loaded
        if _isloaded and tts_file_to_play:
            gray_print('speak start')
            my_dog.speak_block(tts_file_to_play)
            gray_print('speak done')
            try:
                if os.path.exists(tts_file_to_play):
                    os.remove(tts_file_to_play)
            except Exception as e:
                print(f"Warning: Could not delete temp TTS file {tts_file_to_play}: {e}")
            with speech_lock:
                speech_loaded = False
                tts_file_to_play = None
        time.sleep(0.05)

speak_thread = threading.Thread(target=speak_handler)
speak_thread.daemon = True

# actions thread (no changes needed from local_llm_dog.py)
# =================================================================
action_status = 'standby'
actions_to_be_done = []
action_lock = threading.Lock()

def action_handler():
    global action_status, actions_to_be_done
    standby_actions = ['waiting', 'feet_left_right']
    standby_weights = [1, 0.3]
    action_interval = 5
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
            pass
        elif _state == 'actions':
            with action_lock:
                _actions_copy = list(actions_to_be_done)
            for _action in _actions_copy:
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
    global speech_loaded, tts_file_to_play
    global action_status, actions_to_be_done

    if not os.path.exists("./tts"):
        try:
            os.makedirs("./tts")
        except OSError as e:
            print(f"Error creating tts directory: {e}")

    my_dog.rgb_strip.close()
    action_flow.change_status(action_flow.STATUS_SIT)

    speak_thread.start()
    action_thread.start()

    print(f"Pidog Client started. LLM Server URL: {cli_args.server_url}")

    while True:
        user_input_text = ""

        if cli_args.input_mode == 'voice':
            gray_print("listening ...")
            with action_lock:
                action_status = 'standby'
            my_dog.rgb_strip.set_mode('listen', 'cyan', 1)
            _stderr_back = redirect_error_2_null()
            try:
                with sr.Microphone(chunk_size=4096) as source:
                    cancel_redirect_error(_stderr_back)
                    recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    try:
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                    except sr.WaitTimeoutError:
                        gray_print("No speech detected within timeout.")
                        print()
                        continue
            except Exception as e:
                cancel_redirect_error(_stderr_back)
                print(f"Microphone error: {e}")
                time.sleep(1)
                continue
            finally:
                 cancel_redirect_error(_stderr_back)

            my_dog.rgb_strip.set_mode('boom', 'yellow', 0.5)
            stt_start_time = time.time()
            try:
                if cli_args.stt_engine == 'sphinx':
                    gray_print("Performing STT with Sphinx (offline)...")
                    user_input_text = recognizer.recognize_sphinx(audio)
                elif cli_args.stt_engine == 'google':
                    gray_print("Performing STT with Google Web Speech API (online)...")
                    user_input_text = recognizer.recognize_google(audio)
                else:
                    gray_print("Performing STT with Google Web Speech API (online)...")
                    user_input_text = recognizer.recognize_google(audio)
                gray_print(f"STT result: '{user_input_text}' (took {time.time() - stt_start_time:.3f}s)")
            except sr.UnknownValueError:
                gray_print("STT could not understand audio")
                user_input_text = ""
            except sr.RequestError as e:
                gray_print(f"STT error; {e}")
                user_input_text = ""

            if not user_input_text.strip():
                print()
                continue

        elif cli_args.input_mode == 'keyboard':
            with action_lock:
                action_status = 'standby'
            my_dog.rgb_strip.set_mode('listen', 'cyan', 1)
            try:
                user_input_text = input(f'\033[1;30m{"Input: "}\033[0m').encode(sys.stdin.encoding).decode('utf-8')
            except UnicodeDecodeError:
                print("Error decoding input. Please use UTF-8 compatible characters.")
                continue
            if not user_input_text.strip():
                print()
                continue
            my_dog.rgb_strip.set_mode('boom', 'yellow', 0.5)
        else:
            raise ValueError(f"Invalid input mode: {cli_args.input_mode}")

        # LLM Interaction via HTTP Server
        # ----------------------------------------------------------------
        llm_response_data = {}
        request_start_time = time.time()

        with action_lock:
            action_status = 'think'

        gray_print(f"Sending to LLM Server: '{user_input_text}' at {cli_args.server_url}")
        try:
            payload = {"prompt": user_input_text}
            response = requests.post(cli_args.server_url, json=payload, timeout=30) # Added timeout
            response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)
            llm_response_data = response.json()
            gray_print(f"Server request took: {time.time() - request_start_time:.3f}s")
            # gray_print(f"LLM Server raw response data: {llm_response_data}") # Keep for debugging if needed
        except requests.exceptions.Timeout:
            gray_print(f"Error: Request to LLM server timed out.")
            llm_response_data = {"actions": ["stop"], "answer": "Sorry, my brain is a bit slow right now. The request timed out."}
        except requests.exceptions.RequestException as e:
            gray_print(f"Error connecting to LLM server: {e}")
            llm_response_data = {"actions": ["stop"], "answer": "I couldn't connect to my thinking engine. Please check the server."}
        except json.JSONDecodeError:
            gray_print(f"Error: Could not decode JSON response from server.")
            llm_response_data = {"actions": ["stop"], "answer": "I received a strange response from my thinking engine."}


        # Parse LLM server response (same logic as before)
        # ----------------------------------------------------------------
        actions_from_llm = ['stop']
        answer_from_llm = "I didn't understand that."

        try:
            if isinstance(llm_response_data, dict):
                if 'actions' in llm_response_data and isinstance(llm_response_data['actions'], list):
                    actions_from_llm = llm_response_data['actions']
                else:
                    gray_print("LLM Server response missing 'actions' list or not a list.")

                if 'answer' in llm_response_data and isinstance(llm_response_data['answer'], str):
                    answer_from_llm = llm_response_data['answer']
                else:
                    gray_print("LLM Server response missing 'answer' string or not a string.")

                if answer_from_llm:
                    temp_actions = list(actions_from_llm)
                    for _action in temp_actions:
                        if _action in VOICE_ACTIONS:
                            gray_print(f"Action '{_action}' is a voice action, clearing spoken answer.")
                            answer_from_llm = ""
                            break
            else:
                gray_print("LLM Server response was not a dictionary as expected.")

        except Exception as e:
            print(f"Error parsing LLM server response structure: {e}")

        # Local TTS and Action Execution (same logic as before)
        # ----------------------------------------------------------------
        try:
            tts_success = False
            if answer_from_llm and tts_engine:
                tts_proc_start_time = time.time()
                _time_str = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
                temp_raw_tts_file = f"./tts/{_time_str}_raw.wav"
                try:
                    gray_print(f"Generating TTS for: '{answer_from_llm}'")
                    tts_engine.save_to_file(answer_from_llm, temp_raw_tts_file)
                    tts_engine.runAndWait()
                    if os.path.exists(temp_raw_tts_file) and os.path.getsize(temp_raw_tts_file) > 0:
                        temp_final_tts_file = f"./tts/{_time_str}_{VOLUME_DB}dB.wav"
                        if sox_volume(temp_raw_tts_file, temp_final_tts_file, VOLUME_DB):
                            tts_file_to_play = temp_final_tts_file
                            tts_success = True
                            if os.path.exists(temp_raw_tts_file) and temp_raw_tts_file != temp_final_tts_file:
                                os.remove(temp_raw_tts_file)
                        else:
                            gray_print("Sox volume adjustment failed, using raw TTS file.")
                            tts_file_to_play = temp_raw_tts_file
                            tts_success = True
                    else:
                        gray_print("TTS engine failed to generate a valid audio file.")
                        if os.path.exists(temp_raw_tts_file):
                            os.remove(temp_raw_tts_file)
                except Exception as e:
                    print(f"TTS generation error: {e}")
                    if os.path.exists(temp_raw_tts_file):
                         os.remove(temp_raw_tts_file)
                gray_print(f'TTS processing took: {time.time() - tts_proc_start_time:.3f}s')
                if tts_success:
                    with speech_lock:
                        speech_loaded = True
                    my_dog.rgb_strip.set_mode('speak', 'pink', 1)
                else:
                    my_dog.rgb_strip.set_mode('breath', 'blue', 1)
            else:
                if not answer_from_llm:
                    gray_print("No answer from LLM Server to speak.")
                elif not tts_engine:
                    gray_print("TTS engine not available.")
                my_dog.rgb_strip.set_mode('breath', 'blue', 1)

            with action_lock:
                actions_to_be_done = list(actions_from_llm)
                gray_print(f'Actions to be done: {actions_to_be_done}')
                action_status = 'actions'

            if tts_success:
                while True:
                    with speech_lock:
                        if not speech_loaded:
                            break
                    time.sleep(.01)

            while True:
                with action_lock:
                    if action_status != 'actions':
                        break
                time.sleep(.01)

            my_dog.rgb_strip.set_mode('breath', 'blue', 1)
            print()

        except Exception as e:
            print(f'Error during TTS or action execution: {e}')
            my_dog.rgb_strip.set_mode('error', 'red', 1)
            time.sleep(2)
            my_dog.rgb_strip.set_mode('breath', 'blue', 1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"\033[31mFATAL ERROR in main: {e}\033[m")
    finally:
        if 'my_dog' in locals() and my_dog is not None:
            print("Closing PiDog connection...")
            my_dog.close()
        print("Program terminated.")
