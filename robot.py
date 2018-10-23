#!/usr/bin/env python3

import wpilib
from wpilib.command import Command, Scheduler
from commandbased import CommandBasedRobot

from subsystems import singlemotor
from subsystems import breaker
import oi
from commands.autonomous import AutonomousProgram
from commands.followjoystick import FollowJoystick
from commands.RunWithSwitch import RunWithSwitch
from commands.FollowCamera import FollowCamera
from commands.CW_CCW import CW_CCW

class ExampleBot(CommandBasedRobot):
    '''
    The CommandBasedRobot base class implements almost everything you need for
    a working robot program. All you need to do is set up the subsystems and
    commands. You do not need to override the "periodic" functions, as they
    will automatically call the scheduler. You may override the "init" functions
    if you want to do anything special when the mode changes.
    '''

    def robotInit(self):
        '''
        Subsystem, Command, OperatorInterface Instantiation
        IN THAT ORDER
        '''

        Command.getRobot = lambda x=0: self
        self.motor = singlemotor.SingleMotor()
        self.breaker = breaker.Breaker()

        self.autonomousProgram = FollowCamera(self.logger)
        self.teleopProgram = CW_CCW(self.logger)
        
        '''
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        '''
        self.joystick = oi.getJoystick()

    def autonomousInit(self):
        self.autonomousProgram.start()
        
    #def autonomousPeriodic(self):
        #Scheduler.getInstance().run()
        

    def teleopInit(self):
        if self.autonomousProgram is not None:
            self.autonomousProgram.cancel()
            
        self.teleopProgram.start()
        
    def teleopPeriodic(self):
        Scheduler.getInstance().run()
        if self.teleopProgram.isFinished():
            #self.logger.info('finished')
            self.teleopProgram = CW_CCW(self.logger)
            self.teleopProgram.start()

if __name__ == '__main__':
    wpilib.run(ExampleBot)
