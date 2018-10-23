from wpilib.command import Command
from networktables import NetworkTables

class FollowCamera(Command):
    
    def __init__(self, logger):
        super().__init__('Follow camera')

        self.motor = self.getRobot().motor
        self.requires(self.motor)
        self.logger = logger
        self.angle = 0.0
        
        NetworkTables.addConnectionListener(self.connectionListener, immediateNotify=True)
        self.smartDashboard = NetworkTables.getTable('SmartDashboard')
        self.smartDashboard.addEntryListener(self.valueChanged)
        
        
        
    def initialize(self):
        self.motor.setSpeed(0)
        
    def execute(self):
        print('angle', self.angle)
        
    def isFinished(self):
        return False
     
    def end(self):
        pass
        
    def valueChanged(self, table, key, value, isNew):
        if key == 'cameraAngle':
            self.angle = value
        
    def connectionListener(self, connected, info):
        print(info, connected)