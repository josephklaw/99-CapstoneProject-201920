"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Joseph Law, Aaryan Khatri, and Lucas D'Alesio.
  Winter term, 2018-2019.
"""
import m1_extra as m1
import m2_extra as m2
import m3_extra as m3

class DelegateThatReceives(object):
    def __init__(self,robot):
        """:type  robot: rosebot.RoseBot"""
        self.robot = robot
        self.is_time_to_stop = False
    def forward(self,left_wheel_speed,right_wheel_speed):
        self.robot.drive_system.go(int(left_wheel_speed),
                                   int(right_wheel_speed))
    def stop(self):
        self.robot.drive_system.stop()
    def raise_arm(self):
        self.robot.arm_and_claw.raise_arm()
    def lower_arm(self):
        self.robot.arm_and_claw.lower_arm()
    def calibrate_arm(self):
        self.robot.arm_and_claw.calibrate_arm()
    def move_arm_to_position(self,desired_position):
        self.robot.arm_and_claw.move_arm_to_position(desired_position)
    def is_quit(self):
        print("Got quit")
        self.is_time_to_stop = True
    def drive_forward_for_time(self,time,speed):
        self.robot.drive_system.go_straight_for_seconds(time,speed)
    def drive_forward_for_inches_time(self,inches):
        self.robot.drive_system.go_straight_for_inches_using_time(inches)
    def drive_forward_for_inches_sensor(self,inches,speed):
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches,speed)
    def sound_beep(self,beeps):
        for k in range(int(beeps)):
            self.robot.sound_system.beeper.beep().wait()
    def sound_tone(self,frequency,duration):
        self.robot.sound_system.tone_maker.play_tone(frequency,duration)
    def sound_speak(self,message):
        self.robot.sound_system.speech_maker.speak(message)
    def go_straight_until_intensity_is_greater_than(self,intensity,speed):
        self.robot.drive_system.go_straight_until_intensity_is_greater_than(intensity,speed)
    def go_straight_until_intensity_is_less_than(self,intensity,speed):
        self.robot.drive_system.go_straight_until_intensity_is_less_than(intensity,speed)
    def go_straight_until_color_is(self,color,speed):
        self.robot.drive_system.go_straight_until_color_is(color,speed)
    def go_straight_until_color_is_not(self,color,speed):
        self.robot.drive_system.go_straight_until_color_is_not(color,speed)

    def spin_clockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_clockwise_until_sees_object(speed, area)

    def spin_counterclockwise_until_sees_object(self, speed, area):
        self.robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)

    def display_camera_data(self):
        self.robot.drive_system.display_camera_data()

    def spin_clockwise_until_beacon_heading_is_nonnegative(self, speed):
        self.robot.drive_system.spin_clockwise_until_beacon_heading_is_nonnegative(speed)

    def spin_counterclockwise_until_beacon_heading_is_nonpositive(self, speed):
        self.robot.drive_system.spin_counterclockwise_until_beacon_heading_is_nonpositive(speed)

    def go_straight_to_the_beacon(self, inches, speed):
        self.robot.drive_system.go_straight_to_the_beacon(speed, inches)


    def go_forward_until_distance_is_less_than(self, inches, speed):
        self.robot.drive_system.go_forward_until_distance_is_less_than(inches, speed)

    def go_backward_until_distance_is_greater_than(self, inches, speed):
        self.robot.drive_system.go_backward_until_distance_is_greater_than(inches, speed)

    def go_until_distance_is_within(self, delta, inches, speed):
        self.robot.drive_system.go_until_distance_is_within(delta, inches, speed)

    def m1_proximity(self,initial_beep_rate,beep_rate_increase):
        m1.increasing_rate_of_beep(initial_beep_rate,beep_rate_increase,self.robot)

    def m1_camera(self,direction,speed,initial_beep_rate,beep_rate_increase):
        m1.spin_to_find_object(direction,speed,initial_beep_rate,beep_rate_increase,self.robot)
    def m2_proximity(self, initial_tone, tone_rate_increase, speed):
        m2.increasing_tone(float(initial_tone), float(tone_rate_increase), int(speed), self.robot)

    def m2_camera(self, direction, speed, initial_tone, tone_rate_increase):
        m2.point_to_object(str(direction), int(speed), int(initial_tone), int(tone_rate_increase), self.robot)

    def m3_proximity(self, initial, rate_of_increase):
        m3.increasing_rate_led(initial, rate_of_increase, self.robot)

    def m3_camera(self, speed, direction, initial, rate_of_increase):
        m3.camera(int(speed), str(direction), int(initial), int(rate_of_increase), self.robot)


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# Joe's Sprint 3 Functions
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
    def m1_find_package(self,speed):
        m1.spin_to_find_package(speed,self.robot)
    def m1_full_delivery(self,color,greeting,goodbye):
        m1.full_delivery(color,greeting,goodbye,self.robot)
    def m1_theft(self,color,laugh):
        m1.steal_package(color,laugh,self.robot)


#Lucas' Sprint 3 Functions

    def m2_color(self, color):
        m2.color_finder(color, self.robot)

    def m2_find_object(self, speed):
        m2.find_object(speed, self.robot)

    def m2_line_following(self):
        m2.line_following(self.robot)

