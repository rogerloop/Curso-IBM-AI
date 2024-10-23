# food.py

import pygame
import random
from constants import SEGMENT_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT, ORANGE

class Food:
    def __init__(self):
        self.position = self._random_position()
        self.color = ORANGE

    def _random_position(self):
        x = random.randint(0, (SCREEN_WIDTH - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
        y = random.randint(0, (SCREEN_HEIGHT - SEGMENT_SIZE) // SEGMENT_SIZE) * SEGMENT_SIZE
        return (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, SEGMENT_SIZE, SEGMENT_SIZE))

    def respawn(self):
        self.position = self._random_position()
