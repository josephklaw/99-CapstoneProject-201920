"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Lucas D'Alesio.
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
    root.title('CSSE 120 Capstone Project')

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------

    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    teleop, arm, control, drive, sound, proximity = get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    grid_frames(teleop, arm, control, drive, sound, proximity)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()

def get_shared_frames(main_frame, mqtt_sender):
    teleop = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive = shared_gui.get_drive_system(main_frame, mqtt_sender)
    sound = shared_gui.get_sound_system(main_frame, mqtt_sender)
    proximity = proximity_frame(main_frame, mqtt_sender)
    return teleop, arm, control, drive, sound, proximity


def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_frame, proximity_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=3,column=0)
    sound_frame.grid(row=0,column=1)
    proximity_frame.grid(row=2, column=1)



def proximity_frame(window,mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label_proximity = ttk.Label(frame,text="Proximity Sensor")
    initial_tone_label = ttk.Label(frame,text="Initial Tone")
    tone_rate_increase_label = ttk.Label(frame,text="Tone Rate")
    initial_tone_entry = ttk.Entry(frame,width=8)
    tone_rate_increase_entry = ttk.Entry(frame,width=8)
    drive_and_tone_button = ttk.Button(frame,text="Drive")
    speed4_entry=ttk.Entry(frame, width=8)
    speed4_label=ttk.Label(frame, text="Speed")

    # Grid the widgets:
    frame_label_proximity.grid(row=0,column=2)
    initial_tone_label.grid(row=1,column=0)
    initial_tone_entry.grid(row=2,column=0)
    tone_rate_increase_label.grid(row=1,column=2)
    tone_rate_increase_entry.grid(row=2,column=2)
    drive_and_tone_button.grid(row=4,column=2)
    speed4_entry.grid(row=2, column=4)
    speed4_label.grid(row=1, column=4)

    drive_and_tone_button["command"] = lambda: handle_drive_and_tone_button(initial_tone_entry, tone_rate_increase_entry, speed4_entry, mqtt_sender)

    return frame

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
def handle_drive_and_tone_button(initial_tone, tone_rate, speed, mqtt_sender):
    print("Driving toward an object while the tone maker increases frequency as the robot gets closer", [initial_tone.get(), tone_rate.get(), speed.get()])
    mqtt_sender.send_message("m2_proximity", [initial_tone.get(), tone_rate.get(), speed.get()])

main()