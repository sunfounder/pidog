from pidog.tts import EdgeTTS

tts = EdgeTTS(voice="en-US-AriaNeural")
msg = "Hi, I'm Edge TTS. A free cloud text-to-speech service powered by Microsoft Edge."
tts.say(msg)
