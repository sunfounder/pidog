# walk

**File:** `pidog/walk.py`

## Module Description

A full MOVE divided into 8 SECTIONs. like below:
leg| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7
====|===|===|===|===|===|===|===|===
 1  |^^^|___|___|___|___|___|___|___
 2  |___|___|___|___|^^^|___|___|___
 3  |___|___|___|___|___|___|^^^|___
 4  |___|___|^^^|___|___|___|___|___

4 legs move in this order: 1, 4, 2, 3
there will be a break after every leg move

every SECTION devide into 4 STEPs

