import cv2
import numpy as np

import pygame

class CameraRemote:
    def __init__(self, address, camera_size=(1280,720)):
        self._camera_size = camera_size
        self._camera_address = address

        self.open()

    def open(self):
        self.cap = cv2.VideoCapture(self._camera_address)

    def read(self):
        # Read frame from remote camera
        ret, frame = self.cap.read()

        # Convert from OpenCV frame to PyGame Surface
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        #  convert from (height, width, channel) to (width, height, channel)
        frame = frame.transpose([1, 0, 2])
        frame = pygame.surfarray.make_surface(frame)

        return frame
