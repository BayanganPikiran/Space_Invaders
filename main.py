import pygame

pygame.init()

SCREEN_DIM = (800, 600)
SCREEN_COLOR = (0, 0, 0)

screen = pygame.display.set_mode(SCREEN_DIM)

#Caption and Icon
pygame.display.set_caption("Space Invaders")
alien_icon = pygame.image.load("alien.png")
pygame.display.set_icon(alien_icon)

#Player
player_spaceship = pygame.image.load("spaceship.png")
player_pos = (370, 500)


def create_player():
    screen.blit(player_spaceship, player_pos)


#Game loop
running = True
screen.fill(SCREEN_COLOR)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    create_player()
    pygame.display.update()
    
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


