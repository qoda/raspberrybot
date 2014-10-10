import time

from django.core.management.base import BaseCommand

from SimpleCV import Camera, JpegStreamer


class Command(BaseCommand):
    args = ''
    help = "Start the video stream."

    def handle(self, *args, **options):
        host = options.get('host', '0.0.0.0')
        port = options.get('port', '8090')
        width = options.get('width', 640)
        height = options.get('height', 480)
        quality = options.get('quality', 70)
        host_camera = options.get('host_camera', 0)

        # setup the stream
        camera = Camera(host_camera, {"width": width, "height": height})
        stream = JpegStreamer("%s:%s" % (host, port))

        while True:
            camera.getImage().save(stream, quality=quality)

            # ensure it sleeps for as long as the fps in this case 10 fps
            time.sleep(0.1)
