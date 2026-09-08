from pidog.tts import Pico2Wave

tts = Pico2Wave()

tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

# Quick hello (sanity check)
tts.say("Hello! I'm Pico2Wave TTS.")