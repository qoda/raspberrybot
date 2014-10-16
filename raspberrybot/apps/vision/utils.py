import os
import time

from django.conf import settings
from SimpleCV import Camera, Color, DrawingLayer, JpegStreamer


def draw_detected_face(full_image, facial_features=None):
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


def detect_faces(full_image):
    detect_faces = os.path.exists('/tmp/.detect')
    if detect_faces:
        small_image = full_image.scale(320, 240)
        return small_image.findHaarFeatures('face')


def start_camera(host_camera, host, port):
    camera = Camera(host_camera, {"width": 640, "height": 480})
    stream = JpegStreamer("%s:%s" % (host, port))

    count = 0
    facial_features = None
    while True:
        full_image = camera.getImage()

        # detect faces every 10 frames
        if count >= 10:
            facial_features = detect_faces(full_image)
            count = 0

        if count == 0:
            facial_features = None

        draw_detected_face(facial_features, full_image)

        # save the image to the stream
        full_image.save(stream, quality=60)

        # ensure it sleeps for as long as the fps in this case 10 fps
        time.sleep(0.1)

        count += 1
