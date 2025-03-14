import pygame
import datetime
import sys

pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey clock")

m_body = pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\mcclock.png")
l_hand = pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\l_hand.png")
r_hand = pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\r_hand.png")

bg = m_body.get_rect(center=(width // 2, height // 2))

m_hand = pygame.transform.scale(r_hand, (750, 750))  
s_hand = pygame.transform.scale(l_hand, (750, 750))  

def blit_rotate_center(surf, image, angle, pivot, offset):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=(pivot[0] + offset[0], pivot[1] + offset[1]))
    surf.blit(rotated_image, new_rect.topleft)

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(m_body, bg.topleft)  

    now = datetime.datetime.now()
    minutes = now.minute
    seconds = now.second

    minute_angle = -6 * minutes  
    second_angle = -6 * seconds  

    blit_rotate_center(screen, m_hand, minute_angle, (width // 2, height // 2), (0, 10))
    blit_rotate_center(screen, s_hand, second_angle, (width // 2, height // 2), (0, 20))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()

