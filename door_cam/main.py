#!/usr/bin/env python3

import sys
import time

import pygame
from pygame.locals import *
import pygame.camera

# Start Pygame
pygame.init()
pygame.camera.init()

# Create display
camera_size = (1280, 720)
display_size = (1366, 768)
#screen = pygame.display.set_mode((w, h), FULLSCREEN)
screen = pygame.display.set_mode(display_size)

pygame.display.set_caption("Door Cam")
font = pygame.font.SysFont("Arial", 14)
clock = pygame.time.Clock()
timer = 0

# Open camera
cam = pygame.camera.Camera("/dev/video0", camera_size, "RGB")
cam.start()

while True:
    screen = pygame.display.get_surface()
    image = cam.get_image()
    screen.blit(image, (0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
            (event.type is KEYDOWN and event.key == K_ESCAPE)):
                pygame.display.quit()
                pygame.quit()
                sys.exit()

    clock.tick(10)
