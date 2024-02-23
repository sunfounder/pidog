from pidog.dual_touch import DualTouch
from time import sleep

touch = DualTouch('D2', 'D3')

while True:
    print(
        f"\rLeft value: {touch.touch_L.value()} | Right value: {touch.touch_R.value()} | {touch.read()}", end="          ", flush=True)
    sleep(0.05)
