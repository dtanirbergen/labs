import pygame

# initialize pygame
pygame.init()

# константы
width, height = 800, 600
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("pygame paint")

# initialize variables
drawing = False  # флаг рисования
mode = "brush"  # текущий инструмент "brush", "rectangle", "circle", "eraser"
start_pos = None  # начальная точка
selected_color = black
brush_size = 5
eraser_size = 10  # отдельный размер для ластика

# create a font
font = pygame.font.Font(None, 30)

# main loop
running = True
clock = pygame.time.Clock()

# создаем холст для рисования
canvas = pygame.Surface((width, height))
canvas.fill(white)

while running:
    screen.fill(white)
    screen.blit(canvas, (0, 0))  # сохраняем рисунки

    # отображение режима рисования и цвета
    mode_text = font.render(f"Mode: {mode}", True, black)
    color_text = font.render(f"Color: {selected_color}", True, selected_color)

    screen.blit(mode_text, (10, 10))  # отображение режима рисования в верхнем левом углу
    screen.blit(color_text, (10, 40))  # отображение выбранного цвета

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # нажатие мышки
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos  # запоминает начальную точку для квадрата или круга

        elif event.type == pygame.MOUSEBUTTONUP:
            if mode in ["rectangle", "circle"] and start_pos:
                end_pos = event.pos
                if mode == "rectangle":
                    rect = pygame.Rect(min(start_pos[0], end_pos[0]), min(start_pos[1], end_pos[1]),
                                       abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, selected_color, rect, 2)  # рисуем прямоугольник
                elif mode == "circle":
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5 / 2)
                    center = ((start_pos[0] + end_pos[0]) // 2, (start_pos[1] + end_pos[1]) // 2)
                    pygame.draw.circle(canvas, selected_color, center, radius, 2)  # рисуем круг
            drawing = False

        # нажатие клавиш
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"  # переключение на режим прямоугольника
            elif event.key == pygame.K_c:
                mode = "circle"  # переключение на режим круга
            elif event.key == pygame.K_e:
                mode = "eraser"  # переключение на режим ластика
            elif event.key == pygame.K_b:
                mode = "brush"  # переключение на режим кисти

            # выбор цвета
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

            # изменение размера кисти и ластика
            elif event.key == pygame.K_UP:
                brush_size += 2
                eraser_size += 2
            elif event.key == pygame.K_DOWN and brush_size > 2:
                brush_size -= 2
                eraser_size -= 2

    # логика рисования
    if drawing:
        if mode == "brush":
            pygame.draw.circle(canvas, selected_color, pygame.mouse.get_pos(), brush_size)
        elif mode == "eraser":
            pygame.draw.circle(canvas, white, pygame.mouse.get_pos(), eraser_size)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
