"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Logan Cody.
"""
# ------------------------------------------------------------------------------
# DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this DONE.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 2. With your instructor, discuss the "big picture" of laptop-robot
# TODO:    communication:
# TODO:      - One program runs on your LAPTOP.  It displays a GUI.  When the
# TODO:        user presses a button intended to make something happen on the
# TODO:        ROBOT, the LAPTOP program sends a message to its MQTT client
# TODO:        indicating what it wants the ROBOT to do, and the MQTT client
# TODO:        SENDS that message TO a program running on the ROBOT.
# TODO:
# TODO:      - Another program runs on the ROBOT. It stays in a loop, responding
# TODO:        to events on the ROBOT (like pressing buttons on the IR Beacon).
# TODO:        It also, in the background, listens for messages TO the ROBOT
# TODO:        FROM the program running on the LAPTOP.  When it hears such a
# TODO:        message, it calls the method in the DELAGATE object's class
# TODO:        that the message indicates, sending arguments per the message.
# TODO:
# TODO:  Once you understand the "big picture", delete this TODO (if you wish).
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 3. One team member: change the following in mqtt_remote_method_calls.py:
#                LEGO_NUMBER = 12
# TODO:    to use YOUR robot's number instead of 99.
# TODO:    Commit and push the change, then other team members Update Project.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# TODO: 4. Run this module.
# TODO:    Study its code until you understand how the GUI is set up.
# TODO:    Then delete this TODO.
# ------------------------------------------------------------------------------

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import rosebotics_new as rb
import ev3dev.ev3 as ev3


def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()
    mqtt = com.MqttClient()
    mqtt.connect_to_ev3()
    # setup_gui(root, mqtt)

    # --------------------------------------------------------------------------
    # DONE: 5. Add code above that constructs a   com.MqttClient   that will
    # DONE:    be used to send commands to the robot.  Connect it to this pc.
    # DONE:    Test.  When OK, delete this DONE.
    # --------------------------------------------------------------------------

    final_project(root, mqtt)

    root.mainloop()

def setup_gui(root_window, mqtt):
    """ Constructs and sets up widgets on the given window. """

    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, mqtt)


def handle_go_forward(entry, mqtt):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    # --------------------------------------------------------------------------
    # DONE: 6. This function needs the entry box in which the user enters
    # DONE:    the speed at which the robot should move.  Make the 2 changes
    # DONE:    necessary for the entry_box constructed in  setup_gui
    # DONE:    to make its way to this function.  When done, delete this DONE.
    # --------------------------------------------------------------------------
    speed_string = entry.get()
    mqtt.send_message('go_forward', [speed_string])
    # --------------------------------------------------------------------------
    # DONE: 7. For this function to tell the robot what to do, it needs
    # DONE:    the MQTT client constructed in main.  Make the 4 changes
    # DONE:    necessary for that object to make its way to this function.
    # DONE:    When done, delete this DONE.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # TODO: 8. Add the single line of code needed to get the string that is
    # TODO:    currently in the entry box.
    # TODO:
    # TODO:    Then add the single line of code needed to "call" a method on the
    # TODO:    LISTENER that runs on the ROBOT, where that LISTENER is the
    # TODO:    "delegate" object that is constructed when the ROBOT's code
    # TODO:    runs on the ROBOT.  Send to the delegate the speed to use
    # TODO:    plus a method name that you will implement in the DELEGATE's
    # TODO:    class in the module that runs on the ROBOT.
    # TODO:
    # TODO:    Test by using a PRINT statement.  When done, delete this TODO.
    # --------------------------------------------------------------------------


def final_project(root, mqtt):

    frame1 = ttk.Frame(root, padding=80)
    frame1.grid()

    entry_box1 = ttk.Entry(frame1)
    entry_box1.grid()

    button1 = ttk.Button(frame1, text='Should I continue to Red?')
    button1['command'] = (lambda: move_forward_or_stop(entry_box1, mqtt))
    button1.grid()


def move_forward_or_stop(entry_box, mqtt):

    if entry_box.get() == 'Yes':
        mqtt.send_message('see_color')
    if entry_box.get() == 'No':
        mqtt.send_message('stop_moving')


main()
