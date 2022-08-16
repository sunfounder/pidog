#!/usr/bin/env python3
from pidog import Pidog
from time import sleep
from preset_actions import howling

my_dog = Pidog()

sleep(0.5) 

def main():
    while True:
        howling(my_dog)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        my_dog.close()
    