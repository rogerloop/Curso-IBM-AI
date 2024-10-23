# ball.py
# Archivo que define la clase Ball

import pygame
from constants import *


class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Rebotar en la parte superior e inferior
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y = -self.speed_y

    def reset(self, starting_position="center"):
        if starting_position == "player":
            # 1/4 desde el borde derecho
            self.rect.x = WINDOW_WIDTH - WINDOW_WIDTH // 4
            self.speed_x = -abs(self.speed_x)  # Enviar la pelota hacia el oponente
        elif starting_position == "opponent":
            # 1/4 desde el borde izquierdo
            self.rect.x = WINDOW_WIDTH // 4
            self.speed_x = abs(self.speed_x)  # Enviar la pelota hacia el jugador
        else:
            self.rect.x = WINDOW_WIDTH // 2  # Centro de la pantalla
            self.speed_x = BALL_SPEED_X if self.speed_x < 0 else -BALL_SPEED_X

        self.rect.y = WINDOW_HEIGHT // 2
        self.speed_y = BALL_SPEED_Y if self.speed_y < 0 else -BALL_SPEED_Y

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
