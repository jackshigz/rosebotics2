"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # run_test_go_straight_inches()
    # run_test_turn_degrees()
    run_test_polygon()

def run_test_go_straight_inches():
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(20)

def run_test_turn_degrees():
    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(180)

def run_test_polygon():
    run_polygon(6)

def run_polygon(n):
    robot = rb.Snatch3rRobot()
    degree = 360/n
    for _ in range(n):
        robot.drive_system.go_straight_inches(4)
        robot.drive_system.turn_degrees(degree)



main()
