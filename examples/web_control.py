from flask import Flask, render_template, Response
from flask import request
from pidog import Pidog
from preset_actions import *
from vilib.vilib import gen as vilib_gen, Vilib

app = Flask(__name__)

my_dog = Pidog()

head_yrp = [0, 0, 0]
head_angle = 20
head_speed = 80

Vilib.camera_start(vflip=False, hflip=False)
# Vilib.display(local=True, web=True)
# Vilib.human_detect_switch(True)

@app.route("/")
def hello_world():
    return render_template("web_control.html")

def set_head(roll=None, pitch=None, yaw=None):
    global head_yrp
    if roll is not None:
        head_yrp[1] = roll
    if pitch is not None:
        head_yrp[2] = pitch
    if yaw is not None:
        head_yrp[0] = yaw
    my_dog.head_move([head_yrp], immediately=True, speed=head_speed)

@app.route('/mjpg')   ## video
def video_feed():
    # from camera import Camera
    """Video streaming route. Put this in the src attribute of an img tag."""
    response = Response(vilib_gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame') 
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/command", methods=["POST"])
def command():
    if request.method != 'POST':
        return "Error"
    command = request.json['command']
    print(command)

    if command == "trot":
        set_head(pitch=0)
        my_dog.do_action('trot', wait=True, speed=98)
    elif command == "forward":
        set_head(pitch=0)
        my_dog.do_action('forward', wait=True, speed=98)
    elif command == "backward":
        set_head(pitch=0)
        my_dog.do_action('backward', wait=True, speed=98)
    elif command == "turn_left":
        set_head(pitch=0)
        my_dog.do_action('turn_left', wait=True, speed=98)
    elif command == "turn_right":
        set_head(pitch=0)
        my_dog.do_action('turn_right', wait=True, speed=98)
    elif command == "lie":
        set_head(pitch=0)
        my_dog.do_action('lie', wait=True, speed=70)
    elif command == "stand":
        set_head(pitch=0)
        my_dog.do_action('stand', wait=True, speed=70)
    elif command == "sit":
        set_head(pitch=-40)
        my_dog.do_action('sit', wait=True, speed=70)
    elif command == "bark":
        my_dog.speak('single_bark_1')
        bark(my_dog, head_yrp)
    elif command == "bark2":
        bark_action(my_dog, head_yrp)
    elif command == "pant":
        pant(my_dog, head_yrp)
    elif command == "wag_tail":
        my_dog.do_action('wag_tail', wait=True, speed=100)
    elif command == "shake_head":
        shake_head(my_dog)
    elif command == "stretch":
        my_dog.do_action('stretch', wait=True, speed=80)
    elif command == "doze_off":
        set_head(pitch=-30)
        my_dog.do_action('doze_off', wait=True, speed=95)
    elif command == "pushup":
        pushup(my_dog)
    elif command == "howling":
        howling(my_dog)
    elif command == "body_twisting":
        body_twisting(my_dog)
    # Head Pitch
    elif command == "head_pitch_up":
        set_head(pitch=head_angle)
    elif command == "head_pitch_up2":
        set_head(pitch=head_angle*2)
    elif command == "head_pitch_down":
        set_head(pitch=-head_angle)
    elif command == "head_pitch_down2":
        set_head(pitch=-head_angle*2)
    # Head Yaw
    elif command == "head_yaw_left":
        set_head(yaw=head_angle)
    elif command == "head_yaw_left2":
        set_head(yaw=head_angle*2)
    elif command == "head_yaw_right":
        set_head(yaw=-head_angle)
    elif command == "head_yaw_right2":
        set_head(yaw=-head_angle*2)
    # Head Roll
    elif command == "head_roll_left":
        set_head(roll=head_angle)
    elif command == "head_roll_left2":
        set_head(roll=head_angle*2)
    elif command == "head_roll_right":
        set_head(roll=-head_angle)
    elif command == "head_roll_right2":
        set_head(roll=-head_angle*2)
    # Head Reset
    elif command == "head_reset":
        set_head(roll=0, pitch=0, yaw=0)
    return "OK"

# try:
app.run(host='0.0.0.0', port=9001, debug=False)
# finally:
#     my_dog.close()