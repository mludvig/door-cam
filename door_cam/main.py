#!/usr/bin/env python3

import os
import sys
import time

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import click

import pygame
from pygame.locals import *

from .camera_local import CameraLocal
from .camera_remote import CameraRemote

class DoorCam:
    def __init__(self, camera, fullscreen = False):
        # Start Pygame
        pygame.init()

        # Create display
        self.camera = camera
        self.camera_size = (1280, 720)
        self.display_size = self.camera_size
        if fullscreen:
            self.screen = pygame.display.set_mode(self.display_size, FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode(self.display_size)

        pygame.display.set_caption("Door Cam")
        self.font = pygame.font.SysFont("Arial", 14)
        self.clock = pygame.time.Clock()

    def main_loop(self, tick=5):
        while True:
            image = self.camera.read()
            self.screen.blit(image, (0,0))
            pygame.display.update()

            for event in pygame.event.get():
                if (event.type == pygame.QUIT or
                    (event.type is KEYDOWN and event.key == K_ESCAPE)):
                        self.quit()
            self.clock.tick(tick)

    def quit(self):
        pygame.display.quit()
        pygame.quit()
        sys.exit()

@click.command()
@click.option("--remote-cam", "remote", type=str, help="Remote camera URL, e.g. http:// or rtsp://")
@click.option("--local-cam", "local", type=click.Path(exists=True), help="Local camera device, e.g. /dev/video0")
def main(remote, local):
    if local:
        click.secho(f"Using local camera: {local}", fg="green")
        camera = CameraLocal(local)
    elif remote:
        click.secho(f"Using remote camera: {remote}", fg="green")
        camera = CameraRemote(remote)
    else:
        click.secho("Either --remote-cam or --local-cam must be set.", fg="red")
        sys.exit(1)

    doorcam = DoorCam(camera)
    doorcam.main_loop()
