import support

import sys

import pygame


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
TILE_SIZE = 64

class Player():

    def __init__(self, pos=(320, 240)):

        self.import_assets()

        self.status = 'down'
        self.frame_index = 0

        self.image = self.animations[self.status][self.frame_index] 
        
        self.rect = self.image.get_rect(center = pos)
        self.rect.center = pos
        self.hitbox = self.rect.copy().inflate((-32, -64))

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2((pos[0]-32, pos[1]-64))
        self.speed = 20

        self.timers = {'tool use': support.Timer(350, self.use_tool)}

        self.selected_tool = 'plant'
        self.selected_seed = 'flower'
        
        self.soil_layer = SoilLayer()

    def use_tool(self):
        pass

    def import_assets(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], 
                           'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
                           'up_plant': [], 'down_plant': [], 'left_plant': [], 'right_plant': []}
        for animation in self.animations.keys():
            full_path = 'assets/character_sprites/' + animation
            self.animations[animation] = support.import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 0.5 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0

        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()
        if not self.timers['tool use'].active:
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

            if keys[pygame.K_c]:
                self.timers['tool use'].activate()
                self.direction = pygame.math.Vector2()
                self.frame_index = 0
                self.soil_layer.plant_seed(self.hitbox)
        
    def get_status(self):
        if self.direction.magnitude() == 0:
            self.status = self.status.split('_')[0] + '_idle'

        if self.timers['tool use'].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()
    
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        # Horizontal Movement
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hitbox.centerx
        # Vertical Movement
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self.rect.centery = self.hitbox.centery

    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)

    def draw(self, screen):
        screen.blit(self.image, self.pos)

class SoilLayer:

    def __init__(self):
        self.sprite = pygame.image.load('assets/ground_sprites'
        '/grass_tile.png').convert_alpha()

        self.create_soil_grid()
        self.create_hit_rects()

    def create_soil_grid(self):
        h_tiles = SCREEN_WIDTH // TILE_SIZE
        v_tiles = SCREEN_HEIGHT // TILE_SIZE
        
        self.grid = [[['F'] for col in range(h_tiles)] for row in range(v_tiles)]
        
    def create_hit_rects(self):
        self.hit_rects = []
        for idx_row, row in enumerate(self.grid):
            for idx_col, cell in enumerate(row):
                if 'F' in cell:
                    x = idx_col * TILE_SIZE
                    y = idx_row * TILE_SIZE
                    rect = pygame.Rect(x, y, TILE_SIZE//2, TILE_SIZE//2)
                    self.hit_rects.append(rect)
    
    def plant_seed(self, hitbox):
        for rect in self.hit_rects:
            if rect.colliderect(hitbox):
                x = rect.x // TILE_SIZE
                y = rect.y // TILE_SIZE
                if 'P' not in self.grid[y][x]:
                    self.grid[y][x].append('P')
                    rect_surface = pygame.Surface((rect.w, rect.h))
                    plant = Plant(rect)
                    plant.draw(rect_surface)
                    print('plant')

    def draw(self, screen):
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
                screen.blit(self.sprite, (x, y))

class Plant:

    def __init__(self, soil):
        self.frames = support.import_folder(f'assets/plant_sprites')
        self.soil = soil
        # self.soil_rect = pygame.Surface.get_rect(self.soil)

        # self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), 
                                    #   pygame.SRCALPHA)
        self.age = 0
        self.max_age = len(self.frames) - 1
        self.grow_speed = 5

        self.image = pygame.image.load('assets/plant_sprites/0.png').convert_alpha()
        # self.y_offset = -16
        self.rect = pygame.Surface.get_rect(self.image)

    def draw(self, screen):
        screen.blit(self.image, (self.soil.x, self.soil.y))
      

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flower Farm")

    clock = pygame.time.Clock()
    dt = 0

    soil = SoilLayer()
    player = Player(pos=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
    # plant = Plant(player.selected_seed, soil.sprite)

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()


        # Game Logic
        player.update(dt)
        # Render & Display
        soil.draw(screen)
        # plant.draw(screen)
        player.draw(screen)
        # Render & Display
        pygame.display.flip()
        # Maintain FPS
        dt = clock.tick(24) / 100
    pygame.quit()


if __name__ == "__main__":
    main()
