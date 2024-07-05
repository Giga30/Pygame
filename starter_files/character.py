import pygame
import constants

class Character():
    def __init__(self, x, y, mob_animations, char_type):
        self.animation_list = mob_animations[char_type]
        self.char_type = char_type
        self.frame_index = 0
        self.running = False
        self.action = 0
        self.last_frame_ticks = pygame.time.get_ticks()
        self.rect = pygame.Rect(0, 0, 40, 40)
        self.rect.center = (x, y)
        self.image = self.animation_list[self.action][self.frame_index]
        self.flipped = False

    def draw(self, surface):

        flipped_image = pygame.transform.flip(self.image, self.flipped, False)
        if self.char_type == 1:
            surface.blit(flipped_image, (self.rect.x, self.rect.y - constants.OFFSET * constants.SCALE))
        else:    
            surface.blit(flipped_image, self.rect)
        pygame.draw.rect(surface, constants.RED, self.rect, 1)
    
    def update(self):
        frame_cooldown = 70
        self.update_action(self.action)
        self.image = self.animation_list[self.action][self.frame_index]
        if (pygame.time.get_ticks() - self.last_frame_ticks) >= frame_cooldown:
            if self.frame_index >= len(self.animation_list[self.action]) - 1:
                self.frame_index = 0
            else:
                self.frame_index += 1
            self.last_frame_ticks = pygame.time.get_ticks()

    def move(self, movement_vector, dt, speed, keys):
        if (keys[pygame.K_a] and keys[pygame.K_d]):
            movement_vector.x = 0
        if (keys[pygame.K_w] and keys[pygame.K_s]):
            movement_vector.y = 0

        if movement_vector.length() > 0:
            movement_vector = movement_vector.normalize()
            self.running = True
        else:
            self.running = False

        if movement_vector.x < 0:
            self.flipped = True
        elif movement_vector.x > 0:
            self.flipped = False

        self.rect.x += movement_vector.x * dt * speed
        self.rect.y += movement_vector.y * dt * speed

    def update_action(self, last_action):
        if self.running:
            self.action = 1
        else:
            self.action = 0
        if self.action != last_action:        
            self.frame_index = 0
            self.last_frame_ticks = pygame.time.get_ticks()