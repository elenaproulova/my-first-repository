import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определяем размеры окна
WIDTH, HEIGHT = 800, 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Определяем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определяем параметры ракеток и мяча
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15
PADDLE_SPEED = 7
BALL_SPEED_X, BALL_SPEED_Y = 5, 5

# Создаем классы для ракеток и мяча
class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

    def move(self, dy):
        self.rect.y += dy
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Отскок от верхней и нижней границы
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_y

        # Сброс мяча, если он выходит за границы
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.reset()

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = -self.speed_x

# Основной игровой цикл
def main():
    clock = pygame.time.Clock()
    paddle1 = Paddle(30)  # Левый игрок
    paddle2 = Paddle(WIDTH - 30 - PADDLE_WIDTH)  # Правый игрок
    ball = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle1.move(-PADDLE_SPEED)
        if keys[pygame.K_s]:
            paddle1.move(PADDLE_SPEED)
        if keys[pygame.K_UP]:
            paddle2.move(-PADDLE_SPEED)
        if keys[pygame.K_DOWN]:
            paddle2.move(PADDLE_SPEED)

        ball.move()

        # Проверка на столкновение с ракетками
        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x = -ball.speed_x

        # Обновление экрана
            WINDOW.fill(BLACK)
            pygame.draw.rect(WINDOW, WHITE, paddle1.rect)
            pygame.draw.rect(WINDOW, WHITE, paddle2.rect)
            pygame.draw.ellipse(WINDOW, WHITE, ball.rect)
            pygame.draw.aaline(WINDOW, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))  # Центр экрана

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__main__":
    main()