import pygame

pygame.init()

SCREEN_DIM = (600, 600)
SCREEN_COLOR = (0, 0, 0)

alien_icon = pygame.image.load("alien.png")

screen = pygame.display.set_mode(SCREEN_DIM)

pygame.display.set_caption("Space Invaders")
pygame.display.set_icon(alien_icon)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SCREEN_COLOR)
    pygame.display.update()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


