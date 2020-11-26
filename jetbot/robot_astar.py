from traitlets.config.configurable import SingletonConfigurable, Configurable
import traitlets
import atexit
import logging
from jetbot import AStar


class RobotAStar(SingletonConfigurable):
    a_star = AStar()

    def __init__(self, *args, **kwargs):
        super(RobotAStar, self).__init__(*args, **kwargs)

    def set_motors(self, left_speed, right_speed):
        self.a_star.motors(int(min(left_speed, 1) * 400), int(min(right_speed, 1) * 400))
        
    def forward(self, speed=1.0, duration=None):
        self.set_motors(speed, speed)

    def backward(self, speed=1.0):
        self.set_motors(-speed, -speed)

    def left(self, speed=1.0):
        self.set_motors(-speed, speed)

    def right(self, speed=1.0):
        self.set_motors(speed, -speed)

    def stop(self):
        self.set_motors(0, 0)


class MotorSpeed(Configurable):

    l_value = traitlets.Float()
    r_value = traitlets.Float()

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    def __init__(self, astar, *args, **kwargs):
        super(MotorSpeed, self).__init__(*args, **kwargs)  # initializes traitlets
        self._astar = astar

        atexit.register(self._release)

    @traitlets.observe('l_value')
    def _observe_value(self, change):
        logging.info("Updating l_value: " + str(change['new']) + " using existing r_value: " + str(self.r_value))
        self._write_value(change['new'], self.r_value)

    @traitlets.observe('r_value')
    def _observe_value(self, change):
        logging.info("Updating r_value: " + str(change['new']) + " using existing l_value: " + str(self.l_value))
        self._write_value(self.l_value, change['new'])

    def _write_value(self, left_speed, right_speed):
        self._astar.motors(int(min(left_speed, 1) * 400), int(min(right_speed, 1) * 400))

    def _release(self):
        """Stops motor by releasing control"""
        self._write_value(0, 0)


class RobotAStarWithTrait(SingletonConfigurable):
    motor_speed = traitlets.Instance(MotorSpeed)
    a_star = AStar()

    def __init__(self, *args, **kwargs):
        super(RobotAStarWithTrait, self).__init__(*args, **kwargs)
        self.motor_speed = MotorSpeed(self.a_star)

    def forward(self, speed=1.0, duration=None):
        self.set_motors(speed, speed)

    def backward(self, speed=1.0):
        self.set_motors(-speed, -speed)

    def left(self, speed=1.0):
        self.set_motors(-speed, speed)

    def right(self, speed=1.0):
        self.set_motors(speed, -speed)

    def stop(self):
        self.set_motors(0, 0)

    def set_motors(self, left_speed, right_speed):
        self.a_star.motors(int(min(left_speed, 1) * 400), int(min(right_speed, 1) * 400))