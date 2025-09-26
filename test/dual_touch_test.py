from pidog.dual_touch import DualTouch, TouchStyle
from time import sleep

touch = DualTouch('D2', 'D3')

while True:
    left_val = touch.touch_L.value()
    right_val = touch.touch_R.value()
    style = TouchStyle(touch.read()).name
    print(f"\r\033[KLeft value: {left_val} | Right value: {right_val} | {style}", end="", flush=True)
    sleep(0.05)
