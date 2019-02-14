"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Lucas D'Alesio.
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

def increasing_tone(initial_tone, tone_rate_increase, speed, robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(speed, speed)
    starting_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        new_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if new_distance < starting_distance:
            initial_tone = initial_tone * tone_rate_increase
            starting_distance = new_distance
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 2:
            break
        robot.sound_system.tone_maker.play_tone(tone_rate_increase, 150)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()







main()