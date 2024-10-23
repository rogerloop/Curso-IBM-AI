# paddle.py
# Archivo que define la clase Paddle

import pygame
from constants import *

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = PADDLE_SPEED

    def move(self, up_key, down_key):
        keys = pygame.key.get_pressed()
        if keys[up_key]:
            self.rect.y -= self.speed
        if keys[down_key]:
            self.rect.y += self.speed

        # Evitar que la paleta salga de la pantalla
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT

    def ai_move(self, ball):
        # Movimiento muy simple: seguir la pelota
        if self.rect.centery < ball.rect.centery:
            self.rect.y += self.speed
        elif self.rect.centery > ball.rect.centery:
            self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
