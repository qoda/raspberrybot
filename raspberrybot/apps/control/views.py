from django.views import generic

try:
    import raspirobotboard
except ImportError:
    from raspberrybot import fake_raspirobotboard as raspirobotboard

from raspberrybot.decorators import json_response


VALID_COMMANDS = ['forward', 'reverse', 'stop', 'left', 'right']


class CommandView(generic.View):
    """
    Execute the command via gpio.
    """
    @json_response
    def post(self, request, *args, **kwargs):
        direction = kwargs.get('direction')
        success = direction in VALID_COMMANDS

        if success:
            robot_control = raspirobotboard.RaspiRobot()
            getattr(robot_control, self.command)()

        return {
            'success': success,
            'direction': direction
        }

command = CommandView.as_view()
