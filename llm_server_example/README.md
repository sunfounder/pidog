# Pidog LLM Server Example

This directory contains a Flask-based server application designed to run a Large Language Model (LLM) locally on a host machine (e.g., a laptop). The Pidog client application (running on the Raspberry Pi) can then send prompts to this server to offload the computationally intensive LLM processing.

## Server (`app.py`)

### Features

*   Runs a GGUF-quantized LLM using `llama-cpp-python`.
*   Exposes an API endpoint (`/process_command`) for receiving prompts and returning structured JSON responses (actions and answer).
*   Configurable via command-line arguments for model path, network settings, and LLM parameters.

### Setup and Installation (Server-Side)

1.  **Prerequisites:**
    *   Python 3.8+
    *   C++ Compiler (for `llama-cpp-python` compilation)

2.  **Virtual Environment (Recommended):**
    ```bash
    python -m venv venv_server
    source venv_server/bin/activate  # Linux/macOS
    # venv_server\Scripts\activate    # Windows
    ```

3.  **Install Dependencies:**
    ```bash
    pip install Flask llama-cpp-python
    ```
    For GPU support with `llama-cpp-python`, consult its documentation for platform-specific compilation flags.

4.  **Download a GGUF LLM Model:**
    *   E.g., TinyLlama 1.1B Chat: `tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf` from [TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF).
    *   Create a `models` subdirectory inside `llm_server_example` (i.e., `llm_server_example/models/`) and place the `.gguf` file there. Or, use any path and specify it with `--model_path`.

### Running the Server

```bash
python app.py --model_path ./models/your_model_name.gguf [OTHER_OPTIONS]
```

**Server Command-Line Arguments (`app.py`):**

*   `--model_path` (str, **required**): Path to the GGUF LLM model file.
*   `--host` (str, default: `0.0.0.0`): Host to bind the server to. Use `0.0.0.0` to make it accessible on your local network.
*   `--port` (int, default: `5000`): Port for the server.
*   `--n_ctx` (int, default: `2048`): LLM context size.
*   `--n_gpu_layers` (int, default: `0`): Number of LLM layers to offload to GPU (CPU-only if 0).
*   `--n_threads` (int, default: `4`): Number of CPU threads for LLM inference.

**Example:**
```bash
python app.py --model_path ./models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf --port 5001
```

If running on Windows, you might need to configure Windows Firewall to allow incoming connections on the chosen port if accessing from the Raspberry Pi.

### Server API Endpoint

*   **URL:** `/process_command`
*   **Method:** `POST`
*   **Request Body (JSON):** `{"prompt": "User's command for Pidog"}`
*   **Success Response (JSON):** `{"actions": ["action1"], "answer": "Pidog's spoken response"}`
*   **Error Response (JSON):** `{"error": "Details"}` or `{"actions": ["stop"], "answer": "Error message"}`

---
```
