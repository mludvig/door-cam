#!/usr/bin/env python3

import os
import sys
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
from pygame.locals import *

from .camera_local import CameraLocal
from .camera_remote import CameraRemote

class DoorCam:
    def __init__(self, fullscreen = False):
        # Start Pygame
        pygame.init()

        # Create display
        self.camera_size = (1280, 720)
        self.display_size = self.camera_size
        if fullscreen:
            self.screen = pygame.display.set_mode(self.display_size, FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.display_size)

        pygame.display.set_caption("Door Cam")
        self.font = pygame.font.SysFont("Arial", 14)
        self.clock = pygame.time.Clock()

    def main_loop(self, camera):
        while True:
            image = camera.read()
            self.screen.blit(image, (0,0))
            pygame.display.update()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT or
                    (event.type is KEYDOWN and event.key == K_ESCAPE)):
                        self.quit()
            self.clock.tick(5)

    def quit(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit()

def main():
    camera = CameraLocal()
    doorcam = DoorCam()
    doorcam.main_loop(camera)

if __name__ == "__main__":
    main()
