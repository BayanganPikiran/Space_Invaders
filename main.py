import math
import pygame
import random
from pygame import mixer

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

#Background sound
mixer.music.load("space_oddity.wav")
mixer.music.play(-1)

#Collision sounds
# all_wrong = mixer.Sound("this_all_wrong.wav")
# should_not_be_here = mixer.Sound("shouldnt_be_up_here.wav")
# in_school = mixer.Sound("in_school.wav")
# my_dreams = mixer.Sound("my_dreams.wav")
how_dare = mixer.Sound("how_dare_you.wav")


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
enemy_list = [jesus, monster, gandhi, trump, greta]

enemy_image = []
enemy_x_pos = []
enemy_y_pos = []
enemy_x_pos_change = []
enemy_y_pos_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemy_image.append(random.choice(enemy_list))
    enemy_x_pos.append(random.randint(64, 735))
    enemy_y_pos.append(random.randint(50, 180))
    enemy_x_pos_change.append(2.5)
    enemy_y_pos_change.append(40)

#Create missile
missile = pygame.image.load("missile.png")
missile_x_pos = 0
missile_y_pos = 480
missile_x_pos_change = 0
missile_y_pos_change = 20
missile_state = "ready"

#Score
score_value = 0
font = pygame.font.Font("zai_CourierPolski1941.ttf", 46)

score_pos_x = 290
score_pos_y = 10

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def create_player(x, y):
    screen.blit(player_spaceship, (x, y))

def create_enemy(x, y):
    screen.blit(greta, (x, y))

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
                missile_sound = mixer.Sound("laser.wav")
                missile_sound.play()
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
    for i in range(num_of_enemies):
        enemy_x_pos[i] += enemy_x_pos_change[i]
        if enemy_x_pos[i] <= 0:
            enemy_x_pos_change[i] = 2.5
            enemy_y_pos[i] += enemy_y_pos_change[i]
        elif enemy_x_pos[i] >= 736:
            enemy_x_pos_change[i] = -2.5
            enemy_y_pos[i] += enemy_y_pos_change[i]

        # Collision
        collision = detect_collision(enemy_x_pos[i], enemy_y_pos[i], missile_x_pos, missile_y_pos)
        if collision:
            missile_y_pos = 480
            missile_state = "ready"
            how_dare_you = mixer.Sound("how_dare_you.wav")
            how_dare_you.play()
            score_value += 1
            enemy_x_pos[i] = random.randint(64, 735)
            enemy_y_pos[i] = random.randint(50, 180)
        create_enemy(enemy_x_pos[i], enemy_y_pos[i])

    # Missile movement
    if missile_y_pos <= 0:
        missile_y_pos = 480
        missile_state = "ready"
    if missile_state is "fire":
        fire_missile(missile_x_pos, missile_y_pos)
        missile_y_pos -= missile_y_pos_change




    create_player(player_x_pos, player_y_pos)
    show_score(score_pos_x, score_pos_y)


    pygame.display.update()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


