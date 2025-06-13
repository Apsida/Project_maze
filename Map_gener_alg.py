import random


class Maze:
    def __init__(self, size):
        self.size = size
        self.floor = []
        self.h_arr = []
        self.v_arr = []
        self.line = []
        self.set_arr = []
        self.set_num = 0  # счётчик генерации уникальных множеств

    def generate(self):
        self.creat_line()
        self._fill_floor()
        for j in range(self.size[0]):
            self.assign_set()
            self.add_vertical_wall()
            self.add_horizontal_wall()
            self.check_horizontal_wall(j)
            self.prepare_new_line(j)
        self.end_gen()

    def _fill_floor(self):
        for i in range(self.size[0]):
            self.floor.append([0] * self.size[1])

    def creat_line(self):  # создаём пустую линию в которой ни одна ячеёка не принадлежит ни одному множеству
        self.line = []
        for i in range(self.size[1]):
            self.line.append(None)

    def assign_set(self):
        for i in range(self.size[1]):
            if self.line[i] == None:
                self.line[i] = self.set_num
                self.set_num += 1

    def add_vertical_wall(self):
        vert_wall = [0] * self.size[1]
        for i in range(self.size[1]):
            choose = random.choice([True, False])  # выбираем ставить стенку или нет
            # если ячейка - правая граница или текущая ячейка и ячейка справа принадлежат одному множеству (для предотвращения зацикливаний)
            if choose == True or i == self.size[1] - 1 or self.line[i] == self.line[i + 1]:
                vert_wall[i] = 1
            else:
                # объединяем эелементы разным множеств в случае если не ставим стенку
                self.line[i + 1] = self.line[i]
        self.v_arr.append(vert_wall)

    def _calc_size_set(self, set_name):
        count = 0
        # считаем сколько элементов в линии принадлежит данному множеству
        for i in range(self.size[1]):
            if self.line[i] == set_name:
                count += 1
        return count > 1

    def add_horizontal_wall(self):
        hor_wall = [0] * self.size[1]
        for i in range(self.size[1]):
            choose = random.choice([True, False])
            # Ставим стенку если у данного множества более 1 элемента
            if choose == True and self._calc_size_set(self.line[i]) == True:
                hor_wall[i] = 1
        self.h_arr.append(hor_wall)

    def _calc_horizontal_wall(self, row, set_name):
        count = 0
        # считаем сколько элементов в линии принадлежит данному множеству и при этом не стоит горизонтальная стенка
        for i in range(self.size[1]):
            if self.line[i] == set_name and self.h_arr[row][i] == 0:
                count += 1
        return count

    def check_horizontal_wall(self, row):
        for i in range(self.size[1]):
            if self._calc_horizontal_wall(row, self.line[i]) == 0:
                self.h_arr[row][i] = 0

    def prepare_new_line(self, row):
        self.set_arr.append(self.line.copy())  # сохраняем строку множеств
        for i in range(self.size[1]):
            if self.h_arr[row][i] == 1:  # все ячейки под стенками удаляем из множеств
                self.line[i] = None

    def end_gen(self):
        self.h_arr[self.size[0] - 1] = [1] * self.size[1]
        self.v_arr[self.size[0] - 1] = [0] * self.size[1]

    # обходим лабиринт, размещая объекты
    def _bypass(self, count, name):
        while count > 0:
            x = random.randint(0, self.size[0] - 1)
            y = random.randint(0, self.size[1] - 1)

            if self.floor[y][x] == 0:
                self.floor[y][x] = name
                count -= 1

    def add_object(self, arr_obj):
        id_count = 2  # счётчик для присовения id
        for i in arr_obj:
            i.id = id_count
            self._bypass(i.count, i.id)
            id_count += 1


if __name__ == "__main__":
    m = Maze((3, 5))
    m.generate()
