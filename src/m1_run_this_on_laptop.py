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
    #teleop_frame, arm_frame, control_frame, drive_system_frame,sound_frame,proximity_frame,camera_frame = get_shared_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    find_package_frame,deliver_package_frame, steal_package = get_my_frames(main_frame,mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    #grid_frames(teleop_frame, arm_frame, control_frame, drive_system_frame,sound_frame,proximity_frame,camera_frame)
    grid_my_frames(find_package_frame,deliver_package_frame,steal_package)

    # -------------------------------------------------------------------------
    # Using the keyboard to move the robot
    # -------------------------------------------------------------------------
    root.bind_all('<Key-a>', lambda event: go_left(mqtt_sender))
    root.bind_all('<Key-d>', lambda event: go_right(mqtt_sender))
    root.bind_all('<Key-s>', lambda event: go_backward(mqtt_sender))
    root.bind_all('<Key-w>', lambda event: go_forward(mqtt_sender))
    root.bind_all('<Key-c>', lambda event: calibrate_claw(mqtt_sender))
    root.bind_all('<Key-e>', lambda event: raise_claw(mqtt_sender))
    root.bind_all('<Key-q>', lambda event: lower_claw(mqtt_sender))
    root.bind_all('<Key-space>', lambda event: stop_robot(mqtt_sender))



    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()

#PHASE 1 AND 2
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
    drive_and_beep_button["command"] = lambda: handle_proximity(initial_beep_rate_entry, beep_rate_increase_entry, mqtt_sender)

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
    find_object_button["command"] = lambda: handle_spin_to_find_object(direction_entry, speed_entry, mqtt_sender)

    return frame

# -----------------------------------------------------------------------------
# Handle Functions
# -----------------------------------------------------------------------------
def handle_proximity(initial_beep_rate_entry,beep_rate_increase_entry,mqtt_sender):
    print("Proximity Beeping and Booping (Initial rate - Increase): (",initial_beep_rate_entry,"-",beep_rate_increase_entry,")")
    mqtt_sender.send_message("m1_proximity",[initial_beep_rate_entry.get(),beep_rate_increase_entry.get()])

