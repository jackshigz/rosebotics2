"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """

    robot = rb.Snatch3rRobot()

    robot.drive_system.spin_in_place_degrees(90)

main()
