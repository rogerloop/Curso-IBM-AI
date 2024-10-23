## game.py

import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, FPS
from snake import Snake   # CORRECCIÓN AQUÍ
from food import Food     # CORRECCIÓN AQUÍ


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.set_direction('UP')
                    elif event.key == pygame.K_DOWN:
                        self.snake.set_direction('DOWN')
                    elif event.key == pygame.K_LEFT:
                        self.snake.set_direction('LEFT')
                    elif event.key == pygame.K_RIGHT:
                        self.snake.set_direction('RIGHT')

            self.snake.move()

            # Verificar si la serpiente come la comida
            if self.snake.get_head_position() == self.food.position:
                self.snake.grow()
                self.food.respawn()
                self.score += 1

            # Verificar colisiones con los bordes
            x, y = self.snake.get_head_position()
            if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
                running = False

            # Verificar colisión con sí misma
            if self.snake.check_collision_with_self():
                running = False

            self.screen.fill(BLACK)
            self.snake.draw(self.screen)
            self.food.draw(self.screen)
            self.draw_score()
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

    def draw_score(self):
        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, [0, 0])
