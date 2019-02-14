import shared_gui_delegate_on_robot
import time
import rosebot

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
# def spin_to_find_object(direction,robot):
#     """:type  robot: rosebot.RoseBot"""
#     if direction == "CCW":
#         robot.drive_system.go(-50,50)
#         while True:
#             time.sleep(0.01)
#             if robot.sensor_system.camera. :
#                 break
#     elif direction == "CW":
#         robot.drive_system.go(50,-50)
#         while True:
#             time.sleep(0.01)
#             if robot.sensor_system.camera.:
#                 break
