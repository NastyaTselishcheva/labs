class Disolving:
    """
    Класс для имитации растворения твердого тела
    """

    def __init__(self, diameter):
        """
        Конструктор класса
        :param diameter:
        Диаметр сосуда, в котором будет растворение
        """
        self.field = [[-1] * diameter for _ in range(diameter)]
        # Коэффициент растворения
        self.k = 0.3
        # Коэффициент диффузии
        self.d = 0.001

    def initialize(self, pill_diameter):
        """
        Инициализация поля со значениями клеток:
        -1 - не относится к полу
        0 - 100 - концентрация в процентах
        :param pill_diameter:
        диаметр растворяющегося тела (таблетки)
        :return:
        """

        begin = len(self.field) // 2 - pill_diameter // 2
        end = len(self.field) // 2 + pill_diameter // 2
        for y in range(begin, end):
            for x in range(begin, end):
                dx = abs(len(self.field[0]) // 2 - x)
                dy = abs(len(self.field) // 2 - y)
                if dx ** 2 + dy ** 2 < (pill_diameter // 2) ** 2:
                    self.field[y][x] = 100

    def run_transition_rule(self):
        """
        Принимаем значение насыщенного раствора - 50 процентов.
        Твердое тело - > 50
        Раствор <= 50
        :return:
        """
        # buffer field
        # buffer_field = [[0] * len(self.field[0]) for _ in range(len(self.field))]
        for y in range(1, len(self.field) - 1):
            for x in range(1, len(self.field[0]) - 1):
                # Просмотр соседей по вертикали и горизонтали, выбор самых концентрированных
                # рассчёт средней концентрации и увеличение ее в текущей с уменьшением в соседях
                neighbors = []
                csum = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if abs(dx) == abs(dy):  # исключаем диагонали
                            continue
                        if self.field[y + dy][x + dx] > self.field[y][x]:
                            csum += self.field[y + dy][x + dx]
                            neighbors.append((dx, dy))
                aver = csum / len(neighbors) if len(neighbors) else 0
                delta = int(self.k * abs(self.field[y][x] - aver))
                self.field[y][x] += delta
                if self.field[y][x] > 100:
                    self.field[y][x] = 100
                for dx, dy in neighbors:
                    self.field[y + dy][x + dx] -= delta
                    if self.field[y + dy][x + dx] < 0:
                        self.field[y + dy][x + dx] = 0
