import pygame
import random
import sys
import db_handler

pygame.init()

WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

WHITE = (255, 255, 255)
DARKGREEN = (0, 100, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
CHARTREUSE = (127, 255, 0)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = RIGHT
        self.grow = False
    
    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = ((head_x + dx * CELL_SIZE) % WIDTH, (head_y + dy * CELL_SIZE) % HEIGHT)
        
        if new_head in self.body[:-1]:
            return False
        
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True
    
    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) != self.direction:
            self.direction = new_direction
    
    def grow_snake(self):
        self.grow = True

class Food:
    def __init__(self, snake_body):
        self.position = self.random_position(snake_body)
    
    def random_position(self, snake_body):
        while True:
            x = random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE
            y = random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
            if (x, y) not in snake_body:
                return (x, y)
    
    def respawn(self, snake_body):
        self.position = self.random_position(snake_body)

def draw_snake(screen, snake):
    for segment in snake.body:
        pygame.draw.rect(screen, DARKGREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(screen, food):
    pygame.draw.rect(screen, RED, (*food.position, CELL_SIZE, CELL_SIZE))

def show_score_level(screen, score, level, font):
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

def game_over_screen(screen, width, height, font):
    screen.fill(RED)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    db_handler.create_tables()
    
    username = input("Enter your username: ")
    user_id = db_handler.get_or_create_user(username)
    last_score, last_level = db_handler.get_last_score(user_id)
    print(f"Welcome back, {username}! Your last score was {last_score} at level {last_level}")

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    
    snake = Snake()
    food = Food(snake.body)
    score = 0
    level = last_level
    speed = FPS + (level - 1) * 2
    running = True
    paused = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        db_handler.save_score(user_id, score, level)
                elif not paused:
                    if event.key == pygame.K_UP:
                        snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(RIGHT)
        
        if paused:
            continue
        
        if not snake.move():
            game_over_screen(screen, WIDTH, HEIGHT, font)
            running = False
            break
        
        if snake.body[0] == food.position:
            score += 1
            snake.grow_snake()
            food.respawn(snake.body)
            
            if score % 3 == 0:
                level += 1
                speed += 2
        
        screen.fill(CHARTREUSE)
        draw_snake(screen, snake)
        draw_food(screen, food)
        show_score_level(screen, score, level, font)
        
        pygame.display.flip()
        clock.tick(speed)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()