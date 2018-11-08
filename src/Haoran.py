"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import ev3dev.ev3 as ev3
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_go_straight_inches()
    # run_test_turn_degrees()
    # run_test_polygon()
    # run_test_beep_when_see()
    # run_test_go_forward_beacon()

def run_test_go_straight_inches():
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(20)

def run_test_turn_degrees():
    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(180)

def run_test_polygon():
    run_polygon(6)

def run_polygon(n):
    degree = 360/n
    robot = rb.Snatch3rRobot()
    for _ in range(n):
        robot.drive_system.go_straight_inches(20)
        robot.drive_system.turn_degrees(degree)
        # run_polygon_straight()
        # run_polygon_turn(degree)

def run_polygon_straight():
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(20)

def run_polygon_turn(degree):
    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(degree)

def run_test_beep_when_see():
    robot = rb.Snatch3rRobot()
    while True:
        blob = robot.camera.get_biggest_blob()
        if blob.get_area() >= 1000:
            ev3.Sound.beep().wait()
            break

def run_test_go_forward_beacon():
    robot = rb.Snatch3rRobot()
    while True:

        if robot.beacon_button_sensor.is_bottom_blue_button_pressed() == True:
            robot.drive_system.go_straight_inches(20)
            break


main()
