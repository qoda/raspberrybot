import os
import time

from django.conf import settings
from django.core.management.base import BaseCommand

from SimpleCV import Camera, Color, DrawingLayer, JpegStreamer


class Command(BaseCommand):
    args = ''
    help = "Start the video stream."

    def handle(self, *args, **options):
        host = options.get('host', '0.0.0.0')
        port = options.get('port', '8090')
        host_camera = options.get('host_camera', 0)

        # setup the stream
        camera = Camera(host_camera, {"width": 800, "height": 600})
        stream = JpegStreamer("%s:%s" % (host, port))

        while True:
            detect_faces = os.path.exists(
                os.path.join(settings.BASE_DIR, '.detect')
            )
            full_image = camera.getImage()
            if detect_faces:
                small_image = full_image.scale(200, 150)
                facial_features = small_image.findHaarFeatures('face')
                if facial_features is not None:
                    x = facial_features.x() * 4
                    y = facial_features.y() * 4
                    width = facial_features.width() * 4
                    height = facial_features.height() * 4

                    face_layer = DrawingLayer(
                        (full_image.width, full_image.height)
                    )
                    face_layer.centeredRectangle(
                        (x[0], y[0]),
                        (width[0], height[0]),
                        color=Color.ORANGE,
                        width=1
                    )
                    full_image.addDrawingLayer(face_layer)
                    full_image.applyLayers()

            full_image.save(stream, quality=60)

            # ensure it sleeps for as long as the fps in this case 10 fps
            time.sleep(0.1)
