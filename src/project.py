import sys

import pygame


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Flower Farm")

    clock = pygame.time.Clock()
    dt = 0
    
    grass_tile = pygame.image.load("assets/ground_sprites/grass_tile.png").convert_alpha()

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        # Game Logic

        # Tiled Background
        for x in range(0, SCREEN_WIDTH, grass_tile.get_width()):
            for y in range(0, SCREEN_HEIGHT, grass_tile.get_height()):
                screen.blit(grass_tile, (x, y))
        # Render & Display
        pygame.display.flip()
        # Maintain FPS
        dt = clock.tick(24)
    pygame.quit()


if __name__ == "__main__":
    main()
