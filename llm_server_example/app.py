import os
import json
import argparse
from flask import Flask, request, jsonify
from llama_cpp import Llama

# --- Global Variables ---
llm_instance = None
SYSTEM_PROMPT = """You are a helpful assistant that controls a robot dog.
Your goal is to understand user commands and respond with actions for the dog and a spoken phrase.
Respond with a single JSON object containing two keys:
"actions": a list of action strings for the robot dog.
"answer": a short, friendly spoken response for the user.

Available actions are:
["forward", "backward", "lie", "stand", "sit", "bark", "bark harder", "pant", "howling", "wag tail", "stretch", "push up", "scratch", "handshake", "high five", "lick hand", "shake head", "relax neck", "nod", "think", "recall", "head down", "fluster", "surprise", "stop"]

If the action is one of ["bark", "bark harder", "pant", "howling"], then provide no words in the "answer" field (empty string).
If no specific action is requested or appropriate, use ["stop"] for actions.
Be concise.
"""

# --- Flask App Initialization ---
app = Flask(__name__)

def load_llm_model(model_path: str, n_ctx: int, n_gpu_layers: int, n_threads: int):
    """Loads the LLM model using llama-cpp-python."""
    global llm_instance
    if not os.path.exists(model_path):
        print(f"Error: Model file not found at {model_path}")
        raise FileNotFoundError(f"Model file not found at {model_path}")

    try:
        print(f"Loading LLM model from: {model_path}")
        print(f"Parameters: n_ctx={n_ctx}, n_gpu_layers={n_gpu_layers}, n_threads={n_threads}")
        llm_instance = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_gpu_layers=n_gpu_layers,
            n_threads=n_threads,
            verbose=True # Server-side, more verbose can be helpful for debugging
        )
        print("LLM model loaded successfully.")
    except Exception as e:
        print(f"Error loading LLM model: {e}")
        raise

@app.route('/process_command', methods=['POST'])
def process_command():
    global llm_instance
    if not llm_instance:
        return jsonify({"error": "LLM not loaded"}), 500

    try:
        data = request.get_json()
        if not data or 'prompt' not in data:
            return jsonify({"error": "Invalid request: 'prompt' field missing"}), 400

        user_prompt = data['prompt']

        # Construct the full prompt using ChatML format for TinyLlama or similar models
        prompt_template = f"""<|im_start|>system
{SYSTEM_PROMPT}<|im_end|>
<|im_start|>user
{user_prompt}<|im_end|>
<|im_start|>assistant
"""

        print(f"\nReceived prompt: {user_prompt}")
        # print(f"Full prompt to LLM:\n{prompt_template}") # For debugging

        llm_response = llm_instance(
            prompt_template,
            max_tokens=200,  # Max tokens for the response
            stop=["<|im_end|>", "</s>"], # Stop generation tokens
            echo=False,      # Don't echo the prompt in the output
            temperature=0.7,
        )

        # print(f"Raw LLM output: {llm_response}") # For debugging

        if llm_response and 'choices' in llm_response and len(llm_response['choices']) > 0:
            generated_text = llm_response['choices'][0]['text'].strip()
            print(f"Generated text from LLM: {generated_text}")

            json_start_index = generated_text.find('{')
            json_end_index = generated_text.rfind('}')

            if json_start_index != -1 and json_end_index != -1 and json_start_index < json_end_index:
                json_str = generated_text[json_start_index : json_end_index + 1]
                try:
                    parsed_output = json.loads(json_str)
                    if isinstance(parsed_output, dict) and "actions" in parsed_output and "answer" in parsed_output:
                        print(f"Successfully parsed LLM response: {parsed_output}")
                        return jsonify(parsed_output)
                    else:
                        print(f"Error: LLM JSON response missing required keys. Raw JSON: {json_str}")
                        return jsonify({"actions": ["stop"], "answer": "Error: LLM response format error (missing keys)."}), 200 # Return valid structure with error
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON from LLM response: {e}. Raw text: {generated_text}")
                    return jsonify({"actions": ["stop"], "answer": f"Error: LLM response JSON malformed. Content: {generated_text}"}), 200
            else:
                print(f"Error: Could not find JSON object in LLM response. Raw text: {generated_text}")
                return jsonify({"actions": ["stop"], "answer": f"Error: LLM response no JSON found. Content: {generated_text}"}), 200
        else:
            print("Error: LLM response was empty or malformed.")
            return jsonify({"actions": ["stop"], "answer": "Error: LLM returned empty or malformed response."}), 200

    except Exception as e:
        print(f"Error processing request: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LLM Server for Pidog Control")
    parser.add_argument('--model_path', type=str, required=True, help="Path to the GGUF LLM model file.")
    parser.add_argument('--host', type=str, default='0.0.0.0', help="Host to bind the server to (default: 0.0.0.0).")
    parser.add_argument('--port', type=int, default=5000, help="Port to run the server on (default: 5000).")
    parser.add_argument('--n_ctx', type=int, default=2048, help="Context size for the LLM (default: 2048).")
    parser.add_argument('--n_gpu_layers', type=int, default=0, help="Number of layers to offload to GPU (default: 0 for CPU).")
    parser.add_argument('--n_threads', type=int, default=4, help="Number of CPU threads to use for LLM (default: 4).")

    args = parser.parse_args()

    try:
        load_llm_model(args.model_path, args.n_ctx, args.n_gpu_layers, args.n_threads)
        app.run(host=args.host, port=args.port, debug=False) # Debug=False for production, True for dev
    except FileNotFoundError:
        print("Could not start server due to model file not found.")
    except Exception as e:
        print(f"Could not start server: {e}")
