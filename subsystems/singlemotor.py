import wpilib
from wpilib.command.subsystem import Subsystem
from ctre import WPI_TalonSRX
import robotmap

class SingleMotor(Subsystem):
    '''
    This example subsystem controls a single Talon in PercentVBus mode.
    '''

    def __init__(self):
        '''Instantiates the motor object.'''

        super().__init__('SingleMotor')

        self.motor = WPI_TalonSRX(robotmap.PWM_motor)


    def setSpeed(self, speed):
        self.motor.set(speed)
