'''
Created on Sep 25, 2018

@author: LHS
'''
from wpilib.command import Command
from commands.Enumerations import RotationalDirection

class RunWithSwitch(Command):
    '''
    This command will read run while the switch is closed
    '''

    def __init__(self, direction, speed, logger):
        super().__init__('RunWithSwitch')
        self.motor = self.getRobot().motor
        self.breaker = self.getRobot().breaker
        self.requires(self.motor)
        self.requires(self.breaker)
        
        self.speed = speed
        self.direction = direction
        self.isCovered = False # starting state
        self.done = False
        self.logger = logger


    def initialize(self):
        self.logger.info('rws init %f %s, %d' % (self.speed, self.direction.name, self.breaker.isClosed()))
        if self.direction is RotationalDirection.CCW:
            self.speed = - self.speed
        self.motor.setSpeed(self.speed)

    def execute(self):
        if self.isCovered:
            if not self.breaker.isClosed():
                #self.logger.info('isCovered and breaker not closed')
                self.isCovered = False
                self.done = True
        else:
            if self.breaker.isClosed():
                #self.logger.info('not isCovered and breaker closed')
                self.motor.setSpeed(0)
                self.isCovered = True

    def isFinished(self):
        return self.done

    def end(self):
        self.motor.setSpeed(0)
