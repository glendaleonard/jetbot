
from traitlets.config.configurable import SingletonConfigurable
from jetbot import AStar


class RobotAStar(SingletonConfigurable):
    a_star = AStar()

    def __init__(self, *args, **kwargs):
        super(RobotAStar, self).__init__(*args, **kwargs)

    def set_motors(self, left_speed, right_speed):
        self.a_star.motors(min(left_speed, 1) * 400, min(right_speed, 1) * 400)
        
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
