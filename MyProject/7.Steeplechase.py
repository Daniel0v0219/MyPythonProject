"""
File: Steeplechase.py
Name: 蔡佾燁
---------------------------------
蔡佾燁
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()


def jump():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is on the right side of the wall
    """
    up()
    cross()
    down()


def cross():
    """
    Pre-condition: Karel is on the upper left of the wall, facing North
    Post-condition:Karel is on the upper rigth of the wall, facing South
    """
    turn_right()
    move()
    turn_right()

def down():
    """
    Pre-condition: Karel is on the upper right, facing South
    Post-condition:
    """
    while front_is_clear():
        move()


def up():
    """
    Pre-condition: Karel is on the left side of the wall, facing East
    Post-condition: Karel is on the upper right, facing North
    """
    turn_left()
    while not right_is_clear():
        move()

    #    alternative:
    #    while not front_is_clear():
    #    turn_left()
    #    move()
    #    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
