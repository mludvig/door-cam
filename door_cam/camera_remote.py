import threading

import cv2
import numpy as np
import pygame

from loguru import logger

from .fps import FPS_Reporter

class CameraRemote:
    def __init__(self, address, camera_size=(1280,720)):
        self._camera_size = camera_size
        self._camera_address = address
        self._current_frame = None
        self._reader_stop = False

        self.open()

        self.reader = threading.Thread(
            target=self._reader,
            name="Thread-RemoteCam",
            daemon=True
        )
        self.reader.start()

    def open(self):
        self.cap = cv2.VideoCapture(self._camera_address)

    def close(self):
        if self.reader:
            logger.info(f"Stopping the reader thread: {self.reader.name}")
            self._reader_stop = True
            self.reader.join()
        self.cap.release()

    def _reader(self):
        logger.info(f"Starting reader thread: {self.reader.name}")
        fps = FPS_Reporter(loop_name="camera_reader")
        while self._reader_stop == False:
            # Read frame from remote camera
            ret, self._current_frame = self.cap.read()
            fps.report()

    def read(self):
        if self._current_frame is None:
            return None

        # Convert from OpenCV frame to PyGame Surface
        frame = cv2.cvtColor(self._current_frame, cv2.COLOR_BGR2RGB)
        #  convert from (height, width, channel) to (width, height, channel)
        frame = frame.transpose([1, 0, 2])

        return pygame.surfarray.make_surface(frame)
