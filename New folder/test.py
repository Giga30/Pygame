import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
player_rect = pygame.Rect(screen.get_width() / 2, screen.get_height() / 2, 50, 50)
object_rect = pygame.Rect(0, 0, 50, 50)
speed = 500
fps = 60
player_color = 'blue'


image = pygame.image.load('C:\\Users\\kurta\\Desktop\\Pygame\\New folder\\Icon1_no_effect.png').convert()
bow_rect = image.get_rect()
bow_rect.center = (player_rect.centerx -10, player_rect.centery) 

before_frame_time = pygame.time.get_ticks()

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    after_frame_time = pygame.time.get_ticks()
    mouse_pos = pygame.mouse.get_pos()
    print(mouse_pos)
    dt = (after_frame_time - before_frame_time) / 1000
    screen.fill('purple')
    keys = pygame.key.get_pressed()


    move_vector = pygame.Vector2(0, 0)

    if keys[pygame.K_a]:
        move_vector.x = -1
    if keys[pygame.K_d]:
        move_vector.x = 1
    if keys[pygame.K_w]:
        move_vector.y = -1
    if keys[pygame.K_s]:
        move_vector.y = 1

    if keys[pygame.K_a] and keys[pygame.K_d]:
        move_vector.x = 0
    if keys[pygame.K_w] and keys[pygame.K_s]:
        move_vector.y = 0


    if move_vector.length() > 0:
        move_vector = move_vector.normalize()
        print(move_vector)
        player_rect.x += move_vector.x * dt * speed
        player_rect.y += move_vector.y * dt * speed
    
    if player_rect.colliderect(object_rect):
        player_color = 'red'
    else:
        player_color = 'blue'

    triangle = (abs(player_rect[1] - mouse_pos[1]), abs(player_rect[0] - mouse_pos[0]))
    if triangle[1] == 0:
        theta = 0
    else:
        theta = math.atan(triangle[0]/triangle[1])
    pygame.draw.rect(screen, player_color, player_rect)
    pygame.draw.rect(screen, 'red', object_rect)
    screen.blit(pygame.transform.rotate(image, math.degrees(theta)), bow_rect)

    pygame.display.update()
    before_frame_time = pygame.time.get_ticks()
    clock.tick(fps)
pygame.quit()