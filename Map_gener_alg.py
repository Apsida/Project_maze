from random import choice

class Maze:
    def __init__(self, size):
        self.size = size
        self.h_arr = []
        self.v_arr = []
        self.line = []
        self.set_arr = []

    def generate(self):
        self.creat_line()
        for j in range(self.size):
            self.assign_set()
            self.add_ver_wall()
            self.add_hor_wall()
            self.check_hor_wall(j)
            self.prepare_new_line(j)
        self.end_gen()

    def creat_line(self):   #создаём пустую линию в которой ни одна ячеёка не принадлежит ни одному множеству
        self.line = []
        for i in range(self.size):
            self.line.append(None)

    def assign_set(self):
        count = 1   #счётчик генерации уникальных множеств
        for i in range(self.size):
            if self.line[i] == None:
                self.line[i] = count
                count += 1

    def add_ver_wall(self):
        vert_wall = [0]*self.size
        for i in range(self.size):
            choose = choice([True, False])  #выбираем ставить стенку или нет
            if choose == True or i == self.size-1 or self.line[i] == self.line[i+1]:    #если ячейка - правая граница или текущая ячейка и ячейка справа принадлежат одному множеству (для предотвращения зацикливаний)
                vert_wall[i] = 1
            else:
                self.line[i+1] = self.line[i]   #объединяем эелементы разным множеств в случае если не ставим стенку
        self.v_arr.append(vert_wall)

    def _calc_size_set(self, set_name):
        count = 0
        for i in range(self.size):
            if self.line[i] == set_name:
                count +=1
        return count > 1

    def add_hor_wall(self):
        hor_wall = [0] * self.size
        for i in range(self.size):
            choose = choice([True, False])
            if choose == True and self._calc_size_set(self.line[i]) == True:    #Ставим стенку если у данного множества более 1 элемента
                hor_wall[i] = 1
        self.h_arr.append(hor_wall)

    def _calc_hor_wall(self, row, set_name):
        count = 0
        for i in range(self.size):
            if self.line[i] == set_name and self.h_arr[row][i] == 0:
                count += 1
        return count

    def check_hor_wall(self, row):
        for i in range(self.size):
            if self._calc_hor_wall(row, self.line[i]) == 0:
                self.h_arr[row][i] = 0

    def prepare_new_line(self, row):
        self.set_arr.append(self.line)      #сохраняем строку множеств
        for i in range(self.size):
            if self.h_arr[row][i] == 1:     #все ячейки под стенками удаляем из множеств
                self.line[i] = None

    def end_gen(self):
        self.h_arr[self.size-1] = [1]*self.size
        for i in range(self.size-1):
            if self.line[i] != self.line[i+1]:
                self.v_arr[self.size-1][i] = 0
                self.line[i] = self.line[i + 1]

if __name__ == "__main__":
    s = 5
    m = Maze(s)
    m.generate()
    for i in range(s):
        print(m.v_arr[i])
    print()
    for i in range(s):
        print(m.h_arr[i])
