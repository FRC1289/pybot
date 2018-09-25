import wpilib
from wpilib.command.subsystem import Subsystem
import robotmap

class Breaker(Subsystem):
    '''
    This example controls a single digital input device
    '''

    def __init__(self):
        '''Instantiates the breaker object.'''

        super().__init__('Breaker')

        self.breaker = wpilib.DigitalInput(robotmap.DIO_breaker)


    def isOpen(self):
        return breaker.get()

