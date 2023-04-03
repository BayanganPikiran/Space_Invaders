import pygame

pygame.init()

SCREEN_DIM = (600, 600)

screen = pygame.display.set_mode(SCREEN_DIM)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


