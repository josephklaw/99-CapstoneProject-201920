"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Joseph Law.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("CSSE 120 Capstone Project")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root,padding=10,borderwidth=5,relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_system_frame,sound_frame,proximity_frame,camera_frame = get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame,arm_frame,control_frame,drive_system_frame,sound_frame,proximity_frame,camera_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm = shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control = shared_gui.get_control_frame(main_frame,mqtt_sender)
    drive_system = shared_gui.get_drive_system(main_frame,mqtt_sender)
    sound_frame = shared_gui.get_sound_system(main_frame,mqtt_sender)
    myframe_proximity = get_myframe_proximity(main_frame,mqtt_sender)
    myframe_camera = get_myframe_camera(main_frame,mqtt_sender)
    return teleop, arm, control,drive_system,sound_frame,myframe_proximity, myframe_camera


def grid_frames(teleop_frame, arm_frame, control_frame,drive_system_frame,sound_frame,proximity_frame,camera_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)
    drive_system_frame.grid(row=0,column=1)
    sound_frame.grid(row=1,column=1)
    proximity_frame.grid(row=2,column=1)
    camera_frame.grid(row=3,column=0)

def get_myframe_proximity(window,mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label_proximity = ttk.Label(frame,text="Proximity Sensor")
    initial_beep_rate_label = ttk.Label(frame,text="Initial Beep Rate")
    beep_rate_increase_label = ttk.Label(frame,text="Beep Rate Increase")
    initial_beep_rate_entry = ttk.Entry(frame,width=8)
    beep_rate_increase_entry = ttk.Entry(frame,width=8)
    drive_and_beep_button = ttk.Button(frame,text="Drive and Beep")

    # Grid the widgets:
    frame_label_proximity.grid(row=0,column=1)
    initial_beep_rate_label.grid(row=1,column=0)
    initial_beep_rate_entry.grid(row=2,column=0)
    beep_rate_increase_label.grid(row=1,column=2)
    beep_rate_increase_entry.grid(row=2,column=2)
    drive_and_beep_button.grid(row=2,column=1)

    # Set the Button callbacks:
    drive_and_beep_button["command"] = lambda: handle_drive_forward_for_time(seconds_entry, speed_entry, mqtt_sender)

    return frame
def get_myframe_camera(window,mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame,text="Finding Object Through Spinning")
    direction_label = ttk.Label(frame,text="CW or CCW")
    direction_entry = ttk.Entry(frame,width=8)
    speed_label = ttk.Label(frame,text="Speed")
    speed_entry = ttk.Entry(frame,width=8)
    find_object_button = ttk.Button(frame,text="Find Object")

    # Grid the widgets:
    frame_label.grid(row=0,column=1)
    direction_label.grid(row=1,column=0)
    direction_entry.grid(row=2,column=0)
    speed_label.grid(row=1,column=2)
    speed_entry.grid(row=2,column=2)
    find_object_button.grid(row=2,column=1)

    return frame

# -----------------------------------------------------------------------------
# Handle Functions
# -----------------------------------------------------------------------------
def handle_proximity(initial_beep_rate,beep_rate_increase,mqtt_sender):
    print("Proximity Beeping and Booping (Initial rate - Increase): (",initial_beep_rate,"-",beep_rate_increase)
    mqtt_sender.send_message()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()