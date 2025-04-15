import support

import sys

import pygame


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Player():

    def __init__(self, pos):

        self.import_assets()
        self.status = 'down'
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center = pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 25

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
                           'up_plant': [], 'down_plant': [], 'left_plant': [], 'right_plant': []}
        for animation in self.animations.keys():
            full_path = 'assets/character_sprites/' + animation
            self.animations[animation] = support.import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 1 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0
    
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # Horizontal Movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # Vertical Movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)

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
        dt = clock.tick() / 100
    pygame.quit()


if __name__ == "__main__":
    main()
