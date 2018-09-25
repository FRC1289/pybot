'''
Created on Sep 25, 2018

@author: LHS
'''
from wpilib.command import Command

class RunWithSwitch(Command):
    '''
    This command will read run while the switch is closed
    '''

    def __init__(self):
        super().__init__('RunWithSwitch')

        self.motor = self.getRobot().motor
        self.breaker = self.getRobot().breaker
        self.requires(self.motor)
        self.requires(self.breaker)
            


    def initialize(self):
        self.motor.setSpeed(0)

    def execute(self):
        if self.breaker.isOpen():
            self.motor.setSpeed(.5)
        else:
            self.motor.setSpeed(0)

    def isFinished(self):
        return False

    def end(self):
        self.motor.setSpeed(0)
