from local_llm_helper import LocalLLMHelper # Changed
from action_flow import ActionFlow
from utils import *

import readline # optimize keyboard input, only need to import

import speech_recognition as sr
import pyttsx3 # Added for local TTS
from pidog import Pidog

import time
import threading
import random
import argparse # Added for command line arguments

import os
import sys

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

# --- Configuration ---
MODEL_PATH_DEFAULT = "./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf" # Default model path
N_THREADS_DEFAULT = 4 # Default number of threads for LLM
N_CTX_DEFAULT = 2048 # Default context size for LLM
N_GPU_LAYERS_DEFAULT = 0 # Default GPU layers (0 for CPU only)

# VOLUME_DB = 5
VOLUME_DB = 3 # Volume gain for TTS output using sox

VOICE_ACTIONS = ["bark", "bark harder", "pant",  "howling"] # Actions that shouldn't have spoken response

# --- Argument Parsing ---
parser = argparse.ArgumentParser(description="Control PiDog with a local LLM.")
parser.add_argument(
    '--input_mode',
    type=str,
    default='voice',
    choices=['voice', 'keyboard'],
    help='Input mode: "voice" or "keyboard" (default: voice)'
)
parser.add_argument(
    '--model_path',
    type=str,
    default=MODEL_PATH_DEFAULT,
    help=f'Path to the GGUF model file (default: {MODEL_PATH_DEFAULT})'
)
parser.add_argument(
    '--n_threads',
    type=int,
    default=N_THREADS_DEFAULT,
    help=f'Number of CPU threads for LLM (default: {N_THREADS_DEFAULT})'
)
parser.add_argument(
    '--n_ctx',
    type=int,
    default=N_CTX_DEFAULT,
    help=f'Context size for LLM (default: {N_CTX_DEFAULT})'
)
parser.add_argument(
    '--n_gpu_layers',
    type=int,
    default=N_GPU_LAYERS_DEFAULT,
    help=f'Number of layers to offload to GPU (default: {N_GPU_LAYERS_DEFAULT}, 0 for CPU only)'
)
parser.add_argument(
    '--stt_engine',
    type=str,
    default='sphinx', # Changed default to sphinx
    choices=['sphinx', 'google'], # Added choice for STT
    help='STT engine: "sphinx" (offline) or "google" (online, default by speech_recognition if sphinx fails or not chosen)'
)


cli_args = parser.parse_args()

# Local LLM init
# =================================================================
if not os.path.exists(cli_args.model_path):
    print(f"\033[31mERROR: Model file not found at {cli_args.model_path}\033[m")
    print("Please download a GGUF model (e.g., TinyLlama-1.1B-Chat Q4_K_M)")
    print("and place it in the specified path or provide the correct path using --model_path.")
    sys.exit(1)

try:
    llm_helper = LocalLLMHelper(
        model_path=cli_args.model_path,
        n_ctx=cli_args.n_ctx,
        n_threads=cli_args.n_threads,
        n_gpu_layers=cli_args.n_gpu_layers
    )
except Exception as e:
    print(f"\033[31mERROR: Failed to load local LLM: {e}\033[m")
    sys.exit(1)


# dog init
# =================================================================
try:
    my_dog = Pidog()
    time.sleep(1)
except Exception as e:
    print(f"\033[31mERROR: Failed to initialize PiDog: {e}\033[m") # Added error print
    # Allow running without physical pidog for testing LLM part if needed
    # For now, we exit if PiDog fails.
    # raise RuntimeError(e)
    sys.exit(1)


action_flow = ActionFlow(my_dog)

# speech_recognition init
# =================================================================
recognizer = sr.Recognizer()
recognizer.dynamic_energy_adjustment_damping = 0.16 # Keep existing settings
recognizer.dynamic_energy_ratio = 1.6
recognizer.pause_threshold = 1.0
# Note: For Sphinx, ensure pocketsphinx is installed: sudo apt-get install pocketsphinx python3-pocketsphinx

# TTS init (pyttsx3)
# =================================================================
try:
    tts_engine = pyttsx3.init()
    # Optional: Set properties like rate, volume
    # tts_engine.setProperty('rate', 150)    # Speed percent (can go over 100)
    # tts_engine.setProperty('volume', 0.9)  # Volume 0-1
except Exception as e:
    print(f"\033[33mWARNING: Failed to initialize pyttsx3 TTS engine: {e}. TTS will not work.\033[m")
    tts_engine = None

# speak_hanlder
# =================================================================
speech_loaded = False
speech_lock = threading.Lock()
tts_file_to_play = None # Renamed from tts_file to avoid confusion

