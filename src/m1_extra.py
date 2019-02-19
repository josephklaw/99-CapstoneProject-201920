import shared_gui_delegate_on_robot
import time
import rosebot
import ev3dev.ev3 as ev3


#Sprint 2 Functions
def increasing_rate_of_beep(rate_of_beep,rate_of_beep_increase,robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(20,20)
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        #         # time.sleep(abs(int(og_rate_of_beep) - (int(rate_of_beep_increase)/int(distance))))
        robot.sound_system.beeper.beep().wait()
        if int(distance) <= 20:
            for k in range(20):
                if int(distance) == k:
                    delay = (k * int(rate_of_beep_increase) + int(rate_of_beep))*(1/100)
                    time.sleep(delay)
        else:
            time.sleep(20)
        if distance <= 1:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
def spin_to_find_object(direction,speed,rate_of_beep,rate_of_beep_increase,robot):
    """:type  robot: rosebot.RoseBot"""
    pixy = ev3.Sensor(driver_name="pixy-lego")
    pixy.mode = "SIG1"
    if direction == "CCW":
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed),pixy.value(3)*pixy.value(4))
    if direction == "CW":
        robot.drive_system.spin_clockwise_until_sees_object(int(speed),pixy.value(3)*pixy.value(4))
    increasing_rate_of_beep(rate_of_beep,rate_of_beep_increase,robot)

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Sprint 3 Functions
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
def spin_to_find_package(speed,robot):
    """:type  robot: rosebot.RoseBot"""
    pixy = ev3.Sensor(driver_name="pixy-lego")
    pixy.mode = "SIG1"
    robot.drive_system.spin_clockwise_until_sees_object(int(speed), pixy.value(3) * pixy.value(4))
    robot.drive_system.go(speed, speed)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <=1:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()

def find_road(robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(0,50)
    while True:
        if robot.sensor_system.color_sensor.get_color() == 1:
            break
    time.sleep(0.05)
    robot.drive_system.stop()

def find_house(color,robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(50,50)
    while True:
        #If the color sensor detects the color corresponding to the house
        if robot.sensor_system.color_sensor.get_color() == int(color):
            # If the color is green, the robot turns left
            if int(color) == 3:
                robot.drive_system.stop()
                robot.drive_system.go(0, 50)
                break
            # If the color is yellow, the robot turns right
            if int(color) == 4:
                robot.drive_system.stop()
                robot.drive_system.go(50,0)
                break
            # If the color is red, the robot turns left
            if int(color) == 5:
                robot.drive_system.stop()
                robot.drive_system.go(0, 50)
                break
            # If the color is blue,the robot turns right
            if int(color) == 2:
                robot.drive_system.stop()
                robot.drive_system.go(50,0)
                break
    #Allows for a 90 degree turn
    time.sleep(0.5)
    robot.drive_system.stop()

def deliver_package(greeting,goodbye,robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(50, 50)
    time.sleep(2)
    robot.sound_system.speech_maker(greeting)
    robot.arm_and_claw.lower_arm()
    robot.sound_system.speech_maker(goodbye)
    robot.drive_system.go(-50,-50)

def full_delivery(color,greeting,goodbye,robot):
    find_road(robot)
    find_house(color,robot)
    deliver_package(greeting,goodbye,robot)

def theft(robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(50,50)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() <=1:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    robot.drive_system.go(-50,50)
    time.sleep(2)
    robot.drive_system.stop()
    robot.drive_system.go(-50,50)
    #Allows for a turn
    time.sleep(0.5)

def getaway(laugh,robot):
    robot.drive_system.go(100, 100)
    robot.sound_system.speech_maker(laugh)
    time.sleep(5)
    robot.drive_system.stop()

def steal_package(color,laugh,robot):
    find_house(color,robot)
    theft(robot)
    getaway(laugh,robot)