"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Joseph Law, Aaryan Khatri, and Lucas D'Alesio.
  Winter term, 2018-2019.
"""

class DelegateThatReceives(object):
    def __init__(self,robot):
        """:type  robot: rosebot.RoseBot"""
        self.robot = robot

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
    def drive_forward_for_time(self,time):
        self.robot.drive_system.go_straight_for_seconds(time,100)
    def drive_forward_for_inches_time(self,inches):
        self.robot.drive_system.go_straight_for_inches_using_time(inches)
    def drive_forward_for_inches_sensor(self,inches):
        self.robot.drive_system.go_straight_for_inches_using_encoder(inches)
    def sound_beep(self,beeps):
        for k in range(beeps):
            self.robot.sound_system.beeper.beep()
    # def sound_tone(self,frequency,duration):
    #     self.robot.sound_system.tone_maker(frequency,duration)