def speak_handler(): # Renamed from speak_hanlder
    global speech_loaded, tts_file_to_play
    while True:
        with speech_lock:
            _isloaded = speech_loaded
        if _isloaded and tts_file_to_play:
            gray_print('speak start')
            my_dog.speak_block(tts_file_to_play) # speak_block expects a file path
            gray_print('speak done')
            # Clean up the temporary TTS file
            try:
                if os.path.exists(tts_file_to_play):
                    os.remove(tts_file_to_play)
            except Exception as e:
                print(f"Warning: Could not delete temp TTS file {tts_file_to_play}: {e}")
            with speech_lock:
                speech_loaded = False
                tts_file_to_play = None
        time.sleep(0.05)

speak_thread = threading.Thread(target=speak_handler) # Corrected target name
speak_thread.daemon = True


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
            # action_flow.run('think') # Can be enabled if a visual "thinking" action is desired
            pass
        elif _state == 'actions':
            with action_lock:
                _actions_copy = list(actions_to_be_done) # Iterate over a copy
            for _action in _actions_copy:
                try:
                    action_flow.run(_action)
                except Exception as e:
                    print(f'action error: {e}')
                time.sleep(0.5) # Small delay between actions

            with action_lock:
                action_status = 'actions_done'
            last_action_time = time.time()

        time.sleep(0.01)

action_thread = threading.Thread(target=action_handler)
action_thread.daemon = True


