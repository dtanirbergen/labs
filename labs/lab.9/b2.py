import pygame
import random

pygame.init()

w, h = 600, 400
CELL_SIZE = 20  # размер клетки

# Цвета
WHITE = (255, 255, 255)
DARKGREEN = (0, 100, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
CHARTUSE = (127, 255, 0, 255)  # цвет фона

screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Направления
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]  # начальная позиция змейки
        self.direction = RIGHT  # начальное направление
        self.grow = False  # увеличение после еды

    def move(self):
        # движение змейки
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        # проверка на столкновение со стеной
        if new_head[0] < 0 or new_head[0] >= w or new_head[1] < 0 or new_head[1] >= h:
            return False

        # проверка на столкновение с собой
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)  # добавление новой головы

        if not self.grow:
            self.body.pop()  # удаление хвоста если не растем
        else:
            self.grow = False  # сбрасываем флаг роста

        return True

    def change_direction(self, new_direction):
        # запрет поворота на 180 градусов
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def grow_snake(self):
        # включаем рост змейки
        self.grow = True

class Food:
    def __init__(self, snake_body):
        self.respawn(snake_body)

    def respawn(self, snake_body):
        # новая еда в случайном месте
        self.position = self.random_position(snake_body)
        self.weight = random.randint(1, 4)  # случайный вес
        self.spawn_time = pygame.time.get_ticks()  # время появления

    def random_position(self, snake_body):
        # случайная позиция вне тела змеи
        while True:
            x = random.randint(0, (w // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (h // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)

    def check_timer(self, snake_body):
        # если прошло 5 секунд — новая еда
        if pygame.time.get_ticks() - self.spawn_time > 5000:
            self.respawn(snake_body)

def draw_snake(snake):
    # рисуем змейку
    for segment in snake.body:
        pygame.draw.rect(screen, DARKGREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    # рисуем еду
    pygame.draw.rect(screen, RED, (food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))
    weight_text = font.render(str(food.weight), True, WHITE)
    screen.blit(weight_text, (food.position[0] + 5, food.position[1] + 2))

def show_score_level(score, level):
    # рисуем очки и уровень
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over(score, level):
    # экран конца игры
    game_over_running = True
    while game_over_running:
        screen.fill(RED)
        text = font.render("Game Over - Press SPACE to Restart", True, WHITE)
        score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)

        screen.blit(text, (w // 2 - text.get_width() // 2, h // 2 - 40))
        screen.blit(score_text, (w // 2 - score_text.get_width() // 2, h // 2))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return  # перезапуск

while True:
    # создаем элементы
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1
    speed = 10  # начальная скорость

    running = True
    while running:
        screen.fill(CHARTUSE)
        food.check_timer(snake.body)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction(UP)
                elif event.key == pygame.K_DOWN:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction(RIGHT)

        # движение змейки
        if not snake.move():
            game_over(score, level)
            break  # перезапуск

        # проверка на еду
        if snake.body[0] == food.position:
            score += food.weight
            snake.grow_snake()
            food.respawn(snake.body)

            # каждый 3 очка — +уровень и +скорость
            if score % 3 == 0:
                level += 1
                speed += 2

        draw_snake(snake)
        draw_food(food)
        show_score_level(score, level)

        pygame.display.flip()
        clock.tick(speed)
