import time

from django.core.management.base import BaseCommand

from SimpleCV import Camera, JpegStreamer


class Command(BaseCommand):
    args = ''
    help = "Start the video stream."

    def handle(self, *args, **options):
        host = options.get('host', '0.0.0.0')
        port = options.get('port', '8090')
        host_camera = options.get('host_camera', 0)

        # setup the stream
        camera = Camera(host_camera)
        stream = JpegStreamer("%s:%s" % (host, port))

        while True:
            image = camera.getImage()
            image.save(stream)

            # ensure it sleeps for as long as the fps in this case 10 fps
            time.sleep(0.1)
