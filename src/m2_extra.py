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