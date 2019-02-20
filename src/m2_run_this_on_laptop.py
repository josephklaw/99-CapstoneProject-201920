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

    #teleop, arm, control, drive, sound, proximity, camera = get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    sprint_3 = get_my_frames(main_frame,mqtt_sender)


    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------

    grid_my_frames(sprint_3)

    #grid_frames(teleop, arm, control, drive, sound, proximity, camera)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------

    root.mainloop()

#def get_shared_frames(main_frame, mqtt_sender):
#    teleop = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
#    arm = shared_gui.get_arm_frame(main_frame, mqtt_sender)
#    control = shared_gui.get_control_frame(main_frame, mqtt_sender)
#    drive = shared_gui.get_drive_system(main_frame, mqtt_sender)
#    sound = shared_gui.get_sound_system(main_frame, mqtt_sender)
#    proximity = proximity_frame(main_frame, mqtt_sender)
#    camera = camera_frame(main_frame, mqtt_sender)
#    return teleop, arm, control, drive, sound, proximity, camera


#def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_frame, proximity_frame, camera_frame):
 #  arm_frame.grid(row=1, column=0)
 #  control_frame.grid(row=2, column=0)
 #  drive_system_frame.grid(row=3,column=0)
 #  sound_frame.grid(row=0,column=1)
 #  proximity_frame.grid(row=2, column=1)
 #  camera_frame.grid(row=3, column=1)





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

def camera_frame(window,mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame,text="Camera")
    direction_label = ttk.Label(frame,text="Direction(CW or CCW)")
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

    find_object_button["command"]=lambda:handle_find_object_button(direction_entry, speed_entry, mqtt_sender)

    return frame

def sprint_3_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief='ridge')
    frame.grid()

    color_button_label = ttk.Label(frame, text='Color Input')
    blue_label = ttk.Label(frame, text='Blue = 2')
    red_label = ttk.Label(frame, text ="Red = 5")
    green_label = ttk.Label(frame, text="Green = 3")
    yellow_label = ttk.Label(frame, text="Yellow = 4")
    frame_label = ttk.Label(frame, text='The Rainbow Recycler')
    color_button = ttk.Button(frame, text='Color Finder')
    color_entry = ttk.Entry(frame, width=8)
    find_object_button = ttk.Button(frame, text="Find Object")
    line_following_button = ttk.Button(frame, text="Line Following")
    part_1 = ttk.Checkbutton(frame)
    part_2 = ttk.Checkbutton(frame)
    part_3 = ttk.Checkbutton(frame)
    speed_entry = ttk.Entry(frame, width=8)
    speed_label = ttk.Label(frame, text='Speed')

    color_button_label.grid(row=4, column=0)
    frame_label.grid(row=0, column=1)
    color_button.grid(row=3, column=0)
    color_entry.grid(row=6, column=0)
    find_object_button.grid(row=3, column=1)
    line_following_button.grid(row=3, column=2)
    part_1.grid(row=7, column=0)
    part_2.grid(row=7, column=1)
    part_3.grid(row=7, column=2)
    speed_entry.grid(row=6, column=1)
    speed_label.grid(row=4, column=1)
    blue_label.grid(row=8, column=0)
    yellow_label.grid(row=10, column=0)
    green_label.grid(row=9, column=0)
    red_label.grid(row=11, column=0)

    color_button["command"]=lambda: handle_color_button(color_entry, mqtt_sender)
    find_object_button["command"]=lambda: handle_find_object_button2(speed_entry ,mqtt_sender)
    line_following_button["command"]=lambda: handle_line_following_button(mqtt_sender)

    return frame

def grid_my_frames(sprint_3_frame):
    sprint_3_frame.grid(row=0, column=0)


def get_my_frames(frame, mqtt_sender):
    sprint_3 = sprint_3_frame(frame, mqtt_sender)

    return sprint_3

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
def handle_drive_and_tone_button(initial_tone, tone_rate, speed, mqtt_sender):
    print("Driving toward an object while the tone maker increases frequency as the robot gets closer", [initial_tone.get(), tone_rate.get(), speed.get()])
    mqtt_sender.send_message("m2_proximity", [initial_tone.get(), tone_rate.get(), speed.get()])

def handle_find_object_button(direction, speed, mqtt_sender):
    print("Points straight to the object", [direction.get(), speed.get()])
    mqtt_sender.send_message("m2_camera", [direction.get(), speed.get(), 50, 25])

def handle_color_button(color, mqtt_sender):
    print("Finds the given color", [color.get()])
    mqtt_sender.send_message("m2_color", [color.get()])

def handle_find_object_button2(speed, mqtt_sender):
    print("Finds the object", [speed.get()])
    mqtt_sender.send_message("m2_find_object", [speed.get()])

def handle_line_following_button(mqtt_sender):
    print("Follows the line")
    mqtt_sender.send_message("m2_line_following")


main()