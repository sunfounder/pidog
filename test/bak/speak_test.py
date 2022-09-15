
from robot_hat import Music

music = Music()

SOUND_DIR = "/home/pi/pidog/sounds/"
music.sound_play_threading(SOUND_DIR+"pant.mp3")
