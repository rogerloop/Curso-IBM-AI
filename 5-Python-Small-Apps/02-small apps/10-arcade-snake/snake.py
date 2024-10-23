# snake.py

import pygame
from constants import SEGMENT_SIZE, WHITE


class Snake:
    def __init__(self):
        self.segments = [(100, 100), (80, 100), (60, 100)]  # Segmentos iniciales
        self.direction = 'RIGHT'
        self.color = WHITE

    def move(self):
        x, y = self.segments[0]
        if self.direction == 'UP':
            y -= SEGMENT_SIZE
        elif self.direction == 'DOWN':
            y += SEGMENT_SIZE
        elif self.direction == 'LEFT':
            x -= SEGMENT_SIZE
        elif self.direction == 'RIGHT':
            x += SEGMENT_SIZE

        # Insertar nuevo segmento en la cabeza
        new_segment = (x, y)
        self.segments = [new_segment] + self.segments[:-1]

    def grow(self):
        self.segments.append(self.segments[-1])

    def set_direction(self, direction):
        # Prevenir que la serpiente se mueva en dirección opuesta inmediatamente
        opposite_directions = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if direction != opposite_directions.get(self.direction):
            self.direction = direction

    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, self.color, (*segment, SEGMENT_SIZE, SEGMENT_SIZE))

    def check_collision_with_self(self):
        return self.segments[0] in self.segments[1:]

    def get_head_position(self):
        return self.segments[0]
