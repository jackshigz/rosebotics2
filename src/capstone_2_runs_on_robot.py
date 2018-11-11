"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Haoran Shi.
"""
# ------------------------------------------------------------------------------
# TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, review the "big picture" of laptop-robot
# TODO:    communication, per the comment in mqtt_sender.py.
# TODO:    Once you understand the "big picture", delete this TODO.
# ------------------------------------------------------------------------------

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # TODO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # TODO: 4. Add code that constructs a   com.MqttClient   that will
    # TODO:    be used to receive commands sent by the laptop.
    # TODO:    Connect it to this robot.  Test.  When OK, delete this TODO.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
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

class RemoteControlEtc(object):
    def __init__(self,robot):
        """
        Stores the robot.
            :type robot: rb.Snatch3rRobot
        """
        self.robot = robot

    def go_forward(self,speed_string):
        """Makes the robot go forward at the given speed"""
        print("Telling the robot to start moving at",speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed,speed)

    def do_stuff(self,size1_string,size2_string):
        """Make the robot do stuff according to the given color if it is checked"""
        print("Telling the robot to do stuff according to",size1_string,size2_string)
        size1 = int(size1_string)
        size2 = int(size2_string)

        time1 = time.time()
        while True:
            blob = self.robot.camera.get_biggest_blob()
            print(blob.get_area())
            if  blob.get_area() >= size1:
                if blob.get_area() <= size2:
                    self.do_thing_1()
                    break
                else:
                    self.robot.drive_system.spin_in_place_degrees(1080)
                    break
            if time.time() - time1 >= 10:
                self.robot.drive_system.turn_degrees(-30)
                self.robot.drive_system.turn_degrees(60)
                self.robot.drive_system.turn_degrees(-30)
                ev3.Sound.beep().wait()
                ev3.Sound.beep().wait()
                break
            else:
                self.do_other_thing()
                break

    def do_thing_1(self):
        self.robot.drive_system.go_straight_inches(10)
        self.robot.drive_system.turn_degrees(45)
        self.robot.drive_system.go_straight_inches(5)
        self.robot.drive_system.turn_degrees(-45)
        self.robot.drive_system.go_straight_inches(-10)
        self.robot.drive_system.spin_in_place_degrees(-90)
        self.robot.drive_system.go_straight_inches(5)
        self.robot.drive_system.turn_degrees(90)

    def do_other_thing(self):
        degree = 360/4
        self.robot.drive_system.go_straight_inches(5)
        for _ in range(4):
            self.robot.drive_system.go_straight_inches(20)
            self.robot.drive_system.turn_degrees(degree)
main()