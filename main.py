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


def render_pygame(field, scale, screen):
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (x * scale, y * scale, scale, scale))
            elif field[y][x] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (x * scale, y * scale, scale, scale))

            pygame.draw.rect(screen, (0, 0, 0), (x * scale, y * scale, scale, scale), 2)


def main():
    field_size = int(input(" Введите размер поля(одно число): "))
    living_cells_proportion = int(input(" Введите пористость: "))
    cells_size = int(input(" Введите размер пикселя: "))
    type_of_game = int(input(" Выберите тип игры:\n1 - B3/S23\n2 - B35678/S5678\n3 - B2/S0\n4 - B234/S:"))
    if type_of_game == 1:
        gof = GameOfLife(field_size, field_size)
    elif type_of_game == 2:
        gof = Diameba(field_size, field_size)
    elif type_of_game == 3:
        gof = LiveOrDie(field_size, field_size)
    elif type_of_game == 4:
        gof = PersianCarpet(field_size, field_size)
    else:
        print('Unknown type - exit')
        exit(0)
    gof.initialize(living_cells_proportion)

    pygame.init()
    window_size = (field_size * cells_size, field_size * cells_size)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Game of Life")
    clock = pygame.time.Clock()
    # Let's play
    is_running = True
    # Pause variable
    is_paused = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            # keypress monitoring
            if event.type == pygame.KEYDOWN:
                # Space button for pause on/off
                if event.key == pygame.K_SPACE:
                    # invert boolean variable
                    is_paused = not is_paused
            if event.type == pygame.MOUSEBUTTONDOWN:
                cursor_pos = event.pos
                x_pos = cursor_pos[0] // cells_size
                y_pos = cursor_pos[1] // cells_size
                new_state = gof.field[y_pos][x_pos]
                if event.button == 1:
                    new_state = 1
                if event.button == 3:
                    new_state = 0
                gof.field[y_pos][x_pos] = new_state
        # if game not paused
        if not is_paused:
            gof.run_transition_rule()
        render_pygame(gof.field, cells_size, screen)
        pygame.display.flip()

        clock.tick(60)
        pygame.time.delay(200)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
