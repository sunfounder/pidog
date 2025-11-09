# 9_rgb_control

**File:** `basic_examples/9_rgb_control.py`

## Module Description

rgb strip style control

API:
    Pidog.rgb_strip.set_mode(style='breath', color='white', bps=1, brightness=1):

        Set the display mode of the rgb light strip

        - style  str, display style, could be: "breath", "boom", "bark", "speak", "listen"
        - color  str, list or hex, display color,
                  could be: 16-bit rgb value, eg: #a10a0a;
                  or 1*3 list of rgb, eg: [255, 100, 80];
                  or predefined colors:"white", "black", "red", "yellow", "green", "blue", "cyan", "magenta", "pink"
        - bps    float or int, beats per second, this number of style actions executed per second

    Pidog.rgb_strip.close():
        - turn off rgb display


more to see: ../pidog/rgb_strip.py

