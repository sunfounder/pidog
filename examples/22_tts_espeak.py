from pidog.tts import Espeak

tts = Espeak()

# Optional voice tuning
tts.set_amp(200)   # 0 to 200 volume
tts.set_speed(150) # 80 to 260
tts.set_gap(5)     # 0 to 200 time between words
tts.set_pitch(55)  # 0 to 99 low or high voice

# Quick hello (sanity check)
tts.say("Hello! I'm Espeak TTS.")