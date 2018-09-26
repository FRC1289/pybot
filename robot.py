#!/usr/bin/env python3

import wpilib
from wpilib.command import Command
from commandbased import CommandBasedRobot

from subsystems import singlemotor
from subsystems import breaker
import oi
from commands.autonomous import AutonomousProgram
from commands.followjoystick import FollowJoystick

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

        self.autonomousProgram = AutonomousProgram()
        self.teleopProgram = FollowJoystick()
        
        '''
        Since OI instantiates commands and commands need access to subsystems,
        OI must be initialized after subsystems.
        '''
        self.joystick = oi.getJoystick()

        wpilib.CameraServier.launch('vision.py:main')


    def autonomousInit(self):
        '''
        You should call start on your autonomous program here. You can
        instantiate the program here if you like, or in robotInit as in this
        example. You can also use a SendableChooser to have the autonomous
        program chosen from the SmartDashboard.
        '''

        self.autonomousProgram.start()

    def teleopInit(self):
        if self.autonomousProgram is not None:
            self.autonomousProgram.cancel()
            
        self.teleopProgram.start()

if __name__ == '__main__':
    wpilib.run(ExampleBot)
