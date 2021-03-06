import time

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
    small_image = full_image.scale(320, 240)
    return small_image.findHaarFeatures('face')


def start_camera(host_camera, host, port):
    camera = Camera(host_camera, {"width": 640, "height": 480})
    stream = JpegStreamer("%s:%s" % (host, port))

    while True:

        # save the image to the stream
        full_image = camera.getImage()
        full_image.save(stream)

        # ensure it sleeps for as long as the fps in this case 10 fps
        time.sleep(0.1)
