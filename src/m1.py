"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_go_straight_inches()

def run_test_go_straight_inches():
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(20)

main()
