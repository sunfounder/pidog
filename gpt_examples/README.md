## Pidog GPT examples usage

----------------------------------------------------------------

## Install dependencies

- Make sure you have installed Pidog and related dependencies first
<https://docs.sunfounder.com/projects/pidog/en/latest/python/python_start/install_all_modules.html>

- Install openai and speech processing libraries

    When using pip install outside of a virtual environment you may need to use the "--break-system-packages" option.

    ```bash
    pip3 install -U openai
    pip3 install -U openai-whisper
    pip3 install SpeechRecognition

    sudo apt install pyaudio
    ```

----------------------------------------------------------------

## Create your own GPT assistant

### GET API KEY

<https://platform.openai.com/api-keys>

Fill your OPENAI_API_KEY into the `keys.py` file.

![tutorial_1](./tutorial_1.png)

### Create assistant and set Assistant ID

<https://platform.openai.com/assistants>

Fill your ASSISTANT_ID into the `keys.py` file.

![tutorial_2](./tutorial_2.png)

- Set Assistant Name

- Describe your Assistant

    You can modify the description to create your own style of Assistant. Remember to keep the Answer format.

    ``` text
    You are a intelligent  robot dog, your name is Pidog. You are lively, positive.
    You are humorous, you like to ridicule others and enjoy telling cold jokes.
    You know you are an intelligent robot dog.
    You have AI interaction capabilities. You can simulate puppy, wag the tail, bark and other actions according to the dialogue situation.

    Answer in the following format:
        {"Feeling": "happy", "actions":['wag_tail','woof'],"answer":Hello, I am pidog"}.

    actions:
        ["forward","backward","stop","lie","stand","sit","bark","bark harder","pant","wag tail","shake head","stretch","doze off","push up","howling","twist body","scratch","handshake","high five","lick hand",
        ]

    if ["howling", "bark", "bark harder",], then answer no words

    Stretch and sit, when I wake you up.
    ```

- Select gpt model

    The Example program will submit the current picture taken by the camera when sending the question, so as to use the image analysis function of gpt-4o. Of course, you can also choose gpt3.5-turbo or other models

----------------------------------------------------------------

## Set Key for example

Confirm that `keys.py` is configured correctly

## Run

```bash
sudo python3 gpt_dog.py
```
