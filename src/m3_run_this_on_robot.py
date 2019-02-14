"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Aaryan Khatri.
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
    run_test_arm()
    run_calibrate_arm()
    real_thing()
    #led_proximity_sensor()
    #led()
    #c



def run_test_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()

def run_calibrate_arm():
    robot = rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

def real_thing():
    robot = rosebot.RoseBot()
    delegate_that_receives = shared_gui_delegate_on_robot.DelegateThatReceives(robot)
    mqtt_receiver = com.MqttClient(delegate_that_receives)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate_that_receives.is_time_to_stop:
            break

def m3_led_proximity_sensor(initial, rate_of_increase):
    robot = rosebot.RoseBot()
    seconds = float(initial)
    threshold = 20
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()
    robot.arm_and_claw.calibrate_arm()
    robot.drive_system.go(50, 50)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        print(distance)
        # Led Cycle
        robot.led_system.left_led.turn_on()
        time.sleep(secs / 4)
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_on()
        time.sleep(secs / 4)
        robot.led_system.right_led.turn_off()
        robot.led_system.left_led.turn_on()
        robot.led_system.right_led.turn_on()
        time.sleep(secs / 4)
        robot.led_system.left_led.turn_off()
        robot.led_system.right_led.turn_off()
        time.sleep(secs / 4)
        if distance < threshold:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
        increment = float(initial)/float(rate_of_increase)
        sub = 100/increment
        pos = 100 - distance
        x = pos/sub
        secs = initial - (float(rate_of_increase) * x)
        if secs < 0:
            secs = 0


def led_test():
    while True:
        robot = rosebot.RoseBot()
        robot.led_system.left_led.turn_on()
        time.sleep(3)
        robot.led_system.left_led.turn_off()
        time.sleep(3)
        robot.led_system.right_led.turn_on()
        time.sleep(3)
        robot.led_system.right_led.turn_off()
        time.sleep(3)


def m3_chose_pick_up(initial, rate_of_increase, direction, speed, area, string):
    robot = rosebot.RoseBot()
    if direction == 'Clockwise':
        robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    elif direction == 'Counterclockwise':
        robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)
    time.sleep(3)
    if string == 'LED':
        m3_led_proximity_sensor(initial, rate_of_increase)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()