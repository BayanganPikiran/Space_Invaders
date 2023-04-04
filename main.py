import pygame
import random

pygame.init()

SCREEN_DIM = (800, 600)
SCREEN_COLOR = (0, 0, 0)

screen = pygame.display.set_mode(SCREEN_DIM)

#Caption and Icon
pygame.display.set_caption("Space Invaders")
alien_icon = pygame.image.load("alien.png")
pygame.display.set_icon(alien_icon)

#Background
outerspace = pygame.image.load("outerspace.png")

#Player
player_spaceship = pygame.image.load("spaceship.png")
player_x_pos = 370
player_y_pos = 500
player_x_pos_change = 0

def create_player(x, y):
    screen.blit(player_spaceship, (x, y))

#Create enemies
jesus = pygame.image.load("jesus.png")
monster = pygame.image.load("monster.png")
trump = pygame.image.load("trump.png")
enemy_list = [jesus, monster, trump]
enemy_x_pos = random.randint(64, 736)
enemy_y_pos = random.randint(20, 150)
enemy_x_pos_change = 2.5
enemy_y_pos_change = 40


def create_enemy(x, y):
    screen.blit(trump, (x, y) )





#Game loop
running = True

while running:
    screen.fill(SCREEN_COLOR)
    screen.blit(outerspace, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_pos_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_pos_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_pos_change = 0



    player_x_pos += player_x_pos_change
    if player_x_pos <= 0:
        player_x_pos = 0
    elif player_x_pos >= 736:
        player_x_pos = 736


    enemy_x_pos += enemy_x_pos_change
    if enemy_x_pos <= 0:
        enemy_x_pos_change = 2.5
        enemy_y_pos += enemy_y_pos_change
    elif enemy_x_pos >= 736:
        enemy_x_pos_change = -2.5
        enemy_y_pos += enemy_y_pos_change

    create_player(player_x_pos, player_y_pos)
    create_enemy(enemy_x_pos, enemy_y_pos)

    pygame.display.update()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


