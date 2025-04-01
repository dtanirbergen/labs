import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
w, h = 400, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Загрузка ресурсов
player_img = pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\racer\Player.png")
enemy_img = pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\racer\Enemy.png")
coin_img = pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\racer\coin.png")
street_img = pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\racer\AnimatedStreet.png")
crash_sound = pygame.mixer.Sound(r"C:\Users\user\Desktop\PP_2\Pygame\sounds\crash.wav")
background_sound = pygame.mixer.Sound(r"C:\Users\user\Desktop\PP_2\Pygame\sounds\background.wav")

# Изменение размера изображения монеты
coin_img = pygame.transform.scale(coin_img, (30, 30))

# Отображение окна
screen = pygame.display.set_mode((w, h))

# Воспроизведение фоновой музыки
background_sound.play(-1)  # Зацикленный звук

font = pygame.font.Font(None, 50)

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(w // 2, h - 100)) # Начальная позиция внизу по центру
    
    def update(self, keys):  # Движение игрока влево и вправо
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < w:
            self.rect.x += 5

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(midtop=(random.randint(50, w - 50), 0))
        self.speed = 5
    
    def update(self):  # Движение вражеской машины вниз
        self.rect.y += self.speed
        if self.rect.top > h:
            self.rect.midtop = (random.randint(50, w - 50), 0)

# Класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_img  # Изменённый размер монеты
        self.rect = self.image.get_rect(midtop=(random.randint(50, w - 50), 0))
        self.speed = 3 # Скорость монеты
    
    def update(self):  # Движение монеты вниз и удаление, если она достигла нижней границы
        self.rect.y += self.speed
        if self.rect.top > h:
            self.kill()

# Группы игровых объектов
all_sprites = pygame.sprite.Group()
player = Player()
enemy = Enemy()
coins = pygame.sprite.Group()
all_sprites.add(player, enemy)

# Основной игровой цикл
running = True
clock = pygame.time.Clock()
score = 0  # Счётчик монет
score_font = pygame.font.Font(None, 36)

def show_game_over():
    """Отображает экран 'Game Over' и ожидает нажатия ПРОБЕЛА для перезапуска."""
    global running, score, all_sprites, coins, player, enemy
    game_over_running = True
    while game_over_running:
        screen.fill(RED)
        text = font.render("Game Over", True, WHITE)
        score_text = score_font.render(f"Монеты: {score}", True, WHITE)
        restart_text = score_font.render("Нажмите ПРОБЕЛ", True, WHITE)
        
        screen.blit(text, (w // 2 - 100, h // 2 - 70))
        screen.blit(score_text, (w // 2 - 70, h // 2 - 20))
        screen.blit(restart_text, (w // 2 - 130, h // 2 + 30))
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_running = False
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Перезапуск игры
                score = 0
                all_sprites = pygame.sprite.Group()
                coins = pygame.sprite.Group()
                player = Player()
                enemy = Enemy()
                all_sprites.add(player, enemy)
                game_over_running = False

while running:
    screen.fill(WHITE)
    screen.blit(street_img, (0, 0))  # Отображение дороги/фона
    
    # Получение нажатых клавиш и обновление игрока
    keys = pygame.key.get_pressed()
    player.update(keys)  # Обновление позиции игрока
    enemy.update()  # Движение врага
    coins.update()  # Движение монет
    
    # Создание монет
    if random.randint(1, 100) < 2:
        coin = Coin()
        coins.add(coin)
        all_sprites.add(coin)
    
    # Проверка столкновений
    if pygame.sprite.spritecollide(player, coins, True):
        score += 1  # Увеличение счёта при сборе монет
    
    if pygame.sprite.collide_rect(player, enemy):
        crash_sound.play()
        show_game_over()
    
    # Отрисовка объектов
    all_sprites.draw(screen)
    coins.draw(screen)
    
    # Отображение счёта
    score_text = score_font.render(f"Монеты: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
