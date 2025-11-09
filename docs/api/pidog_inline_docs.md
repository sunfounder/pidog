# Inline Documentation: pidog/pidog.py

This file contains significant inline documentation and comments extracted from `pidog/pidog.py`.

## Line 17

```
''' servos order
                     4,
                   5, '6'
                     |
              3,2 --[ ]-- 7,8
                    [ ]
              1,0 --[ ]-- 10,11
                     |
                    '9'
                    /

    legs pins: [2, 3, 7, 8, 0, 1, 10, 11]
        left front leg, left front leg
        right front leg, right front leg
        left hind leg, left hind leg,
        right hind leg, right hind leg,

    head pins: [4, 6, 5]
        yaw, roll, pitch

    tail pin: [9] 

'''
```

## Line 100

```
    # Servo Speed
    # HEAD_DPS = 300
    # LEGS_DPS = 350
    # TAIL_DPS = 500
```

## Line 620

```
        """
        speak, play audio

        :param name: the file name int the folder(SOUND_DIR)
        :type name: str
        :param volume: volume, 0-100
        :type volume: int
        """
```

## Line 644

```
        """
        speak, play audio with block

        :param name: the file name int the folder(SOUND_DIR)
        :type name: str
        :param volume: volume, 0-100
        :type volume: int
        """
```

