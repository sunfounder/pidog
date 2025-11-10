from .preset_actions import *
import threading
import time
from enum import Enum, StrEnum
import queue

class Posetures(Enum):
    STAND = 0
    SIT = 1
    LIE = 2

class ActionStatus(StrEnum):
    STANDBY = 'standby'
    THINK = 'think'
    ACTIONS = 'actions'
    ACTIONS_DONE = 'actions_done'

class ActionFlow():
    SIT_HEAD_PITCH = -35
    STAND_HEAD_PITCH = 0
    HEAD_SPEED = 80
    HEAD_ANGLE = 20
    CHANGE_STATUS_SPEED = 60

    dog_obj = None
    head_yrp = [0, 0, 0]
    head_pitch_init = 0
    posture = Posetures.STAND
    last_actions = None

    OPERATIONS = {
        "forward": {
            "function": lambda self: self.dog_obj.do_action('forward', speed=98),
            "poseture": Posetures.STAND,
        },
        "backward": {
            "function": lambda self: self.dog_obj.do_action('backward', speed=98),
            "poseture": Posetures.STAND,
        },
        "turn left": {
            "function": lambda self: self.dog_obj.do_action('turn_left', speed=98),
            "poseture": Posetures.STAND,
        },
        "turn right": {
            "function": lambda self: self.dog_obj.do_action('turn_right', speed=98),
            "poseture": Posetures.STAND,
        },
        "stop": {
        },
        "lie": {
            "function": lambda self: self.dog_obj.do_action('lie', speed=70),
            "poseture": Posetures.LIE,
        },
        "stand": {
            "function": lambda self: self.dog_obj.do_action('stand', speed=65),
            "poseture": Posetures.STAND,
        },
        "sit": {
            "function": lambda self: self.dog_obj.do_action('sit', speed=70),
            "poseture": Posetures.SIT,
        },
        "bark": {
            "function": lambda self: bark(self.dog_obj, self.head_yrp, pitch_comp=self.head_pitch_init),
        },
        "bark harder": {
            # "before": "stand",
            "before": lambda self: attack_posture(self.dog_obj),
            "function": lambda self: bark_action(self.dog_obj, self.head_yrp, 'single_bark_1'),
            "poseture": Posetures.STAND,
        },
        "pant": {
            "function": lambda self: pant(self.dog_obj, self.head_yrp, pitch_comp=self.head_pitch_init),
        },
        "wag tail": {
            "function": lambda self: self.dog_obj.do_action('wag_tail', speed=100),
            "after": "wag tail",
        },
        "shake head": {
            "function": lambda self: shake_head(self.dog_obj, [self.head_yrp[0], self.head_yrp[1], self.head_yrp[2]+self.head_pitch_init]),
        },
        "stretch": {
            "function": lambda self: stretch(self.dog_obj),
            "after": "sit",
            "poseture": Posetures.SIT,
        },
        "doze off": {
            "function": lambda self: self.dog_obj.do_action('doze_off', speed=95),
            "after": "doze off",
            "poseture": Posetures.LIE,
        },
        "push up": {
            "function": lambda self:push_up(self.dog_obj),
            "poseture": Posetures.STAND,
        },
        "howling": {
            "function": lambda self:howling(self.dog_obj),
            "after": "sit",
            "poseture": Posetures.SIT,
        },
        "twist body": {
            "function": lambda self:body_twisting(self.dog_obj),
            "after": "sit",
            "poseture": Posetures.STAND,
        },
        "scratch": {
            "function": lambda self:scratch(self.dog_obj),
            "after": "sit",
            "poseture": Posetures.SIT,
        },
        "handshake": {
            "function": lambda self:hand_shake(self.dog_obj),
            "after": "sit",
            "poseture": Posetures.SIT,
        },
        "high five": {
            "function": lambda self:high_five(self.dog_obj),
            "after": "sit",
            "poseture": Posetures.SIT,
        },
        "lick hand": {
            "function": lambda self:lick_hand(self.dog_obj),
            "poseture": Posetures.SIT,
        },
        "waiting": {
            "function": lambda self:waiting(self.dog_obj, pitch_comp=self.head_pitch_init),
        },
        "feet shake": {
            "function": lambda self:feet_shake(self.dog_obj),
            "poseture": Posetures.SIT,
        },
        "relax neck": {
            "function": lambda self:relax_neck(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
        "nod": {
            "function": lambda self:nod(self.dog_obj, pitch_comp=self.head_pitch_init),
            "head_pitch": SIT_HEAD_PITCH,
            "poseture": Posetures.SIT,
        },
        "think": {
            "function": lambda self:think(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
        "recall": {
            "function": lambda self:recall(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
        "fluster": {
            "function": lambda self:fluster(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
        "surprise": {
            "function": lambda self:surprise(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
    }

    def __init__(self, dog_obj):

        self.dog_obj = dog_obj

        self.head_yrp = [0, 0, 0]
        self.head_pitch_init = 0
        self.posture = Posetures.LIE

        self.thread = None
        self.thread_running = False
        self.thread_action_state = 'standby'
        self.action_queue = queue.Queue()

    def set_head_pitch_init(self, pitch):
        self.head_pitch_init = pitch
        self.dog_obj.head_move([self.head_yrp], pitch_comp=pitch,
                        immediately=True, speed=self.HEAD_SPEED)
                     
    def change_poseture(self, poseture):
        if poseture == Posetures.STAND:
            self.set_head_pitch_init(self.STAND_HEAD_PITCH)
            if self.posture != Posetures.STAND:
                sit_2_stand(self.dog_obj, speed=75) # speed > 70
            else:
               self.dog_obj.do_action('stand', speed=self.CHANGE_STATUS_SPEED) 
        elif poseture == Posetures.SIT:
            self.set_head_pitch_init(self.SIT_HEAD_PITCH)
            self.dog_obj.do_action('sit', speed=self.CHANGE_STATUS_SPEED)
        elif poseture == Posetures.LIE:
            self.set_head_pitch_init(self.STAND_HEAD_PITCH)
            self.dog_obj.do_action('lie', speed=self.CHANGE_STATUS_SPEED)
        
        self.posture = poseture
        self.dog_obj.wait_all_done()


    def run(self, action):
        try:
            # print(f'run: {action}')
            if action in self.OPERATIONS:
                operation = self.OPERATIONS[action]
                # poseture
                if "poseture" in operation and operation["poseture"] != None:
                    # if self.posture != operation["poseture"]:
                    if self.last_actions != action:
                        self.last_actions = action 
                        self.change_poseture(operation["poseture"])
                # before
                if "before" in operation and operation["before"] != None:
                    before = operation["before"]
                    if before in self.OPERATIONS and self.OPERATIONS[before]["function"] != None:
                        self.OPERATIONS[before]["function"](self) # run before function
                        self.dog_obj.wait_all_done()
                    else:
                        before(self)
                        self.dog_obj.wait_all_done()
                # function
                if "function" in operation and operation["function"] != None:
                    operation["function"](self) # run function function
                    self.dog_obj.wait_all_done()
                # after
                if "after" in operation and operation["after"] != None:
                    after = operation["after"]
                    if after in self.OPERATIONS and self.OPERATIONS[after]["function"] != None:
                        self.OPERATIONS[after]["function"](self) # run after function
                        self.dog_obj.wait_all_done()
                    else:
                        after(self)
                        self.dog_obj.wait_all_done()
        except Exception as e:
            print(f'action error: {e}')
    
    def action_handler(self):
        standby_actions = ['waiting', 'feet_left_right']
        standby_weights = [1, 0.3]

        action_interval = 5 # seconds
        last_action_time = time.time()

        while self.thread_running:
            if self.thread_action_state == ActionStatus.STANDBY:
                if time.time() - last_action_time > action_interval:
                    choice = random.choices(standby_actions, standby_weights)[0]
                    self.run(choice)
                    last_action_time = time.time()
                    action_interval = random.randint(2, 6)
            elif self.thread_action_state == ActionStatus.THINK:
                pass
            elif self.thread_action_state == ActionStatus.ACTIONS:
                _action = self.action_queue.get()
                try:
                    self.run(_action)
                except Exception as e:
                    print(f'action error: {e}')

                if self.action_queue.empty():
                    self.thread_action_state = ActionStatus.STANDBY
                    last_action_time = time.time()

                time.sleep(0.5)

            time.sleep(0.01)

    def add_action(self, *actions):
        for action in actions:
            self.action_queue.put(action)
        self.thread_action_state = ActionStatus.ACTIONS

    def set_status(self, status):
        self.thread_action_state = status

    def wait_actions_done(self):
        while self.thread_action_state != ActionStatus.STANDBY:
            time.sleep(0.01)

    def start(self):
        self.thread_running = True
        self.thread_action_state = ActionStatus.STANDBY
        self.action_queue = queue.Queue()
        self.thread = threading.Thread(name="action_handler", target=self.action_handler)
        self.thread.start()

    def stop(self):
        self.thread_running = False
        if self.thread != None:
            self.thread.join()
