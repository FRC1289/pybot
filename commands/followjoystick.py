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
        self.motor.setSpeed(self.getRobot().joystick.getY())

    def isFinished(self):
        return false

    def end(self):
        self.motor.setSpeed(0)
