from pidog import Pidog
from pidog.action_flow import Operations, ActionStatus, Posetures, ActionFlow
import time

my_dog = Pidog()
action_flow = ActionFlow(my_dog)

def main():          
    action_flow.start()                       # worker begins idle "waiting" motions
    action_flow.change_poseture(Posetures.SIT)
    time.sleep(3)

    # user speaks -> app suspends motion while the LLM thinks
    action_flow.set_status(ActionStatus.THINK)
    time.sleep(3)

    action_flow.add_action(Operations.WAG_TAIL, Operations.SCRATCH)   # state -> ACTIONS
    action_flow.wait_actions_done()              # blocks until back in STANDBY

    action_flow.change_poseture(Posetures.SIT)
    action_flow.stop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"\033[31mERROR: {e}\033[m")
    finally:
        action_flow.wait_actions_done()
        action_flow.stop()
        my_dog.close()