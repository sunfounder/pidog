# !/usr/bin/env python3
''' camera easy use
    Use the image processing library [vilb] to easily implement functions such as：
web-cam, color detection, face detection, take photos and so on.

github: https://github.com/sunfounder/vilib.git

more examples to see: ~/vilib/examples/

'''

from vilib import Vilib
import time

# Most of the functions in the vilib library are [@staticmethod],
# you can use them directly without instantiating the Vilib class

try:
    # start camera
    Vilib.camera_start(vflip=False,hflip=False) # vflip: image vertical flip, hflip:horizontal flip
    # display camera screen
    Vilib.display(local=True,web=True) # local: desktop window display, web: webcam display
    # enable face detection
    Vilib.face_detect_switch(True)
    # wait for vilib launch
    time.sleep(1)
    print('')

    while True:
        n = Vilib.detect_obj_parameter['human_n']
        print(f"\r \033[032m{n:^3}\033[m faces are found.", end='', flush=True)
        time.sleep(1)
        print("\r \033[032m   \033[m faces are found.", end='', flush=True)
        time.sleep(0.1)


except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"\033[31mERROR: {e}\033[m")
finally:
    print("")
    Vilib.camera_close()
