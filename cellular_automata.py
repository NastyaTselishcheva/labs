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
        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
                if random.randint(1, 100) <= life_fraction:
                    self.field[y][x] = 1

    def run_transition_rule(self):
        """
        Метод реализует правило B3/S23
        :return: None
        """
        # buffer field
        buffer_field = [[0] * len(self.field[0]) for _ in range(len(self.field))]

        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
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
        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]

    def get_alive_cells_count(self):
        """
        Подсчёт живых клеток
        :return:
        integer
        """
        live_cells_counter = 0
        for line in self.field:
            live_cells_counter += line.count(1)
        return live_cells_counter


class Diameba(GameOfLife):
    """
        Данный класс реализует «Жизнь», основанную на правиле B35678/S5678,
        т.е. для рождения клетки (Birth) требуется от 3, 5, 6, 7, 8 живых соседей,
        для выживания (Survival) – от 5 до 8.
        Во всех других случаях клетка умирает (или же остаётся пустой).
        """

    def run_transition_rule(self):
        """
        Метод реализует правило B35678/S5678
        :return: None
        """
        # buffer field
        buffer_field = [[0] * len(self.field[0]) for _ in range(len(self.field))]

        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
                live_neighbors = 0
                # 3x3 - find neighbors
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if self.field[y + dy][x + dx] == 1:
                            live_neighbors += 1

                # life conditions rule
                if live_neighbors in [0, 1, 2, 4]:
                    buffer_field[y][x] = 0
                elif live_neighbors in [3, 5, 6, 7, 8]:
                    buffer_field[y][x] = 1
                else:
                    buffer_field[y][x] = self.field[y][x]
        # copy field
        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]


class LiveOrDie(GameOfLife):
    """
        Данный класс реализует «Жизнь», основанную на правиле B2/S0,
    """

    def initialize(self, life_fraction):
        # ограничить начало центром поля
        begin = 2 * len(self.field) // 5
        end = 3 * len(self.field) // 5
        for y in range(begin, end):
            for x in range(begin, end):
                if random.randint(1, 100) <= life_fraction:
                    self.field[y][x] = 1

    def run_transition_rule(self):
        """
        Метод реализует правило B2/S0
        :return: None
        """
        # buffer field
        buffer_field = [[0] * len(self.field[0]) for _ in range(len(self.field))]

        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
                live_neighbors = 0
                # 3x3 - find neighbors
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if self.field[y + dy][x + dx] == 1:
                            live_neighbors += 1

                # life conditions rule
                if live_neighbors in [1, 3, 4, 5, 6, 7, 8]:
                    buffer_field[y][x] = 0
                elif live_neighbors == 2:
                    buffer_field[y][x] = 1
                else:
                    buffer_field[y][x] = self.field[y][x]
        # copy field
        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]


class PersianCarpet(GameOfLife):
    """
        Данный класс реализует «Жизнь», основанную на правиле B234/S,
    """

    def initialize(self, life_fraction):
        # ограничить начало 4-мя клетками в центре поля
        middle = len(self.field) // 2
        self.field[middle][middle] = 1
        self.field[middle + 1][middle] = 1
        self.field[middle][middle + 1] = 1
        self.field[middle + 1][middle + 1] = 1

    def run_transition_rule(self):
        """
        Метод реализует правило B234/S
        :return: None
        """
        # buffer field
        buffer_field = [[0] * len(self.field[0]) for _ in range(len(self.field))]

        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
                live_neighbors = 0
                # 3x3 - find neighbors
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if dx == 0 and dy == 0:
                            continue
                        if self.field[y + dy][x + dx] == 1:
                            live_neighbors += 1

                # life conditions rule
                if live_neighbors in [2, 3, 4]:
                    buffer_field[y][x] = 1
                elif live_neighbors not in [2, 3, 4]:
                    buffer_field[y][x] = 0
                else:
                    buffer_field[y][x] = self.field[y][x]
        # copy field
        for y in range(0, len(self.field) - 1):
            for x in range(0, len(self.field[0]) - 1):
                self.field[y][x] = buffer_field[y][x]
