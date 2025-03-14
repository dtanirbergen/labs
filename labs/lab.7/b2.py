import pygame
import sys
import pygame.mixer

pygame.init()
pygame.mixer.init()
pygame.font.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music player")

music_album = [
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Arctic_Monkeys_-_Do_I_Wanna_Know.mp3",#0
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Arctic_Monkeys_-_I_Wanna_Be_Yours.mp3",#1
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Arctic_Monkeys_-_No1_Party_Anthem.mp3",#2
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Arctic_Monkeys_-_R_U_Mine.mp3",#3
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Arctic_Monkeys_-_Whyd_You_Only_Call_Me_When_Youre_High.mp3",#4
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Arctic_Monkeys_-_505.mp3",#5
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Kiss_-_I_Was_Made_For_Lovin_You.mp3",#6
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Darkhan_Juzz_-_E_Sulu.mp3",#7
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Darkhan_Juzz_-_Erikpe.mp3",#8
    r"C:\Users\user\Desktop\PP_2\Pygame\sounds\Darkhan_Juzz_-_uide.mp3"#9
]

music_pictures = [
    pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\music_pictures\Arctic_Monkeys_logo.png"),#0
    pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\music_pictures\505_logo.jpg"),#1
    pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\music_pictures\kiss_logo.jpg"),#2
    pygame.image.load(r"C:\Users\user\Desktop\PP_2\Pygame\images\music_pictures\Darkhan_Juzz.jpg")#3
]

music_names = [
    "Do I Wanna Know",
    "I Wanna Be Yours",
    "No1 Party Anthem",
    "R U Mine",
    "Why'd You Only Call Me When You're High",
    "505",
    "I Was Made For Lovin' You",
    "En Sulu",
    "Erikpe",
    "Uide"
]

def start_music(index):
    pygame.mixer.music.load(music_album[index])
    pygame.mixer.music.play()

track = 0

MUSIC_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(MUSIC_END)

start_music(track)
is_paused = False

font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 150, HEIGHT // 2 - 180, 300, 300), 2)

    if track < 5:
        image = music_pictures[0]  # Arctic Monkeys
    elif track == 5:
        image = music_pictures[1]  # 505
    elif track == 6:
        image = music_pictures[2]  # Kiss
    elif track in [7, 8, 9]:
        image = music_pictures[3]  # Darkhan Juzz

    image = pygame.transform.scale(image, (300, 300))
    screen.blit(image, (WIDTH // 2 - 150, HEIGHT // 2 - 180))

    track_text = font.render(music_names[track], True, (255, 255, 255))
    text_rect = track_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 140))
    screen.blit(track_text, text_rect)

    pygame.draw.line(screen, (255, 255, 255), (WIDTH // 2 - 150, HEIGHT // 2 + 167), (WIDTH // 2 + 150, HEIGHT // 2 + 167), 2)

    pygame.draw.polygon(screen, (255, 255, 255), [
        (WIDTH // 2 - 90, HEIGHT // 2 + 180),
        (WIDTH // 2 - 110, HEIGHT // 2 + 200),
        (WIDTH // 2 - 90, HEIGHT // 2 + 220)
    ])

    pygame.draw.rect(screen, (255, 255, 255), (WIDTH // 2 - 15, HEIGHT // 2 + 183, 30, 30))

    pygame.draw.polygon(screen, (255, 255, 255), [
        (WIDTH // 2 + 90, HEIGHT // 2 + 180),
        (WIDTH // 2 + 110, HEIGHT // 2 + 200),
        (WIDTH // 2 + 90, HEIGHT // 2 + 220)
    ])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MUSIC_END:
            track = (track + 1) % len(music_album)
            start_music(track)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                else:
                    pygame.mixer.music.pause()
                    is_paused = True

            elif event.key == pygame.K_l:
                track = (track + 1) % len(music_album)
                start_music(track)

            elif event.key == pygame.K_j:
                track = (track - 1) % len(music_album)
                start_music(track)

    pygame.display.update()

pygame.quit()
sys.exit()
