
from pidog import Pidog
dog = Pidog(feet_pins=[1, 2, 3, 4, 5, 6, 7, 8],
    head_pins=[9, 10, 11], tail_pin=[12],
)

pushup = [
        [90, -30, -90, 30, 80, 70, -80, -70],
        [45, 35, -45, -35, 80, 70, -80, -70]
    ]

import readchar

def pause():
    key = readchar.readkey()
    if key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
        import sys
        print('')
        sys.exit(0)

try:
    while True:
        for angles in pushup:
            print(angles)
            dog.feet.servo_move2(angles, speed=80)
            pause()
finally:
    dog.close()