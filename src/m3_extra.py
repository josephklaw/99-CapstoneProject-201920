import shared_gui_delegate_on_robot
import time
import rosebot
import ev3dev.ev3 as ev3

def increasing_rate_led (initial, rate_of_increase, robot):

    print(initial, rate_of_increase)
    robot.drive_system.go(50, 50)
    cnt = 0
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() > 15:
            if cnt % float(initial) == 0:
                led_pattern(initial, rate_of_increase, robot)
                cnt = 0
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() >= 2.6:
            if cnt % float(rate_of_increase) == 0:
                led_pattern(initial, rate_of_increase, robot)
                cnt = 0
            cnt = cnt + .5
        elif robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <= 2.5:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            break
        cnt = cnt + .5


def led_pattern(initial, rate_of_increase, robot):
    robot.led_system.left_led.turn_on()
    time.sleep(0.25)
    robot.led_system.left_led.turn_off()
    time.sleep(0.25)
    robot.led_system.right_led.turn_on()
    time.sleep(0.25)
    robot.led_system.right_led.turn_off()
    time.sleep(0.25)
    robot.led_system.left_led.turn_on()
    robot.led_system.right_led.turn_on()
    time.sleep(0.25)
    robot.led_system.left_led.turn_off()
    robot.led_system.right_led.turn_off()
    time.sleep(0.25)


def camera(speed, direction, robot):
    if direction == "clockwise":
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), 50)
        robot.drive_system.left_motor.turn_on(-50)
        robot.drive_system.right_motor.turn_on(50)
        time.sleep(.07)
    elif direction == "counterclockwise":
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), 50)
        robot.drive_system.left_motor.turn_on(50)
        robot.drive_system.right_motor.turn_on(-50)
        time.sleep(.07)
    increasing_rate_led(5, .05, robot)