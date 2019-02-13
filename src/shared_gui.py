"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Joseph Law, Aaryan Khatri, and Lucas D'Alesio.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame
def get_drive_system(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Drive System")
    forward_for_seconds = ttk.Button(frame, text="Seconds")
    forward_for_inches_time = ttk.Button(frame, text="Inches (Time)")
    forward_for_inches_sensor = ttk.Button(frame,text="Inches (Sensor")
    seconds_entry = ttk.Entry(frame, width=8)
    inches_entry_time = ttk.Entry(frame,width = 8)
    inches_entry_sensor = ttk.Entry(frame,width=8)
    speed_entry = ttk.Entry(frame,width=8)
    speed_label = ttk.Label(frame,text="Speed")
    color_label = ttk.Label(frame,text="Color")
    intensity_label = ttk.Label(frame,text="Intensity")
    color_entry = ttk.Entry(frame,width=8)
    intensity_entry = ttk.Entry(frame,width=8)
    straight_until_intensity_less = ttk.Button(frame,text="Straight until intensity <")
    straight_until_intensity_great = ttk.Button(frame,text="Straight until intensity >")
    straight_until_color_is = ttk.Button(frame,text="Straight until color =")
    straight_until_color_is_not = ttk.Button(frame,text="Straight until color !=")


    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    forward_for_seconds.grid(row=2, column=0)
    seconds_entry.grid(row=1,column=0)
    forward_for_inches_time.grid(row=2,column=1)
    inches_entry_time.grid(row=1,column=1)
    forward_for_inches_sensor.grid(row=2,column=2)
    inches_entry_sensor.grid(row=1,column=2)
    speed_label.grid(row=3,column=0)
    speed_entry.grid(row=4,column=0)
    color_label.grid(row=3,column=1)
    intensity_label.grid(row=3,column=2)
    color_entry.grid(row=4,column=1)
    intensity_entry.grid(row=4,column=2)
    straight_until_intensity_less.grid(row=5,column=0)
    straight_until_intensity_great.grid(row=5,column=2)
    straight_until_color_is.grid(row=6,column=0)
    straight_until_color_is_not.grid(row=6,column=2)



    # Set the Button callbacks:
    forward_for_seconds["command"] = lambda: handle_drive_forward_for_time(seconds_entry, speed_entry, mqtt_sender)
    forward_for_inches_time["command"] = lambda: handle_drive_forward_for_inches_time(inches_entry_time, mqtt_sender)
    forward_for_inches_sensor["command"] = lambda: handle_drive_forward_for_inches_sensor(inches_entry_sensor, speed_entry, mqtt_sender)
    straight_until_intensity_less["command"] = lambda: handle_go_straight_until_intensity_is_less_than(intensity_entry,speed_entry,mqtt_sender)
    straight_until_intensity_great["command"] = lambda: handle_go_straight_until_intensity_is_greater_than(intensity_entry,speed_entry,mqtt_sender)
    straight_until_color_is["command"] = lambda: handle_go_straight_until_color_is(color_entry,speed_entry,mqtt_sender)
    straight_until_color_is_not["command"] = lambda: handle_go_straight_until_color_is_not(color_entry, speed_entry,mqtt_sender)

    return frame

def get_sound_system(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window(via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sound System")
    beep_label = ttk.Label(frame,text="# of Times to Beep")
    beep_button = ttk.Button(frame, text="Beep")
    beep_entry = ttk.Entry(frame,width = 8)
    frequency_label = ttk.Label(frame,text="Frequency of Tone")
    frequency_entry = ttk.Entry(frame,width=8)
    tone_button = ttk.Button(frame,text="Tone")
    duration_label = ttk.Label(frame,text="Duration of Tone")
    duration_entry = ttk.Entry(frame,width=8)
    phrase_label = ttk.Label(frame,text="Phrase")
    phrase_entry = ttk.Entry(frame,width=20)
    speak_button = ttk.Button(frame,text="Speak")

    # Grid the widgets:
    frame_label.grid(row=0, column=2)
    beep_label.grid(row=1,column=0)
    beep_button.grid(row=3, column=0)
    beep_entry.grid(row=2,column=0)
    frequency_label.grid(row=1,column=1)
    frequency_entry.grid(row=2,column=1)
    tone_button.grid(row=2,column=2)
    duration_label.grid(row=1,column=3)
    duration_entry.grid(row=2,column=3)
    phrase_label.grid(row=1,column=4)
    phrase_entry.grid(row=2,column=4)
    speak_button.grid(row=3,column=4)



    # Set the Button callbacks:
    beep_button["command"] = lambda: handle_beep(beep_entry, mqtt_sender)
    tone_button["command"] = lambda: handle_tone(frequency_entry,duration_entry,mqtt_sender)
    speak_button["command"] = lambda: handle_speak(phrase_entry,mqtt_sender)

    return frame
###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("forward",left_entry_box.get(),right_entry_box.get())
    mqtt_sender.send_message("forward",[left_entry_box.get(),
                                        right_entry_box.get()])

def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("backward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [-1*int(left_entry_box.get()),
                                         -1*int(right_entry_box.get())])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("left", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [1,
                                         right_entry_box.get()])

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("right", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(),
                                         1])

def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Stop")
    mqtt_sender.send_message("stop")

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Raise Arm")
    mqtt_sender.send_message("raise_arm")

def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Lower Arm")
    mqtt_sender.send_message("lower_arm")

def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Calibrate Arm")
    mqtt_sender.send_message("calibrate_arm")

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("Move Arm to Position")
    mqtt_sender.send_message("move_arm_to_position",[arm_position_entry.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print("quit")
    mqtt_sender.send_message("is_quit")

def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print("Exit")
    handle_quit(mqtt_sender)
    exit()
###############################################################################
# Handlers for Buttons in the Drive System frame.
###############################################################################
def handle_drive_forward_for_time(seconds_entry,speed_entry,mqtt_sender):
    print("Drive forward for time",seconds_entry.get())
    mqtt_sender.send_message("drive_forward_for_time", [seconds_entry.get(),speed_entry.get()])
def handle_drive_forward_for_inches_time(inches_entry_time,mqtt_sender):
    print("Drive forward for inches using time",inches_entry_time.get())
    mqtt_sender.send_message("drive_forward_for_inches_time", [inches_entry_time.get()])
def handle_drive_forward_for_inches_sensor(inches_entry_sensor,speed_entry,mqtt_sender):
    print("Drive forward for inches using time",inches_entry_sensor.get())
    mqtt_sender.send_message("drive_forward_for_inches_sensor", [inches_entry_sensor.get(),speed_entry.get()])
def handle_go_straight_until_intensity_is_less_than(intensity_entry,speed_entry,mqtt_sender):
    print("Go straight until intensity is less than", intensity_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_less_than",[intensity_entry.get(),speed_entry.get()])
def handle_go_straight_until_intensity_is_greater_than(intensity_entry,speed_entry,mqtt_sender):
    print("Go straight until intensity is greater than", intensity_entry.get())
    mqtt_sender.send_message("go_straight_until_intensity_is_greater_than",[intensity_entry.get(),speed_entry.get()])
def handle_go_straight_until_color_is(color_entry,speed_entry,mqtt_sender):
    print("Go straight until color is",color_entry.get(),speed_entry.get())
    mqtt_sender.send_message("go_straight_until_color_is",[color_entry.get(),speed_entry.get()])
def handle_go_straight_until_color_is_not(color_entry,speed_entry,mqtt_sender):
    print("Go straight until color is not",color_entry.get())
    mqtt_sender.send_message("go_straight_until_color_is_not",[color_entry.get(),speed_entry.get()])
###############################################################################
# Handlers for Buttons in the Sound System frame.
###############################################################################
def handle_beep(beep_entry,mqtt_sender):
    print("Beep!",beep_entry.get())
    mqtt_sender.send_message("sound_beep", [beep_entry.get()])
def handle_tone(frequency_entry,duration_entry,mqtt_sender):
    print("Tone",frequency_entry.get(),duration_entry.get())
    mqtt_sender.send_message("sound_tone",[frequency_entry.get(),duration_entry.get()])
def handle_speak(phrase_entry,mqtt_sender):
    print("Speak",phrase_entry.get())
    mqtt_sender.send_message("sound_speak",[phrase_entry.get()])
