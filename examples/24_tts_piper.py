### the model files are downloaded to folder /home/pds/.piper_models

from pidog.tts import Piper

tts = Piper()

# List supported languages
print("Supported languages:")
print(tts.available_countrys())

# List models for English (en_us)
print(tts.available_models('en_us'))

# Set a voice model (auto-download if not already present)
tts.set_model("en_US-amy-low")

# Say something
tts.say("Hello! I'm Piper TTS.")


# List models for English (nl_BE)
print("Available models for nl_BE:")
print(tts.available_models('nl_BE'))

# Set a voice model (auto-download if not already present)
tts.set_model("nl_BE-nathalie-medium")

# Say something
tts.say("Hallo! Ik ben Piper TTS.")