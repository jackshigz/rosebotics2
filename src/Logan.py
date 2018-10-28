"""
  Capstone Project.  Code written by Logan Cody.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """

    # black_line()
    see_color()


def black_line():

    robot = rb.Snatch3rRobot()

    while True:
        robot.drive_system.move_for_seconds(30)
        if robot.color_sensor.get_value() < 50:
            robot.drive_system.turn_degrees(1)


def see_color():
    robot = rb.Snatch3rRobot()

    color = 'red'

    while True:
        robot.drive_system.go_straight_inches(10, 80)
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()

main()

