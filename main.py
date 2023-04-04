import math
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



#Create enemies
jesus = pygame.image.load("jesus.png")
monster = pygame.image.load("monster.png")
trump = pygame.image.load("trump.png")
gandhi = pygame.image.load("gandhi.png")
greta = pygame.image.load("greta_thunberg.png")
enemy_list = [jesus, monster, gandhi, trump]
enemy_x_pos = random.randint(64, 735)
enemy_y_pos = random.randint(50, 180)
enemy_x_pos_change = 2.5
enemy_y_pos_change = 40

#Create missile
missile = pygame.image.load("missile.png")
missile_x_pos = 0
missile_y_pos = 480
missile_x_pos_change = 0
missile_y_pos_change = 20
missile_state = "ready"

score = 0


def create_player(x, y):
    screen.blit(player_spaceship, (x, y))

def create_enemy(x, y):
    screen.blit(greta, (x, y) )

def fire_missile(x, y):
    global missile_state
    missile_state = "fire"
    screen.blit(missile, (x+16, y+10))

def detect_collision(enemy_x, enemy_y, missile_x, missile_y):
    distance = math.sqrt(math.pow(enemy_x- missile_x, 2) + math.pow(enemy_y - missile_y, 2))
    if distance < 27:
        return True
    else:
        return False




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
            if event.key == pygame.K_SPACE:
                missile_x_pos = player_x_pos
                fire_missile(missile_x_pos, missile_y_pos)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_x_pos_change = 0



    #Player movement
    player_x_pos += player_x_pos_change
    if player_x_pos <= 0:
        player_x_pos = 0
    elif player_x_pos >= 736:
        player_x_pos = 736

    #Enemy Movement
    enemy_x_pos += enemy_x_pos_change
    if enemy_x_pos <= 0:
        enemy_x_pos_change = 2.5
        enemy_y_pos += enemy_y_pos_change
    elif enemy_x_pos >= 736:
        enemy_x_pos_change = -2.5
        enemy_y_pos += enemy_y_pos_change

    # Missile movement
    if missile_y_pos <= 0:
        missile_y_pos = 480
        missile_state = "ready"
    if missile_state is "fire":
        fire_missile(missile_x_pos, missile_y_pos)
        missile_y_pos -= missile_y_pos_change

    # Collision
    collision = detect_collision(enemy_x_pos, enemy_y_pos, missile_x_pos, missile_y_pos)
    if collision:
        missile_y_pos = 480
        missile_state = "ready"
        score += 1
        print(score)
        enemy_x_pos = random.randint(64, 735)
        enemy_y_pos = random.randint(50, 180)


    create_player(player_x_pos, player_y_pos)
    create_enemy(enemy_x_pos, enemy_y_pos)

    pygame.display.update()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


