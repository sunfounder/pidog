### the model files are downloaded to folder /home/pds/.vosk_models

from pidog.stt import Vosk

vosk = Vosk(language="en-us")

while True:
    print("Say something")
    for result in vosk.listen(stream=True):
        if result["done"]:
            print(f"final:   {result['final']}")
        else:
            print(f"partial: {result['partial']}", end="\r", flush=True)