"""
File: PotholeFilling.py
Name: 蔡佾燁
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def go_in():
    """
    pre-condition:Karel is at upper left of the pothole,facing East
    post-condition:Karel is in the pothole,facing South
    """
    move()
    turn_r()
    move()


def go_out():
    """
    pre-condition:Karel is in the pothole,facing South
    post-condition:Karel is at upper left of the pothole,facing East
    """
    turn_left()
    turn_left()
    move()
    turn_r()
    move()

def main():
    """
    TODO:
    """

    for i in range(3):
        go_in()
        put_99b()
        go_out()



# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
