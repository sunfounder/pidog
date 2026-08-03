### the model files are downloaded to folder /home/pds/.vosk_models

from pidog.stt import Vosk

vosk = Vosk(language="en-us")
# vosk = Vosk(language="nl")

print(vosk.available_languages)

while True:
    print("Say something")
    result = vosk.listen(stream=False)
    print(result)