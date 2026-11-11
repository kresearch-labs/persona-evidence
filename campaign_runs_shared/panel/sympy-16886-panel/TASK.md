# TASK
The project (sympy, checked out at an old commit) has this issue:

Morse encoding for "1" is not correct
The current Morse mapping in simpy.crypto.crypto contains an incorrect mapping of 
`"----": "1"`   

The correct mapping is `".----": "1"`.




Find the cause and make the minimal correct fix in the source (not in tests).
Do NOT modify or add tests. Do NOT commit. Leave your changes in the working tree.
