import shared_gui_delegate_on_robot
import time
import rosebot
import ev3dev.ev3 as ev3

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
        led_pattern()

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