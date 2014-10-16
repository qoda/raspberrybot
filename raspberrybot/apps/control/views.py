import os

from django.views import generic

try:
    import raspirobotboard
except ImportError:
    from raspberrybot import fake_raspirobotboard as raspirobotboard

from raspberrybot.decorators import json_response


VALID_DIRECTION_COMMANDS = ['forward', 'reverse', 'stop', 'left', 'right']
VALID_SETTING_COMMANDS = ['detect']

DETECT_FILE = "/tmp/.detect"


class CommandView(generic.View):
    """
    Execute the command via gpio.
    """
    @json_response
    def get(self, request, *args, **kwargs):
        cmd = kwargs.get('cmd')
        direction = cmd if cmd in VALID_DIRECTION_COMMANDS else None
        setting = cmd if cmd in VALID_SETTING_COMMANDS else None

        if direction:
            robot_control = raspirobotboard.RaspiRobot()
            getattr(robot_control, direction)()

        if setting:
            if setting == 'detect':
                if os.path.exists(DETECT_FILE):
                    os.remove(DETECT_FILE)
                else:
                    open(DETECT_FILE, 'a').close()

        return {
            'success': any([setting, direction]),
            'direction': direction,
            'setting': setting
        }

command = CommandView.as_view()
