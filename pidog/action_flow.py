from .preset_actions import *

class ActionFlow():
    SIT_HEAD_PITCH = -35
    STAND_HEAD_PITCH = 0
    STATUS_STAND = 0
    STATUS_SIT = 1
    STATUS_LIE = 2
    HEAD_SPEED = 80
    HEAD_ANGLE = 20
    CHANGE_STATUS_SPEED = 60

    dog_obj = None
    head_yrp = [0, 0, 0]
    head_pitch_init = 0
    current_status = -1
    last_actions = None

    OPERATIONS = {
        "forward": {
            "function": lambda self: self.dog_obj.do_action('forward', speed=98),
            "status": STATUS_STAND,
        },
        "backward": {
            "function": lambda self: self.dog_obj.do_action('backward', speed=98),
            "status": STATUS_STAND,
        },
        "turn left": {
            "function": lambda self: self.dog_obj.do_action('turn_left', speed=98),
            "status": STATUS_STAND,
        },
        "turn right": {
            "function": lambda self: self.dog_obj.do_action('turn_right', speed=98),
            "status": STATUS_STAND,
        },
        "stop": {
        },
        "lie": {
            "function": lambda self: self.dog_obj.do_action('lie', speed=70),
            "status": STATUS_LIE,
        },
        "stand": {
            "function": lambda self: self.dog_obj.do_action('stand', speed=65),
            "status": STATUS_STAND,
        },
        "sit": {
            "function": lambda self: self.dog_obj.do_action('sit', speed=70),
            "status": STATUS_SIT,
        },
        "bark": {
            "function": lambda self: bark(self.dog_obj, self.head_yrp, pitch_comp=self.head_pitch_init),
        },
        "bark harder": {
            # "before": "stand",
            "before": lambda self: attack_posture(self.dog_obj),
            "function": lambda self: bark_action(self.dog_obj, self.head_yrp, 'single_bark_1'),
            "status": STATUS_STAND,
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
            "status": STATUS_SIT,
        },
        "doze off": {
            "function": lambda self: self.dog_obj.do_action('doze_off', speed=95),
            "after": "doze off",
            "status": STATUS_LIE,
        },
        "push up": {
            "function": lambda self:push_up(self.dog_obj),
            "status": STATUS_STAND,
        },
        "howling": {
            "function": lambda self:howling(self.dog_obj),
            "after": "sit",
            "status": STATUS_SIT,
        },
        "twist body": {
            "function": lambda self:body_twisting(self.dog_obj),
            "after": "sit",
            "status": STATUS_STAND,
        },
        "scratch": {
            "function": lambda self:scratch(self.dog_obj),
            "after": "sit",
            "status": STATUS_SIT,
        },
        "handshake": {
            "function": lambda self:hand_shake(self.dog_obj),
            "after": "sit",
            "status": STATUS_SIT,
        },
        "high five": {
            "function": lambda self:high_five(self.dog_obj),
            "after": "sit",
            "status": STATUS_SIT,
        },
        "lick hand": {
            "function": lambda self:lick_hand(self.dog_obj),
            "status": STATUS_SIT,
        },
        "waiting": {
            "function": lambda self:waiting(self.dog_obj, pitch_comp=self.head_pitch_init),
        },
        "feet shake": {
            "function": lambda self:feet_shake(self.dog_obj),
            "status": STATUS_SIT,
        },
        "relax neck": {
            "function": lambda self:relax_neck(self.dog_obj, pitch_comp=self.head_pitch_init),
            "status": STATUS_SIT,
        },
        "nod": {
            "function": lambda self:nod(self.dog_obj, pitch_comp=self.head_pitch_init),
            "head_pitch": SIT_HEAD_PITCH,
            "status": STATUS_SIT,
        },
        "think": {
            "function": lambda self:think(self.dog_obj, pitch_comp=self.head_pitch_init),
            "status": STATUS_SIT,
        },
        "recall": {
            "function": lambda self:recall(self.dog_obj, pitch_comp=self.head_pitch_init),
            "status": STATUS_SIT,
        },
        "fluster": {
            "function": lambda self:fluster(self.dog_obj, pitch_comp=self.head_pitch_init),
            "status": STATUS_SIT,
        },
        "surprise": {
            "function": lambda self:surprise(self.dog_obj, pitch_comp=self.head_pitch_init),
            "status": STATUS_SIT,
        },
    }

    def __init__(self, dog_obj):

        self.dog_obj = dog_obj

        self.head_yrp = [0, 0, 0]
        self.head_pitch_init = 0
        self.current_status = self.STATUS_LIE


    def set_head_pitch_init(self, pitch):
        self.head_pitch_init = pitch
        self.dog_obj.head_move([self.head_yrp], pitch_comp=pitch,
                        immediately=True, speed=self.HEAD_SPEED)
                     
    def change_status(self, status):
        if status == self.STATUS_STAND:
            self.set_head_pitch_init(self.STAND_HEAD_PITCH)
            if self.current_status != self.STATUS_STAND:
                sit_2_stand(self.dog_obj, speed=75) # speed > 70
            else:
               self.dog_obj.do_action('stand', speed=self.CHANGE_STATUS_SPEED) 
        elif status == self.STATUS_SIT:
            self.set_head_pitch_init(self.SIT_HEAD_PITCH)
            self.dog_obj.do_action('sit', speed=self.CHANGE_STATUS_SPEED)
        elif status == self.STATUS_LIE:
            self.set_head_pitch_init(self.STAND_HEAD_PITCH)
            self.dog_obj.do_action('lie', speed=self.CHANGE_STATUS_SPEED)
        
        self.current_status = status
        self.dog_obj.wait_all_done()


    def run(self, action):
        try:
            # print(f'run: {action}')
            if action in self.OPERATIONS:
                operation = self.OPERATIONS[action]
                # status
                if "status" in operation and operation["status"] != None:
                    # if self.current_status != operation["status"]:
                    if self.last_actions != action:
                        self.last_actions = action 
                        self.change_status(operation["status"])
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


def test(my_dog):
    action_flow = ActionFlow(my_dog)
    action_flow.change_status(action_flow.STATUS_SIT)
    # action_flow.change_status(action_flow.STATUS_STAND)


    actions = list(action_flow.OPERATIONS.keys())
    for i, key in enumerate(actions):
        print(f'{i} {key}')

    last_key = None

    while True:
        key = input()
        try:
            if key == '':
                print(actions[last_key])
                action_flow.run(actions[last_key])
            else:
                key = int(key)
                last_key = key
                print(actions[key])
                action_flow.run(actions[key])
        except:
            print('Invalid input')

if __name__ == '__main__':
    try:
        from pidog import Pidog
        import time
        my_dog = Pidog()
        time.sleep(1)
        my_dog.rgb_strip.set_mode('listen', 'cyan', 1)

        test(my_dog)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        my_dog.close()

