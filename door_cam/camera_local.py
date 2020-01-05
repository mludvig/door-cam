import pygame.camera

class CameraLocal:
    def __init__(self, device="/dev/video0", camera_size=(1280,720)):
        self._camera_device = device
        self._camera_size = camera_size

        self.open()

    def open(self):
        pygame.camera.init()
        self.camera = pygame.camera.Camera(self._camera_device, self._camera_size, "RGB")
        self.camera.start()

    def read(self):
        return self.camera.get_image()
