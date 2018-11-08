"""
  Capstone Project.  Code written by Logan Cody.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """

    # black_line()
    run_test_see_color()
    # raise_arm()


def black_line():

    robot = rb.Snatch3rRobot()

    initial_time = time.time()

    while True:

        if robot.color_sensor.get_reflected_intensity() < 40:
            robot.drive_system.start_moving(40, 40)
        if robot.color_sensor.get_reflected_intensity() >= 40:
            robot.drive_system.start_moving(75, 10)
        if time.time() - initial_time >= 15:
            robot.drive_system.stop_moving()
            break


def run_test_see_color():

    see_color('red')


def see_color(color):
    robot = rb.Snatch3rRobot()

    while True:
        robot.drive_system.go_straight_inches(10, 80)
        if robot.color_sensor.get_color() == color:
            robot.drive_system.stop_moving()
            break


def raise_arm():
    robot = rb.Snatch3rRobot()

    # robot.arm.raise_arm_and_close_claw()
    # robot.arm.calibrate()

main()
