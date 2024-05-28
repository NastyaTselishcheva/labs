import pygame
from disolving import *


def render_pygame(field, scale, screen):
    for y in range(len(field)):
        for x in range(len(field[0])):
            red_component = (255 * field[y][x] // 100) if field[y][x] >= 0 else 0
            cell_color = pygame.Color(red_component, 0, 0)
            pygame.draw.rect(screen, cell_color, (x * scale, y * scale, scale, scale))


def main():
    # Таблетка для растворения
    field_size = 150
    cells_size = 5
    pill_size = 40
    pill = Disolving(field_size)
    pill.initialize(pill_size)

    # Инициализация экрана
    pygame.init()
    windows_size_x = field_size * cells_size
    windows_size_y = field_size * cells_size
    window_size = (windows_size_x, windows_size_y)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Disolving imitation")
    screen_clock = pygame.time.Clock()

    # Начало имитации
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            # итерация растворения
            pill.run_transition_rule()
            render_pygame(pill.field, cells_size, screen)
            # перерисовка поля
            pygame.display.flip()
            screen_clock.tick()
            pygame.time.delay(200)


if __name__ == '__main__':
    main()
