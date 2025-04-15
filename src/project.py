import sys

import pygame


SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


def main():
    pygame.init()
    pygame.display.set_caption("Flower Farm")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    running = True
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        # Game Logic

        # Render & Display
        pygame.display.flip()
        dt = clock.tick(24)
    pygame.quit()


if __name__ == "__main__":
    main()
