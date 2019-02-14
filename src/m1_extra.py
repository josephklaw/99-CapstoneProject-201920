import shared_gui_delegate_on_robot
import time
import rosebot
import ev3dev.ev3 as ev3

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
def spin_to_find_object(direction,speed,robot):
    """:type  robot: rosebot.RoseBot"""
    pixy = ev3.Sensor(driver_name="pixy-lego")
    pixy.mode = "SIG1"
    if direction == "CCW":
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed),pixy.value(3)*pixy.value(4))
    if direction == "CW":
        robot.drive_system.spin_clockwise_until_sees_object(int(speed),pixy.value(3)*pixy.value(4))
    #     robot.drive_system.go(-50,50)
    #     while True:
    #         time.sleep(0.01)
    #         if robot.sensor_system.camera. :
    #             break
    # elif direction == "CW":
    #     robot.drive_system.go(50,-50)
    #     while True:
    #         time.sleep(0.01)
    #         if robot.sensor_system.camera.:
    #             break
