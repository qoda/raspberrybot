from django.views import generic

try:
    import raspirobotboard
except ImportError:
    from raspberrybot import fake_raspirobotboard as raspirobotboard

from raspberrybot.decorators import json_response


VALID_DIRECTION_COMMANDS = ['forward', 'reverse', 'stop', 'left', 'right']


class CommandView(generic.View):
    """
    Execute the command via gpio.
    """
    @json_response
    def get(self, request, *args, **kwargs):
        direction = kwargs.get('cmd')
        success = direction in VALID_DIRECTION_COMMANDS

        if success:
            robot_control = raspirobotboard.RaspiRobot()
            getattr(robot_control, direction)()

        return {
            'success': success,
            'direction': direction
        }

command = CommandView.as_view()
