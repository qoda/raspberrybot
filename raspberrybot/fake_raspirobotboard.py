

class RaspiRobot(object):
    """
    Fake RaspiRobot class for testing on non RPi systems.
    """
    def __init__(self):
        for direction in ['forward', 'reverse', 'stop', 'left', 'right']:
            self.__setattr__(direction, lambda direction: direction)
