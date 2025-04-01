import pygame
import random

pygame.init()

w, h = 600, 400
CELL_SIZE = 20 #размер змейки

"""Цвета"""
WHITE = (255, 255, 255)
DARKGREEN = (0, 100, 0, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
CHARTUSE=(127, 255, 0, 255)

screen = pygame.display.set_mode((w, h))

#контроль времени игры
clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

# направление
UP = (0, -CELL_SIZE)
DOWN = (0, CELL_SIZE)
LEFT = (-CELL_SIZE, 0)
RIGHT = (CELL_SIZE, 0)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)] #начальная позиция змейки
        self.direction = RIGHT  #начальное направление
        self.grow = False  #для увеличение роста после еды
    
    def move(self):
        #движение змейки
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])

        #проверка на выход из границ
        if new_head[0] < 0 or new_head[0] >= w or new_head[1] < 0 or new_head[1] >= h:
            return False  
        
        #проверка не сьели сама себя
        if new_head in self.body:
            return False  
        
        self.body.insert(0, new_head)  #добавление головы
        
        if not self.grow:
            self.body.pop()  #если не должна расти удаляем последний сегмент
        else:
            self.grow = False  

        return True  #продолжаем игру

    def change_direction(self, new_direction):
        #исключаем возможность поворота на 180
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction

    def grow_snake(self):
        #увелечение змейки
        self.grow = True

class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body) #случайное позицие еды

    def random_position(self, snake_body):
        #нахождение позиции еды не в внутри змейки
        while True:
            x = random.randint(0, (w // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (h // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)

    def respawn(self, snake_body):
        #генерацие новой еды
        self.position = self.random_position(snake_body)

def draw_snake(snake):
    #рисуем змейку
    for segment in snake.body:
        pygame.draw.rect(screen, DARKGREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

def draw_food(food):
    """Рисует еду на экране"""
    pygame.draw.rect(screen, RED, (food.position[0], food.position[1], CELL_SIZE, CELL_SIZE))

def show_score_level(score, level):
    """Пишет очки и левел"""
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))

def game_over(score, level):
    #выводит окончание игры
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
                    return  #пробел экрана Game Over для рестарта

while True:
    """игровые элементы"""
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = 1
    speed = 10  # скорость фпс

    running = True
    while running:
        screen.fill(CHARTUSE)

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

        #проверяем продолжится ли игра дальше
        if not snake.move():
            game_over(score, level)
            break  # Выход из игрового цикла, чтобы перезапустить

        #проверяем сьелали еду змея
        if snake.body[0] == food.position:
            score += 1 
            snake.grow_snake()
            food.respawn(snake.body)

            #каждые 3три фрукта увеличиваем левел и скорость
            if score % 3 == 0:
                level += 1
                speed += 2  

        #Отрисовываем объекты и обновляем игру
        draw_snake(snake)
        draw_food(food)
        show_score_level(score, level)

        pygame.display.flip()
        clock.tick(speed)
