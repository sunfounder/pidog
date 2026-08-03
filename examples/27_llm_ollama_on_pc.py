### since my Raspberry Pi has only 4 GB of RAM I decided to run Ollama on my PC
### On the settings page of Ollama activate the option 'Expose Ollame to the network

from pidog.llm import Ollama

INSTRUCTIONS = "You are a helpful assistant."
WELCOME = "Hello, I am a helpful assistant. How can I help you?"

# If Ollama runs on the same Raspberry Pi, use "localhost".
# llm = Ollama(
#     ip="localhost",
#     model="llama3.2:3b"   # you can replace with any model
# )

# If it runs on another computer in your LAN, replace with that computer's IP address.
llm = Ollama(
    ip="192.168.0.163",
    model="llama3.2"   # you can replace with any model
)

# Basic configuration
llm.set_max_messages(20)
llm.set_instructions(INSTRUCTIONS)
llm.set_welcome(WELCOME)

print(WELCOME)

while True:
    text = input(">>> ")
    if text.strip().lower() in {"exit", "quit"}:
        break

    # Response with streaming output
    response = llm.prompt(text, stream=True)
    for token in response:
        if token:
            print(token, end="", flush=True)
    print("")
