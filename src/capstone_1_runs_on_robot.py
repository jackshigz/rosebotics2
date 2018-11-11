"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Logan Cody.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this DONE.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# DONE: 2. With your instructor, review the "big picture" of laptop-robot
# DONE:    communication, per the comment in mqtt_sender.py.
# DONE:    Once you understand the "big picture", delete this DONE.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # DONE: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this DONE.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # DONE: 4. Add code that constructs a   com.MqttClient   that will
    # DONE:    be used to receive commands sent by the laptop.
    # DONE:    Connect it to this robot.  Test.  When OK, delete this DONE.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt = com.MqttClient(rc)
    mqtt.connect_to_pc()
    # --------------------------------------------------------------------------
    # TODO: 5. Add a class for your "delegate" object that will handle messages
    # TODO:    sent from the laptop.  Construct an instance of the class and
    # TODO:    pass it to the MqttClient constructor above.  Augment the class
    # TODO:    as needed for that, and also to handle the go_forward message.
    # TODO:    Test by PRINTING, then with robot.  When OK, delete this TODO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 6. With your instructor, discuss why the following WHILE loop,
    # TODO:    that appears to do nothing, is necessary.
    # TODO:    When you understand this, delete this TODO.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # TODO: 7. Add code that makes the robot beep if the top-red button
        # TODO:    on the Beacon is pressed.  Add code that makes the robot
        # TODO:    speak "Hello. How are you?" if the top-blue button on the
        # TODO:    Beacon is pressed.  Test.  When done, delete this TODO.
        # ----------------------------------------------------------------------
        time.sleep(0.01)  # For the delegate to do its work

        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep().wait()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hello. How are you?')


class RemoteControlEtc(object):

    def __init__(self, robot):
        """
        Stores the robot.
            :type robot: rb.Snatch3rRobot

        """
        self.robot = robot

    def go_forward(self, speed_string):
        """"Makes the robot go forward at the given speed"""
        print('tell robot to move at', speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def stop_moving(self):
        self.robot.drive_system.stop_moving()

    def see_color(self):

        self.robot.drive_system.start_moving(80, 80)
        while True:
            if self.robot.color_sensor.get_color() == 5:
                self.robot.drive_system.stop_moving()
                break
        self.robot.drive_system.spin_in_place_degrees(460)
        c = (self.robot.drive_system.left_wheel.get_degrees_spun() +
             self.robot.drive_system.right_wheel.get_degrees_spun()) / 2
        print('Robot traveled', c / 87, 'inches')


robot = rb.Snatch3rRobot()


def final_project():

    robot.drive_system.start_moving(80, 80)
    while True:
        if robot.color_sensor.get_reflected_intensity() <= 40:
            robot.drive_system.stop_moving()
            break

    rc = RemoteControlEtc(robot)
    mqtt = com.MqttClient(rc)
    mqtt.connect_to_pc()

    while True:
        time.sleep(0.1)


final_project()
