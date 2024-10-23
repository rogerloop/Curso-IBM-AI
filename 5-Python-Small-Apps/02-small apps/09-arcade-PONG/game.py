# game.py
# Archivo que define la clase Game

import pygame
from constants import *
from paddle import Paddle
from ball import Ball

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Pong")

        self.font = pygame.font.Font(None, FONT_SIZE)
        self.clock = pygame.time.Clock()

        # Crear las paletas y la pelota
        self.player = Paddle(WINDOW_WIDTH - 20, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.opponent = Paddle(10, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2)
        self.ball = Ball()

        # Puntuaciones
        self.player_score = 0
        self.opponent_score = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Movimiento de la pelota
            self.ball.move()

            # Movimiento de la paleta del jugador
            self.player.move(pygame.K_UP, pygame.K_DOWN)

            # Movimiento de la IA
            self.opponent.ai_move(self.ball)

            # Colisiones entre la pelota y las paletas
            if self.ball.rect.colliderect(self.player.rect) or self.ball.rect.colliderect(self.opponent.rect):
                self.ball.speed_x = -self.ball.speed_x

            # Comprobar si la pelota sale de los límites y actualizar el marcador
            if self.ball.rect.left <= 0:
                self.player_score += 1
                self.ball.reset("player")  # Iniciar el nuevo punto desde el fondo del jugador
            if self.ball.rect.right >= WINDOW_WIDTH:
                self.opponent_score += 1
                self.ball.reset("opponent")  # Iniciar el nuevo punto desde el fondo del oponente

            # Dibujar todos los elementos en la pantalla
            self.screen.fill(BLACK)
            self.player.draw(self.screen)
            self.opponent.draw(self.screen)
            self.ball.draw(self.screen)

            # Mostrar el marcador
            score_text = self.font.render(f"{self.opponent_score} - {self.player_score}", True, WHITE)
            self.screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 10))

            # Actualizar la pantalla
            pygame.display.flip()

            # Controlar la velocidad del juego
            self.clock.tick(100)

        pygame.quit()
