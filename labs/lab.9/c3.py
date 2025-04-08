import pygame
import math

# Инициализация pygame
pygame.init()

# Константы
width, height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
soft_pink = (255, 182, 193)  # Дополнительный цвет

# Настройка дисплея
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pygame paint")

# Инициализация переменных
drawing = False
mode = "brush"  # Режимы рисования: "brush", "rectangle", "circle", "square", "right_triangle", "equilateral_triangle", "rhombus", "eraser"
start_pos = None
selected_color = black
brush_size = 5
eraser_size = 10  # Размер ластика

# Создание холста для рисования
canvas = pygame.Surface((width, height))
canvas.fill(white)

# Создаем шрифт для отображения текста
font = pygame.font.Font(None, 30)

# Основной цикл
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(white)
    screen.blit(canvas, (0, 0))  # Сохраняем рисунки на холсте

    # Отображение режима рисования и цвета
    mode_text = font.render(f"Mode: {mode}", True, black)
    color_text = font.render(f"Color: {selected_color}", True, selected_color)

    # Отображаем режим рисования и цвет на экране
    screen.blit(mode_text, (10, 10))  # Отображаем режим рисования в верхнем левом углу
    screen.blit(color_text, (10, 40))  # Отображаем выбранный цвет ниже

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Нажатие кнопки мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos  # Запоминаем начальную точку для рисования

        # Отжатие кнопки мыши
        elif event.type == pygame.MOUSEBUTTONUP:
            if start_pos:
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos

                # Рисуем фигуры в зависимости от выбранного режима
                if mode == "rectangle":
                    rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, selected_color, rect, 2)

                elif mode == "square":
                    side_length = min(abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, selected_color, (x1, y1, side_length, side_length), 2)

                elif mode == "circle":
                    radius = int(math.dist(start_pos, end_pos) / 2)
                    center = ((x1 + x2) // 2, (y1 + y2) // 2)
                    pygame.draw.circle(canvas, selected_color, center, radius, 2)

                elif mode == "right_triangle":
                    pygame.draw.polygon(canvas, selected_color, [(x1, y1), (x1, y2), (x2, y2)], 2)

                elif mode == "equilateral_triangle":
                    side = abs(x2 - x1)
                    height = int(math.sqrt(3) / 2 * side)
                    pygame.draw.polygon(canvas, selected_color, [(x1, y2), (x1 + side, y2), (x1 + side // 2, y2 - height)], 2)

                elif mode == "rhombus":
                    dx = abs(x2 - x1) // 2
                    dy = abs(y2 - y1) // 2
                    pygame.draw.polygon(canvas, selected_color, [(x1, y1 + dy), (x1 + dx, y1), (x1 + 2 * dx, y1 + dy), (x1 + dx, y1 + 2 * dy)], 2)

            drawing = False

        # Обработка нажатий клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"  # Режим прямоугольника
            elif event.key == pygame.K_s:
                mode = "square"  # Режим квадрата
            elif event.key == pygame.K_c:
                mode = "circle"  # Режим круга
            elif event.key == pygame.K_t:
                mode = "right_triangle"  # Режим прямоугольного треугольника
            elif event.key == pygame.K_e:
                mode = "equilateral_triangle"  # Режим равностороннего треугольника
            elif event.key == pygame.K_h:
                mode = "rhombus"  # Режим ромба
            elif event.key == pygame.K_x:
                mode = "eraser"  # Режим ластика
            elif event.key == pygame.K_b:
                mode = "brush"  # Режим кисти

            # Выбор цвета
            elif event.key == pygame.K_1:
                selected_color = black
            elif event.key == pygame.K_2:
                selected_color = red
            elif event.key == pygame.K_3:
                selected_color = green
            elif event.key == pygame.K_4:
                selected_color = blue
            elif event.key == pygame.K_5:
                selected_color = yellow
            elif event.key == pygame.K_6:
                selected_color = soft_pink

            # Регулировка размера кисти и ластика
            elif event.key == pygame.K_UP:
                brush_size += 2
                eraser_size += 2
            elif event.key == pygame.K_DOWN and brush_size > 2:
                brush_size -= 2
                eraser_size -= 2

    # Логика рисования
    if drawing:
        if mode == "brush":
            pygame.draw.circle(canvas, selected_color, pygame.mouse.get_pos(), brush_size)
        elif mode == "eraser":
            pygame.draw.circle(canvas, white, pygame.mouse.get_pos(), eraser_size)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
