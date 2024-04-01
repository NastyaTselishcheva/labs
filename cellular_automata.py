import random


class GameOfLife:
    """
    Данный класс реализует «Жизнь» Конвея, основанную на правиле B3/S23,
    т.е. для рождения клетки (Birth) требуется ровно 3 живых соседа,
    для выживания (Survival) – 2 или 3.
    Во всех других случаях клетка умирает (или же остаётся пустой).
    """
    def __init__(self, width, height):
        self.field = [[0] * width for _ in range(height)]

    def initialize(self, life_fraction):
        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                if random.randint(1, 100) <= life_fraction:
                    self.field[y][x] = 1

    def run_transition_rule(self):
        """
        Метод реализует правило B3/S23
        :return: None
        """
        # buffer field
        buffer_field = [[0] * len(self.field[0]) for _ in range(len(self.field))]

        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                live_neighbors = 0
                # 3x3 - find neighbors
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if self.field[y + dy][x + dx] == 1:
                            live_neighbors += 1

                # life conditions rule
                if live_neighbors < 2 or live_neighbors > 3:
                    buffer_field[y][x] = 0
                elif live_neighbors == 3:
                    buffer_field[y][x] = 1
                else:
                    buffer_field[y][x] = self.field[y][x]
        # copy field
        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]
