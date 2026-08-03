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

class Operations(StrEnum):
    FORWARD = 'forward'
    BACKWARD = 'backward'
    TURN_LEFT = 'turn left'
    TURN_RIGHT = 'turn right'
    STOP = 'stop'
    LIE = 'lie'
    STAND = 'stand'
    SIT = 'sit'
    BARK = 'bark'
    BARK_HARDER = 'bark harder'
    PANT = 'pant'
    WAG_TAIL = 'wag tail'
    SHAKE_HEAD = 'shake head'
    STRETCH = 'stretch'
    DOZE_OFF = 'doze off'
    PUSH_UP = 'push up'
    HOWLING = 'howling'
    TWIST_BODY = 'twist body'
    SCRATCH = 'scratch'
    HANDSHAKE = 'handshake'
    HIGH_FIVE = 'high five'
    LICK_HAND = 'lick hand'
    WAITING = 'waiting'
    FEET_SHAKE = 'feet shake'
    RELAX_NECK = 'relax neck'
    NOD = 'nod'
    THINK_ACTION = 'think'
    RECALL = 'recall'
    FLUSTER = 'fluster'
    SURPRISE = 'surprise'

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
        Operations.FORWARD: {
            "function": lambda self: self.dog_obj.do_action(Operations.FORWARD, speed=98),
            "poseture": Posetures.STAND,
        },
        Operations.BACKWARD: {
            "function": lambda self: self.dog_obj.do_action(Operations.BACKWARD, speed=98),
            "poseture": Posetures.STAND,
        },
        Operations.TURN_LEFT: {
            "function": lambda self: self.dog_obj.do_action(Operations.TURN_LEFT, speed=98),
            "poseture": Posetures.STAND,
        },
        Operations.TURN_RIGHT: {
            "function": lambda self: self.dog_obj.do_action(Operations.TURN_RIGHT, speed=98),
            "poseture": Posetures.STAND,
        },
        Operations.STOP: {
        },
        Operations.LIE: {
            "function": lambda self: self.dog_obj.do_action(Operations.LIE, speed=70),
            "poseture": Posetures.LIE,
        },
        Operations.STAND: {
            "function": lambda self: self.dog_obj.do_action(Operations.STAND, speed=65),
            "poseture": Posetures.STAND,
        },
        Operations.SIT: {
            "function": lambda self: self.dog_obj.do_action(Operations.SIT, speed=70),
            "poseture": Posetures.SIT,
        },
        Operations.BARK: {
            "function": lambda self: bark(self.dog_obj, self.head_yrp, pitch_comp=self.head_pitch_init),
        },
        Operations.BARK_HARDER: {
            # "before": "stand",
            "before": lambda self: attack_posture(self.dog_obj),
            "function": lambda self: bark_action(self.dog_obj, self.head_yrp, 'single_bark_1'),
            "poseture": Posetures.STAND,
        },
        Operations.PANT: {
            "function": lambda self: pant(self.dog_obj, self.head_yrp, pitch_comp=self.head_pitch_init),
        },
        Operations.WAG_TAIL: {
            "function": lambda self: self.dog_obj.do_action(Operations.WAG_TAIL, speed=100),
            "after": Operations.WAG_TAIL,
        },
        Operations.SHAKE_HEAD: {
            "function": lambda self: shake_head(self.dog_obj, [self.head_yrp[0], self.head_yrp[1], self.head_yrp[2]+self.head_pitch_init]),
        },
        Operations.STRETCH: {
            "function": lambda self: stretch(self.dog_obj),
            "after": Operations.SIT,
            "poseture": Posetures.SIT,
        },
        Operations.DOZE_OFF: {
            "function": lambda self: self.dog_obj.do_action(Operations.DOZE_OFF, speed=95),
            "after": Operations.DOZE_OFF,
            "poseture": Posetures.LIE,
        },
        Operations.PUSH_UP: {
            "function": lambda self:push_up(self.dog_obj),
            "poseture": Posetures.STAND,
        },
        Operations.HOWLING: {
            "function": lambda self:howling(self.dog_obj),
            "after": Operations.SIT,
            "poseture": Posetures.SIT,
        },
        Operations.TWIST_BODY: {
            "function": lambda self:body_twisting(self.dog_obj),
            "after": Operations.SIT,
            "poseture": Posetures.STAND,
        },
        Operations.SCRATCH: {
            "function": lambda self:scratch(self.dog_obj),
            "after": Operations.SIT,
            "poseture": Posetures.SIT,
        },
        Operations.HANDSHAKE: {
            "function": lambda self:hand_shake(self.dog_obj),
            "after": Operations.SIT,
            "poseture": Posetures.SIT,
        },
        Operations.HIGH_FIVE: {
            "function": lambda self:high_five(self.dog_obj),
            "after": Operations.SIT,
            "poseture": Posetures.SIT,
        },
        Operations.LICK_HAND: {
            "function": lambda self:lick_hand(self.dog_obj),
            "poseture": Posetures.SIT,
        },
        Operations.WAITING: {
            "function": lambda self:waiting(self.dog_obj, pitch_comp=self.head_pitch_init),
        },
        Operations.FEET_SHAKE: {
            "function": lambda self:feet_shake(self.dog_obj),
            "poseture": Posetures.SIT,
        },
        Operations.RELAX_NECK: {
            "function": lambda self:relax_neck(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
        Operations.NOD: {
            "function": lambda self:nod(self.dog_obj, pitch_comp=self.head_pitch_init),
            "head_pitch": SIT_HEAD_PITCH,
            "poseture": Posetures.SIT,
        },
        Operations.THINK_ACTION: {
            "function": lambda self:think(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
        Operations.RECALL: {
            "function": lambda self:recall(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
        Operations.FLUSTER: {
            "function": lambda self:fluster(self.dog_obj, pitch_comp=self.head_pitch_init),
            "poseture": Posetures.SIT,
        },
        Operations.SURPRISE: {
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
        self.thread_action_state = ActionStatus.STANDBY
        self.action_queue = queue.Queue()

    def set_head_pitch_init(self, pitch):
        self.head_pitch_init = pitch
        self.dog_obj.head_move([self.head_yrp], pitch_comp=pitch,
                        immediately=True, speed=self.HEAD_SPEED)
                     
    def change_poseture(self, poseture: Posetures):
        if poseture == Posetures.STAND:
            self.set_head_pitch_init(self.STAND_HEAD_PITCH)
            if self.posture != Posetures.STAND:
                sit_2_stand(self.dog_obj, speed=75) # speed > 70
            else:
               self.dog_obj.do_action(Operations.STAND, speed=self.CHANGE_STATUS_SPEED) 
        elif poseture == Posetures.SIT:
            self.set_head_pitch_init(self.SIT_HEAD_PITCH)
            self.dog_obj.do_action(Operations.SIT, speed=self.CHANGE_STATUS_SPEED)
        elif poseture == Posetures.LIE:
            self.set_head_pitch_init(self.STAND_HEAD_PITCH)
            self.dog_obj.do_action(Operations.LIE, speed=self.CHANGE_STATUS_SPEED)
        
        self.posture = poseture
        self.dog_obj.wait_all_done()


    def run(self, action: Operations):
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
        # standby_actions = [Operations.WAITING, Operations.FEET_SHAKE]
        standby_actions = [Operations.FEET_SHAKE]
        standby_weights = [1, 0.3]

        action_interval = 5 # seconds
        last_action_time = time.time()

        while self.thread_running:
            if self.thread_action_state == ActionStatus.STANDBY:
                if time.time() - last_action_time > action_interval:
                    choice = random.choices(standby_actions, standby_weights)[0]
                    self.run(Operations(choice))
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

    def set_status(self, status: ActionStatus):
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
