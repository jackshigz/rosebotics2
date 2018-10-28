"""
  Capstone Project.  Code written by Logan Cody.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """

    black_line()


def black_line():

    robot = rb.Snatch3rRobot()

    robot.drive_system.move_for_seconds(15)
    if robot.color_sensor.get_value() < 50:
        robot.drive_system.turn_degrees(10)


main()

