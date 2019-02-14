# """
#   Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
#   Author:  Your professors (for the framework)
#     and Aaryan Khatri.
#   Winter term, 2018-2019.
# """
#
import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot
#
def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # run_test_arm()
    # run_calibrate_arm()
    # real_thing()
    increasing_rate_led(initial, rate_of_increase, robot)
    led_pattern()



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


def increasing_rate_led(initial, rate_of_increase, robot):
    robot.drive_system.go(50, 50)
    robot.drive_system.left_motor.reset_position()
    prev_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    prev_time = time.time()
    rate = initial
    delta = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() / ((robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() - 0.01) / rate_of_increase)
    while True:
        if robot.drive_system.left_motor.get_position() - prev_distance >= delta:
            if time.time() - prev_time >= rate:
                prev_distance = robot.drive_system.left_motor.get_position()
                prev_time, rate = led_pattern(initial, rate_of_increase, robot)

        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 1:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break

def led_pattern(initial, rate_of_increase, robot):
    robot.led_system.left_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_on()
    robot.led_system.right_led.turn_off()
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()
    return time.time(), initial - rate_of_increase

#
# # -----------------------------------------------------------------------------
# # Calls  main  to start the ball rolling.
# # -----------------------------------------------------------------------------
main()