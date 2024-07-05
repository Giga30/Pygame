import pygame
import constants
from character import Character
from weapon import Weapon

pygame.init()

screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
clock = pygame.time.Clock()

mob_animations = []
mob_types = ['big_demon', 'elf', 'goblin', 'imp', 'muddy', 'skeleton', 'tiny_zombie']

def scale_image(image, scale):
    w = image.get_width()
    h = image.get_height()
    return pygame.transform.scale(image, (w * scale, h * scale))

for k in range(len(mob_types)):
    animation_types = ['idle', 'run']

    animation_list = []
    for j in range(len(animation_types)):
        temp_list = []
        for i in range(4):
            image = pygame.image.load(f'starter_files\\assets\\images\\characters\\{mob_types[k]}\\{animation_types[j]}\\{i}.png').convert_alpha()
            image = scale_image(image, constants.SCALE)
            temp_list.append(image)
        animation_list.append(temp_list)
    mob_animations.append(animation_list)

player = Character(100, 100, mob_animations, 1)
bow = Weapon(scale_image(pygame.image.load('starter_files\\assets\\images\\weapons\\bow.png').convert_alpha(), constants.WEAPON_SCALE))
player_speed = 200

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    player_movement_vector = pygame.Vector2(0, 0)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player_movement_vector.x = -1
    if keys[pygame.K_d]:
        player_movement_vector.x = 1
    if keys[pygame.K_w]:
        player_movement_vector.y = -1
    if keys[pygame.K_s]:
        player_movement_vector.y = 1

    screen.fill(constants.BG)
    dt = clock.tick(constants.FPS)/1000

    player.draw(screen)
    bow.draw(screen)

    player.update()
    bow.update(player)
    player.move(player_movement_vector, dt, constants.SPEED, keys)

    pygame.display.update()                                                     
    after_frame_time = pygame.time.get_ticks()

pygame.quit()