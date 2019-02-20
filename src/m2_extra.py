import ev3dev.ev3 as ev3
import rosebot as robot

def increasing_tone(initial_tone, tone_rate_increase, speed, robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(speed, speed)
    starting_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    while True:
        new_distance = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()

        if new_distance < starting_distance:
            initial_tone = initial_tone + tone_rate_increase
            starting_distance = new_distance
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 1:
            break
        robot.sound_system.tone_maker.play_tone(initial_tone, 150)
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()


def point_to_object(direction, speed, initial_tone, tone_rate_increase, robot):
    """:type  robot: rosebot.RoseBot"""
    p = ev3.Sensor(driver_name="pixy-lego")
    p.mode = "SIG1"
    if direction == "CCW":
        robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), p.value(3) * p.value(4))
    if direction == "CW":
        robot.drive_system.spin_clockwise_until_sees_object(int(speed), p.value(3) * p.value(4))
    increasing_tone(initial_tone, tone_rate_increase, speed, robot)





#Sprint 3 Functions


def color_finder(color, robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(75, 75)
    while True:
        if robot.sensor_system.color_sensor.get_color() == int(color):
            robot.drive_system.stop()
            robot.sound_system.speech_maker.speak("I found the color")
            print(robot.sensor_system.color_sensor.get_color())
            break

def find_object(speed, robot):
    """:type  robot: rosebot.RoseBot"""
    p = ev3.Sensor(driver_name="pixy-lego")
    p.mode = "SIG1"
    robot.drive_system.go_straight_for_seconds(2, speed)
    robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), p.value(3) * p.value(4))
    robot.drive_system.go(speed, speed)
    while True:
        if robot.sensor_system.ir_proximity_sensor.get_distance_in_inches() < 0.75:
            break
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()


def line_following(robot):
    """:type  robot: rosebot.RoseBot"""
    robot.drive_system.go(50, 50)
    while True:
        if robot.sensor_system.color_sensor.get_color() == 1:
            robot.drive_system.go(50,50)
        if robot.sensor_system.color_sensor.get_color() == 4:
            robot.drive_system.right_motor.turn_on(10)
            robot.drive_system.left_motor.turn_on(50)
        if robot.sensor_system.color_sensor.get_color() == 5:
            robot.drive_system.right_motor.turn_on(50)
            robot.drive_system.left_motor.turn_on(10)
        if robot.sensor_system.color_sensor.get_color() == 6:
            robot.drive_system.stop()
            break
    robot.arm_and_claw.lower_arm()






            # # - 1: Black
            # - 2: Blue
            # - 3: Green
            # - 4: Yellow
            # - 5: Red
            # - 6: White
            # - 7: Brown