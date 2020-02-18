import cv2
import numpy as np

import pygame
import threading

class CameraRemote:
    def __init__(self, address, camera_size=(1280,720)):
        self._camera_size = camera_size
        self._camera_address = address
        self.current_frame = None
        self.reader_stop = False

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
            print(f"Stopping the reader thread: {self.reader.name}")
            self.reader_stop = True
            self.reader.join()
        self.cap.release()

    def _reader(self):
        print(f"Starting reader thread: {self.reader.name}")
        while self.reader_stop == False:
            # Read frame from remote camera
            ret, frame = self.cap.read()

            # Convert from OpenCV frame to PyGame Surface
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            #  convert from (height, width, channel) to (width, height, channel)
            frame = frame.transpose([1, 0, 2])
            self.current_frame = pygame.surfarray.make_surface(frame)

    def read(self):
        return self.current_frame
