"""
  Capstone Project.  Code written by Logan Cody.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """

    # black_line()
    # run_test_see_color()
    raise_arm()


def black_line():

    robot = rb.Snatch3rRobot()
    while True:
        if robot.color_sensor.get_reflected_intensity() <= 50:
            robot.drive_system.start_moving(80, 80)
        elif robot.color_sensor.get_reflected_intensity() > 50:
            robot.drive_system.left_wheel.start_spinning(80)
            robot.drive_system.right_wheel.stop_spinning(stop_action='brake')


def run_test_see_color():

    see_color('red')


def see_color(color):
    robot = rb.Snatch3rRobot()

    while True:
        robot.drive_system.go_straight_inches(10, 80)
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()


def raise_arm():
    robot = rb.Snatch3rRobot()

    # robot.arm.raise_arm_and_close_claw()
    # robot.arm.calibrate()

main()
