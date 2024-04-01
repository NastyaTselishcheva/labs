from cellular_automata import *
import pygame


def render_field(field):
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == 0:
                print(' ', end='')
            elif field[y][x] == 1:
                print('*', end='')
        print()
    print('-' * len(field))


def render_pygame(field, screen):
    scale = 15
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (x * scale, y * scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (x * scale, y * scale, scale, scale))

            pygame.draw.rect(screen, (0, 0, 0), (x * scale, y * scale, scale, scale), 2)


def main():
    gof = GameOfLife(30, 30)
    gof.initialize(30)

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        gof.run_transition_rule()
        render_pygame(gof.field, screen)
        pygame.display.flip()

        clock.tick(60)
        pygame.time.delay(200)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
