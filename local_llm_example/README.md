## Pidog Local LLM Example Usage

This example demonstrates how to control your Pidog using a lightweight Large Language Model (LLM) running directly on the Raspberry Pi. It utilizes local Speech-to-Text (STT) and Text-to-Speech (TTS) capabilities for a more self-contained experience.

----------------------------------------------------------------

### 1. Install Dependencies

*   **Pidog Software:** Ensure you have installed Pidog and its related dependencies first. Follow the official guide:
    [Pidog Python Installation](https://docs.sunfounder.com/projects/pidog/en/latest/python/python_start/install_all_modules.html)

*   **LLM, STT, TTS, and Audio Libraries:**
    You'll need `llama-cpp-python` for the local LLM, `SpeechRecognition` for STT, `pyttsx3` for TTS, and some system audio libraries.

    ```bash
    # Ensure pip is up to date
    sudo pip3 install -U pip --break-system-packages

    # Install Python libraries
    sudo pip3 install -U llama-cpp-python --break-system-packages
    sudo pip3 install -U SpeechRecognition --break-system-packages
    sudo pip3 install -U pyttsx3 --break-system-packages
    sudo pip3 install -U sox --break-system-packages # For volume adjustment

    # Install system audio packages
    sudo apt update
    sudo apt install -y python3-pyaudio sox

    # For offline STT with CMU Sphinx (PocketSphinx):
    sudo apt install -y pocketsphinx python3-pocketsphinx # For Sphinx STT
    # Note: If python3-pocketsphinx installation via apt fails or is outdated,
    # you might need to build it from source or install via pip:
    # sudo pip3 install -U pocketsphinx --break-system-packages

    # For local TTS (pyttsx3 relies on these)
    sudo apt install -y espeak # Common TTS engine on Linux
    ```
    > **Note:** When using `pip install` outside of a virtual environment on Raspberry Pi OS, you may need to use the `--break-system-packages` option. It's generally recommended to use virtual environments for Python projects.

----------------------------------------------------------------

### 2. Download a Local LLM Model

This example is configured to use a GGUF-quantized model. We recommend **TinyLlama-1.1B-Chat v1.0 (Q4_K_M quantization)** for good performance on Raspberry Pi 4.

*   **Download the model:**
    You can download it from Hugging Face:
    [TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)
    Look for the file `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf`.

*   **Place the model:**
    Create a directory named `models` inside the `local_llm_example` directory and place the downloaded `.gguf` file there.
    The default expected path is: `local_llm_example/models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf`
    You can use a different path/model by specifying the `--model_path` argument when running the script.

    ```bash
    cd local_llm_example
    mkdir models
    # Download or move your GGUF model file into the 'models' directory
    # e.g., wget https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf -P ./models/
    ```

----------------------------------------------------------------

### 3. Running the Example

Navigate to the `local_llm_example` directory and run the `local_llm_dog.py` script.

```bash
cd local_llm_example
sudo python3 local_llm_dog.py [OPTIONS]
```

**Command-line Options:**

*   `--input_mode`: How you want to interact with Pidog.
    *   `voice` (default): Use your microphone to speak commands.
    *   `keyboard`: Type commands into the console.
*   `--model_path`: Path to your GGUF LLM file.
    *   Default: `./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf`
*   `--n_threads`: Number of CPU threads for the LLM.
    *   Default: `4`. Adjust based on your Raspberry Pi's cores (e.g., a Pi 4 has 4 cores).
*   `--n_ctx`: Context size (max sequence length) for the LLM.
    *   Default: `2048`.
*   `--n_gpu_layers`: Number of model layers to offload to GPU.
    *   Default: `0` (CPU only). Raspberry Pi typically doesn't have a compatible GPU for LLM layer offloading.
*   `--stt_engine`: Speech-to-Text engine to use.
    *   `sphinx` (default): Uses CMU PocketSphinx for offline STT. Requires `pocketsphinx` to be installed.
    *   `google`: Uses Google Web Speech API (requires internet connection). This is a fallback if Sphinx has issues or is not preferred.

**Example Scenarios:**

*   **Run with voice input using default settings (offline STT):**
    ```bash
    sudo python3 local_llm_dog.py
    ```
*   **Run with keyboard input:**
    ```bash
    sudo python3 local_llm_dog.py --input_mode keyboard
    ```
*   **Run with voice input using Google STT (online):**
    ```bash
    sudo python3 local_llm_dog.py --stt_engine google
    ```
*   **Run with a different model path:**
    ```bash
    sudo python3 local_llm_dog.py --model_path /path/to/your/other_model.gguf
    ```

----------------------------------------------------------------

### How it Works

1.  **Input:** The script takes your command via voice (processed by STT) or keyboard.
2.  **LLM Processing:** The text command is sent to the local LLM (e.g., TinyLlama). The LLM is prompted to return a JSON object containing:
    *   `"actions"`: A list of actions for Pidog (e.g., `["forward"]`, `["wag tail"]`).
    *   `"answer"`: A text phrase for Pidog to "speak".
3.  **Action Execution:** The `action_flow.py` script translates these actions into Pidog movements.
4.  **TTS Output:** The `answer` text is converted to speech using a local TTS engine (`pyttsx3` with `espeak` or similar) and played through the Pidog's speaker (or system speakers).

----------------------------------------------------------------

### Important Notes:

*   **LLM Performance:** Running LLMs on a Raspberry Pi 4 can be slow, especially for larger models or complex prompts. Response times might take several seconds. The chosen TinyLlama Q4_K_M model is a compromise between size and capability.
*   **STT Accuracy:**
    *   Offline STT with **Sphinx** can be less accurate than online services, especially in noisy environments or with varied accents. Ensure you have a decent microphone.
    *   **Google STT** is generally more accurate but requires an internet connection.
*   **TTS Quality:** Local TTS (e.g., via `espeak`) might sound robotic.
*   **Permissions:** The script usually requires `sudo` to access hardware components of the Pidog.
*   **First Run:** The first time you run the LLM, it might take longer to load the model into memory.
*   **`keys.py`:** This file is no longer used for API keys in this local example but is kept for structural consistency if you wish to adapt parts from the original `gpt_examples`. You can safely ignore or remove it for this local LLM setup.

----------------------------------------------------------------

### Customization (Optional)

*   **LLM Prompting:** You can modify the system prompt in `local_llm_helper.py` (`system_message` variable) to change how the LLM behaves or to fine-tune its responses and JSON output format.
*   **TTS Voice/Properties:** `pyttsx3` allows some customization of voice, rate, and volume. You can explore its documentation and modify the `tts_engine` initialization in `local_llm_dog.py`.
*   **Available Actions:** The list of recognized actions is defined in the system prompt within `local_llm_helper.py` and corresponds to functions in `action_flow.py` and `preset_actions.py`.
*   **Volume Gain:** The `VOLUME_DB` variable in `local_llm_dog.py` controls the gain applied by `sox` to the TTS output file.
