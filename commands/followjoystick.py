from wpilib.command import Command

class FollowJoystick(Command):
    '''
    This command will read the joystick's y axis and use that value to control
    the speed of the SingleMotor subsystem.
    '''

    def __init__(self):
        super().__init__('Follow Joystick')

        self.motor = self.getRobot().motor
        self.requires(self.motor)
        


    def initialize(self):
        self.motor.setSpeed(0)

    def execute(self):
        current_speed = self.getRobot().joystick.getY()
        self.motor.setSpeed(current_speed)
    

    def isFinished(self):
        if self.getRobot().joystick.getRawButton(1):
            return True
        else:
            return False

    def end(self):
        self.motor.setSpeed(0)
