"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Joseph Law.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_thing()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
def real_thing():
    robot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate_that_receives.is_time_to_stop:
            break

def increasing_rate_of_beep(rate_of_beep,rate_of_beep_increase,robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(100,100)
    og_rate_of_beep = rate_of_beep
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        time.sleep(og_rate_of_beep - (rate_of_beep_increase/distance))
        robot.sound_system.beeper.beep().wait()
        if distance <= 5:
            break
    robot.drive_system.stop()
def spin_to_find_object(direction,robot):
    """:type  robot: rosebot.RoseBot"""
    if direction == "CCW":
        robot.drive_system.go(-50,50)
        while True:
            time.sleep(0.01)
            if robot.sensor_system.camera. :
                break
    elif direction == "CW":
        robot.drive_system.go(50,-50)
        while True:
            time.sleep(0.01)
            if robot.sensor_system.camera.:
                break
main()