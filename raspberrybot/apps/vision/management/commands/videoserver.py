from django.core.management.base import BaseCommand

from raspberrybot.apps.vision import utils


class Command(BaseCommand):
    args = ''
    help = "Start the video stream."

    def handle(self, *args, **options):
        host = options.get('host', '0.0.0.0')
        port = options.get('port', '8090')
        host_camera = options.get('host_camera', 0)

        # start the stream
        utils.start_camera(host_camera, host, port)
