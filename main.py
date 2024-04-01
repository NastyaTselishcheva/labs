from cellular_automata import *


def render_field(field):
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == 0:
                print(' ', end='')
            elif field[y][x] == 1:
                print('*', end='')
        print()
    print('-' * len(field))


def main():
    gof = GameOfLife(30, 30)
    gof.initialize(30)
    for i in range(30):
        gof.run_transition_rule()
        render_field(gof.field)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
