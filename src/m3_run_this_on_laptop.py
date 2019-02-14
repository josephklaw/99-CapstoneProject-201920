# """
#   Capstone Project.  Code to run on a LAPTOP (NOT the robot).
#   Displays the Graphical User Interface (GUI) and communicates with the robot.
#
#   Authors:  Your professors (for the framework)
#     and Aaryan Khatri.
#   Winter term, 2018-2019.
# """
#
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
    root.title("CSSE 120 Capstone Project 2018-19")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------

    teleop, arm, control, drive, sound, proximity, camera = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop, arm, control, drive, sound, proximity, camera)

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
    camera = camera_frame(main_frame, mqtt_sender)

    return teleop, arm, control, drive, sound, proximity, camera




def grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame, sound_frame, proximity_frame, camera_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_system_frame.grid(row=3,column=0)
    sound_frame.grid(row=0,column=1)
    proximity_frame.grid(row=2, column=1)
    camera_frame.grid(row=3, column=1)


def proximity_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label0 = ttk.Label(frame, text='LED Pick up')
    frame_label1 = ttk.Label(frame, text="Initial: ")
    frame_label2 = ttk.Label(frame, text="Rate of Increase: ")
    initial_entry = ttk.Entry(frame, width=8)
    rate_of_increase_entry = ttk.Entry(frame, width=8)
    go_button = ttk.Button(frame, text='Go')

    # Grid the widgets:
    frame_label0.grid(row=0, column=2)
    frame_label1.grid(row=1, column=0)
    frame_label2.grid(row=1, column=2)
    initial_entry.grid(row=1, column=1)
    rate_of_increase_entry.grid(row=1, column=3)
    go_button.grid(row=1, column=5)

    # Set the Button callbacks:
    go_button["command"] = lambda: handle_go_button(initial_entry, rate_of_increase_entry,
                                                                        mqtt_sender)

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

    find_object_button["command"]=lambda: handle_find_object_button(direction_entry, speed_entry, mqtt_sender)

    return frame


def handle_go_button(initial_entry, rate_of_increase_entry, mqtt_sender):
    print("Driving toward an object while the LED increases frequency as the robot gets closer", [initial_entry.get(), rate_of_increase_entry.get()])
    mqtt_sender.send_message("m3_proximity", [initial_entry.get(), rate_of_increase_entry.get()])



# # -----------------------------------------------------------------------------
# # Calls  main  to start the ball rolling.
# # -----------------------------------------------------------------------------
main()