def handle_spin_to_find_object(direction_entry,speed_entry,mqtt_sender):
    print("Spinning to find object",direction_entry,speed_entry)
    mqtt_sender.send_message("m1_camera",[direction_entry.get(),speed_entry.get(),1,2])

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# PHASE 3
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Frames
# -----------------------------------------------------------------------------
def find_package_frame(window, mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Package Finder")
    speed_label = ttk.Label(frame,text="Speed")
    speed_entry = ttk.Entry(frame,width=8)
    button = ttk.Button(frame,text="Find package!")

    frame_label.grid(row=0,column=0)
    speed_label.grid(row=1,column=0)
    speed_entry.grid(row=2,column=0)
    button.grid(row=3,column=0)

    #Lambda command
    button["command"] = lambda: handle_find_package(speed_entry, mqtt_sender)



    return frame

def package_delivery_frame(window,mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Package Delivery")
    house_choice_label = ttk.Label(frame,text="Who's house would you like to deliver to?")
    greeting_label = ttk.Label(frame,text="Greeting:")
    greeting_entry = ttk.Entry(frame,width=18)
    goodbye_label = ttk.Label(frame,text="Goodbye:")
    goodbye_entry = ttk.Entry(frame,width=18)
    deliver_button = ttk.Button(frame,text="Deliver package!")

    #Setting up the Radio Frame
    radio_frame = ttk.Frame(frame, borderwidth=10, relief='groove')
    house1 = ttk.Radiobutton(radio_frame, text='John',
                             value=3)
    house2 = ttk.Radiobutton(radio_frame, text='Joe',
                             value=4)
    house3 = ttk.Radiobutton(radio_frame, text='Brad',
                             value=5)
    house4 = ttk.Radiobutton(radio_frame, text='Cooper',
                             value=2)
    house1.grid(row=0,column=0)
    house2.grid(row=0, column=1)
    house3.grid(row=0, column=2)
    house4.grid(row=0, column=3)
    radio_observer = tkinter.IntVar()
    for radio in [house1, house2, house3, house4]:
        radio['variable'] = radio_observer



    #Gridding everything
    frame_label.grid(row=0,column=1)
    house_choice_label.grid(row=1,column=1)
    radio_frame.grid(row=2,column=1)
    greeting_label.grid(row=1,column=0)
    greeting_entry.grid(row=2,column=0)
    goodbye_label.grid(row=1,column=2)
    goodbye_entry.grid(row=2,column=2)
    deliver_button.grid(row=3,column=1)


    #Lambda command
    deliver_button["command"] = lambda: handle_delivery(radio_observer,greeting_entry,goodbye_entry,mqtt_sender)
    return frame

def steal_package_frame(window,mqtt_sender):
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()


    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Package Stealer")
    house_choice_label = ttk.Label(frame, text="Who's house would you steal from?")
    laugh_label = ttk.Label(frame,text="Pick your evil laugh:")
    steal_button = ttk.Button(frame,text="Steal package!")
    # Setting up the Radio Frame for house choice
    radio_frame = ttk.Frame(frame, borderwidth=10, relief='groove')
    house1 = ttk.Radiobutton(radio_frame, text='John',
                             value=3)
    house2 = ttk.Radiobutton(radio_frame, text='Joe',
                             value=4)
    house3 = ttk.Radiobutton(radio_frame, text='Brad',
                             value=5)
    house4 = ttk.Radiobutton(radio_frame, text='Cooper',
                             value=2)
    house1.grid(row=0, column=0)
    house2.grid(row=0, column=1)
    house3.grid(row=0, column=2)
    house4.grid(row=0, column=3)
    radio_observer = tkinter.IntVar()
    for radio in [house1, house2, house3, house4]:
        radio['variable'] = radio_observer
    # Setting up the Radio Frame for laugh choice
    radio_frame2 = ttk.Frame(frame, borderwidth=10, relief='groove')
    laugh1 = ttk.Radiobutton(radio_frame2, text='Haha',
                             value='hahahahahahahahaha')
    laugh2 = ttk.Radiobutton(radio_frame2, text='Bwaha',
                             value='bawahahahahahahaha')
    laugh3 = ttk.Radiobutton(radio_frame2, text='Bwahahe',
                             value='bwahahahehehehehehe')
    laugh4 = ttk.Radiobutton(radio_frame2, text="Bwahaheho",
                             value='bwahahahehehehohoho')
    laugh1.grid(row=0, column=0)
    laugh2.grid(row=0, column=1)
    laugh3.grid(row=0, column=2)
    laugh4.grid(row=0, column=3)
    radio_observer2 = tkinter.StringVar()
    for radio in [laugh1, laugh2, laugh3, laugh4]:
        radio['variable'] = radio_observer2


    # Gridding everything
    frame_label.grid(row=0, column=1)
    house_choice_label.grid(row=1,column=0)
    laugh_label.grid(row=1,column=2)
    radio_frame.grid(row=2,column=0)
    radio_frame2.grid(row=2,column=2)
    steal_button.grid(row=2,column=1)

    steal_button["command"] = lambda: handle_theft(radio_observer, radio_observer2, mqtt_sender)

    return frame



# -----------------------------------------------------------------------------
# Handle Functions
# -----------------------------------------------------------------------------
def handle_find_package(speed_entry,mqtt_sender):
    print("Finding package",speed_entry.get())
    mqtt_sender.send_message("m1_find_package",[speed_entry.get()])

def handle_delivery(color,greeting_entry,goodbye_entry,mqtt_sender):
    print("Delivering package!",color.get(),greeting_entry.get,goodbye_entry.get())
    mqtt_sender.send_message("m1_full_delivery",[color.get(),greeting_entry.get(),goodbye_entry.get()])

def handle_theft(color,laugh_entry,mqtt_sender):
    print("Stealing package!",color.get(),laugh_entry.get())
    mqtt_sender.send_message("m1_theft",[color.get(),laugh_entry.get()])

def go_forward(mqtt_sender):
    print("forward")
    mqtt_sender.send_message("forward",[50,50])

def go_backward(mqtt_sender):
    print("backward")
    mqtt_sender.send_message("forward",[-50,-50])

def go_right(mqtt_sender):
    print("right")
    mqtt_sender.send_message("forward",[50,1])
def go_left(mqtt_sender):
    print("left")
    mqtt_sender.send_message("forward",[1,50])
def raise_claw(mqtt_sender):
    print("Raise claw!")
    mqtt_sender.send_message("raise_arm")
def lower_claw(mqtt_sender):
    print("Lower Arm")
    mqtt_sender.send_message("lower_arm")
def stop_robot(mqtt_sender):
    print("Stop")
    mqtt_sender.send_message("stop")
def calibrate_claw(mqtt_sender):
    print("Calibrate Arm")
    mqtt_sender.send_message("calibrate_arm")
# -----------------------------------------------------------------------------
# Get and Grid My Frames
# -----------------------------------------------------------------------------
def get_my_frames(main_frame, mqtt_sender):
    find_package = find_package_frame(main_frame,mqtt_sender)
    deliver_package = package_delivery_frame(main_frame,mqtt_sender)
    steal_package = steal_package_frame(main_frame,mqtt_sender)

    return find_package, deliver_package,steal_package

def grid_my_frames(find_package_frame,deliver_package_frame,steal_package_frame):
    find_package_frame.grid(row=0,column=0)
    deliver_package_frame.grid(row=1,column=0)
    steal_package_frame.grid(row=2,column=0)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()