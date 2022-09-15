from pidog.dual_touch import DualTouch
from time import sleep

touch = DualTouch('D2', 'D3')

while True:
    print(
        f"\rLeft value: {touch.touch_1.value()} | Right value: {touch.touch_2.value()} | Slide direction: {touch.is_slide()}", end="          ", flush=True)
    sleep(0.05)
