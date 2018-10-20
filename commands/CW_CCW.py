from wpilib.command.commandgroup import CommandGroup

from commands.Enumerations import RotationalDirection
from commands.RunWithSwitch import RunWithSwitch

class CW_CCW(CommandGroup):
    '''
    A simple program that spins the motor for in one direction
    Then spins it in the other direction
    '''

    def __init__(self, logger):
        super().__init__('RunWithSwitch')
        self.addSequential(RunWithSwitch(RotationalDirection.CW, 0.05, logger))
        self.addSequential(RunWithSwitch(RotationalDirection.CCW, 0.05, logger))
        
