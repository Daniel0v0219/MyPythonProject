"""
File: StepUp.py
Name: 蔡佾燁
------------------------
This file shows Karel picking up 
the beeper at Street 1 Avenue 2,
putting it onto Street 2 Avenue 4.
Karel will be facing East at Street
2 Avenue 5 at the end of this program.
"""

from karel.stanfordkarel import *

def turn_r():
    for i in range(3):
        turn_left()

def main():
    pass
    move()
    pick_beeper()
    move()
    turn_left()
    move()
    turn_r()
    move()
    put_99b()
    move()

def put_99b():
    for i in range(99):
        put_beeper()

# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
