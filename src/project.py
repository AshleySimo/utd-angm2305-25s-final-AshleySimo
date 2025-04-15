import sys

import pygame


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Player():

    def __init__(self, pos):

        self.image = pygame.Surface((32, 64))
        self.image.fill('black')
        self.rect = self.image.get_rect(center = pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 0.25 # milliseconds

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def move(self, dt):
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def update(self, dt):
        self.input()
        self.move(dt)

    def draw(self, screen):
        screen.blit(self.image, self.pos)



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flower Farm")

    clock = pygame.time.Clock()
    dt = 0
    
    grass_tile = pygame.image.load("assets/ground_sprites/grass_tile.png").convert_alpha()

    player = Player((320, 240))

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        # Game Logic
        player.update(dt)
        # Tiled Background
        for x in range(0, SCREEN_WIDTH, grass_tile.get_width()):
            for y in range(0, SCREEN_HEIGHT, grass_tile.get_height()):
                screen.blit(grass_tile, (x, y))
        player.draw(screen)
        # Render & Display
        pygame.display.flip()
        # Maintain FPS
        dt = clock.tick(24)
    pygame.quit()


if __name__ == "__main__":
    main()
