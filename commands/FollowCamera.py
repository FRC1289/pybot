from wpilib.command import Command
from networktables import NetworkTables
import wpilib

class FollowCamera(Command):
    
    def __init__(self, logger):
        super().__init__(name='FollowCamera')

        self.motor = self.getRobot().motor
        self.requires(self.motor)
        self.logger = logger
        self.angle = 0.0
        self.pidOutput = 0.0
        
        NetworkTables.addConnectionListener(self.connectionListener, immediateNotify=True)
        self.smartDashboard = NetworkTables.getTable('SmartDashboard')
        self.smartDashboard.addEntryListener(self.valueChanged)
        
        self.pid = wpilib.PIDController(0.01, 0, 0,
                                        lambda: self.getAngle(),
                                        lambda s: self.motor.setSpeed(s))
        self.pid.setAbsoluteTolerance(0.01)
        self.pid.setSetpoint(0)
        self.pid.setOutputRange(-1.0, 1.0)
        
    def getAngle(self):
        return self.angle
        
    def initialize(self):
        self.motor.setSpeed(0)
        self.pid.reset()
        self.pid.enable()
        
    def execute(self):
        self.logger.info('angle %0.2f' % self.angle)
        pass
        
    def isFinished(self):
        return False
     
    def end(self):
        self.motor.setSpeed(0)
        self.pid.disable()
        pass
        
    def valueChanged(self, table, key, value, isNew):
        if key == 'cameraAngle':
            self.angle = value
        
    def connectionListener(self, connected, info):
        print(info, connected)