# main
# =================================================================
def main():
    # global current_feeling, last_feeling # These seem unused, remove if confirmed
    global speech_loaded, tts_file_to_play # Corrected variable name
    global action_status, actions_to_be_done

    # Create tts directory if it doesn't exist
    if not os.path.exists("./tts"):
        try:
            os.makedirs("./tts")
        except OSError as e:
            print(f"Error creating tts directory: {e}")
            # If TTS dir can't be made, local file TTS won't work well.
            # For now, we continue, but pyttsx3 might fail to save.

    my_dog.rgb_strip.close() # Close any existing animations
    action_flow.change_status(action_flow.STATUS_SIT) # Start in sitting position

    speak_thread.start()
    action_thread.start()

    while True:
        user_input_text = "" # Stores text from STT or keyboard

        if cli_args.input_mode == 'voice':
            # listen
            # ----------------------------------------------------------------
            gray_print("listening ...")

            with action_lock: # Ensure dog is in standby during listening
                action_status = 'standby'
            my_dog.rgb_strip.set_mode('listen', 'cyan', 1)

            # Suppress ALSA errors during microphone use
            _stderr_back = redirect_error_2_null()
            try:
                with sr.Microphone(chunk_size=4096) as source: # chunk_size can be tuned
                    cancel_redirect_error(_stderr_back)
                    recognizer.adjust_for_ambient_noise(source, duration=0.5) # Shorter adjustment
                    try:
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10) # Added timeouts
                    except sr.WaitTimeoutError:
                        gray_print("No speech detected within timeout.")
                        print() # new line
                        continue
            except Exception as e:
                cancel_redirect_error(_stderr_back)
                print(f"Microphone error: {e}")
                time.sleep(1) # Avoid busy-looping on mic error
                continue
            finally:
                 cancel_redirect_error(_stderr_back) # Ensure stderr is restored

            # stt
            # ----------------------------------------------------------------
            my_dog.rgb_strip.set_mode('boom', 'yellow', 0.5) # Thinking/processing color

            stt_start_time = time.time()
            try:
                if cli_args.stt_engine == 'sphinx':
                    gray_print("Performing STT with Sphinx (offline)...")
                    user_input_text = recognizer.recognize_sphinx(audio) # No language arg for sphinx here
                elif cli_args.stt_engine == 'google':
                    gray_print("Performing STT with Google Web Speech API (online)...")
                    user_input_text = recognizer.recognize_google(audio) # Uses default API key if available
                else: # Fallback or if not specified, try Google as a default
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
                print() # new line
                continue

        elif cli_args.input_mode == 'keyboard':
            with action_lock:
                action_status = 'standby'
            my_dog.rgb_strip.set_mode('listen', 'cyan', 1) # Indicate ready for input

            try:
                user_input_text = input(f'\033[1;30m{"Input: "}\033[0m').encode(sys.stdin.encoding).decode('utf-8')
            except UnicodeDecodeError:
                print("Error decoding input. Please use UTF-8 compatible characters.")
                continue


            if not user_input_text.strip():
                print() # new line
                continue

            my_dog.rgb_strip.set_mode('boom', 'yellow', 0.5) # Thinking/processing color

        else:
            # This case should not be reached due to argparse choices
            raise ValueError(f"Invalid input mode: {cli_args.input_mode}")

        # Local LLM Interaction
        # ----------------------------------------------------------------
        llm_response_data = {}
        llm_start_time = time.time()

        with action_lock:
            action_status = 'think' # Dog can "think" while LLM processes

        gray_print(f"Sending to LLM: '{user_input_text}'")
        llm_response_data = llm_helper.get_completion(user_input_text)
        gray_print(f"LLM processing took: {time.time() - llm_start_time:.3f}s")
        gray_print(f"LLM raw response data: {llm_response_data}")


        # Parse LLM response for actions and spoken answer
        # ----------------------------------------------------------------
        actions_from_llm = ['stop'] # Default to 'stop' if parsing fails
        answer_from_llm = "I didn't understand that." # Default answer

        try:
            if isinstance(llm_response_data, dict):
                if 'actions' in llm_response_data and isinstance(llm_response_data['actions'], list):
                    actions_from_llm = llm_response_data['actions']
                else:
                    gray_print("LLM response missing 'actions' list or not a list.")

                if 'answer' in llm_response_data and isinstance(llm_response_data['answer'], str):
                    answer_from_llm = llm_response_data['answer']
                else:
                    gray_print("LLM response missing 'answer' string or not a string.")

                # If answer is present, but the primary action is a "voice action", clear the answer.
                if answer_from_llm:
                    temp_actions = list(actions_from_llm) # Operate on a copy
                    for _action in temp_actions:
                        if _action in VOICE_ACTIONS:
                            gray_print(f"Action '{_action}' is a voice action, clearing spoken answer.")
                            answer_from_llm = "" # Clear answer for voice actions like bark
                            break
            else:
                gray_print("LLM response was not a dictionary as expected.")
                # actions_from_llm remains ['stop']
                # answer_from_llm remains "I didn't understand that."

        except Exception as e:
            print(f"Error parsing LLM response structure: {e}")
            # Defaults will be used.

        # Local TTS and Action Execution
        # ----------------------------------------------------------------
        try:
            tts_success = False
            if answer_from_llm and tts_engine:
                tts_proc_start_time = time.time()
                # Create a unique filename for the TTS output
                _time_str = time.strftime("%y-%m-%d_%H-%M-%S", time.localtime())
                temp_raw_tts_file = f"./tts/{_time_str}_raw.wav"

                try:
                    gray_print(f"Generating TTS for: '{answer_from_llm}'")
                    tts_engine.save_to_file(answer_from_llm, temp_raw_tts_file)
                    tts_engine.runAndWait() # Important to ensure file is written

                    if os.path.exists(temp_raw_tts_file) and os.path.getsize(temp_raw_tts_file) > 0:
                        # Apply sox volume adjustment if needed
                        temp_final_tts_file = f"./tts/{_time_str}_{VOLUME_DB}dB.wav"
                        if sox_volume(temp_raw_tts_file, temp_final_tts_file, VOLUME_DB):
                            tts_file_to_play = temp_final_tts_file
                            tts_success = True
                            # Clean up raw file if sox succeeded
                            if os.path.exists(temp_raw_tts_file) and temp_raw_tts_file != temp_final_tts_file:
                                os.remove(temp_raw_tts_file)
                        else: # Sox failed, try to use the raw file
                            gray_print("Sox volume adjustment failed, using raw TTS file.")
                            tts_file_to_play = temp_raw_tts_file # Fallback to raw if sox fails
                            tts_success = True # Still counts as success if raw file exists
                    else:
                        gray_print("TTS engine failed to generate a valid audio file.")
                        if os.path.exists(temp_raw_tts_file): # remove empty file
                            os.remove(temp_raw_tts_file)

                except Exception as e:
                    print(f"TTS generation error: {e}")
                    if os.path.exists(temp_raw_tts_file): # cleanup if error
                         os.remove(temp_raw_tts_file)

                gray_print(f'TTS processing took: {time.time() - tts_proc_start_time:.3f}s')

                if tts_success:
                    with speech_lock:
                        speech_loaded = True # Signal speak_handler thread
                    my_dog.rgb_strip.set_mode('speak', 'pink', 1) # Dog is "speaking"
                else:
                    my_dog.rgb_strip.set_mode('breath', 'blue', 1) # Back to idle if TTS failed
            else:
                if not answer_from_llm:
                    gray_print("No answer from LLM to speak.")
                elif not tts_engine:
                    gray_print("TTS engine not available.")
                my_dog.rgb_strip.set_mode('breath', 'blue', 1) # Idle if no TTS

            # ---- Execute Actions ----
            with action_lock:
                actions_to_be_done = list(actions_from_llm) # Ensure it's a list
                gray_print(f'Actions to be done: {actions_to_be_done}')
                action_status = 'actions' # Signal action_handler thread

            # ---- Wait for speech to complete (if any) ----
            if tts_success:
                while True:
                    with speech_lock:
                        if not speech_loaded:
                            break
                    time.sleep(.01)

            # ---- Wait for actions to complete ----
            while True:
                with action_lock:
                    if action_status != 'actions': # 'actions_done' or 'standby'
                        break
                time.sleep(.01)

            my_dog.rgb_strip.set_mode('breath', 'blue', 1) # Return to idle breathing LED
            print() # New line for cleaner console output

        except Exception as e:
            print(f'Error during TTS or action execution: {e}')
            my_dog.rgb_strip.set_mode('error', 'red', 1) # Error LED
            time.sleep(2) # Show error color for a bit
            my_dog.rgb_strip.set_mode('breath', 'blue', 1) # Back to idle


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
