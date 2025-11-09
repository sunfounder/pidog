# 5_stop_actions

**File:** `basic_examples/5_stop_actions.py`

## Module Description

stop all actions


API:
    Pidog.wait_all_done()
        wait for all the actions in the leg actions buffer, head buffer and tail buffer to be executed

    Pidog.body_stop()
        stop all the actions of legs, head and tail

    Pidog.stop_and_lie()
        stop all the actions of legs, head and tail, then reset to "lie" pose

    Pidog.close()
        stop all the actions, reset to "lie" pose, and  close all the threads,
        usually used when exiting a program

