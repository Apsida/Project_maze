from random import choice

class Maze:
    def __init__(self, size):
        self.size = size
        self.floor = []
        self.h_arr = []
        self.v_arr = []
        self.line = []
        self.set_arr = []
        self.set_num = 0 #счётчик генерации уникальных множеств

    def _fill_floor(self):
        for i in range(self.size[0]):
            self.floor.append([0]*self.size[1])

    def generate(self):
        self.creat_line()
        self._fill_floor()
        for j in range(self.size[0]):
            self.assign_set()
            self.add_ver_wall()
            self.add_hor_wall()
            self.check_hor_wall(j)
            self.prepare_new_line(j)
        self.end_gen()

    def creat_line(self):   #создаём пустую линию в которой ни одна ячеёка не принадлежит ни одному множеству
        self.line = []
        for i in range(self.size[1]):
            self.line.append(None)

    def assign_set(self):
        for i in range(self.size[1]):
            if self.line[i] == None:
                self.line[i] = self.set_num
                self.set_num += 1

    def add_ver_wall(self):
        vert_wall = [0]*self.size[1]
        for i in range(self.size[1]):
            choose = choice([True, False])  #выбираем ставить стенку или нет
            #если ячейка - правая граница или текущая ячейка и ячейка справа принадлежат одному множеству (для предотвращения зацикливаний)
            if choose == True or i == self.size[1]-1 or self.line[i] == self.line[i+1]:
                vert_wall[i] = 1
            else:
                # объединяем эелементы разным множеств в случае если не ставим стенку
                self.line[i+1] = self.line[i]
        self.v_arr.append(vert_wall)

    def _calc_size_set(self, set_name):
        count = 0
        #считаем сколько элементов в линии принадлежит данному множеству
        for i in range(self.size[1]):
            if self.line[i] == set_name:
                count +=1
        return count > 1

    def add_hor_wall(self):
        hor_wall = [0] * self.size[1]
        for i in range(self.size[1]):
            choose = choice([True, False])
            # Ставим стенку если у данного множества более 1 элемента
            if choose == True and self._calc_size_set(self.line[i]) == True:
                hor_wall[i] = 1
        self.h_arr.append(hor_wall)

    def _calc_hor_wall(self, row, set_name):
        count = 0
        for i in range(self.size[1]):
            if self.line[i] == set_name and self.h_arr[row][i] == 0:
                count += 1
        return count

    def check_hor_wall(self, row):
        for i in range(self.size[1]):
            if self._calc_hor_wall(row, self.line[i]) == 0:
                self.h_arr[row][i] = 0

    def prepare_new_line(self, row):
        self.set_arr.append(self.line.copy())      #сохраняем строку множеств
        for i in range(self.size[1]):
            if self.h_arr[row][i] == 1:     #все ячейки под стенками удаляем из множеств
                self.line[i] = None

    def end_gen(self):
        self.h_arr[self.size[0]-1] = [1]*self.size[1]
        print(len(self.v_arr))
        self.v_arr[self.size[0]-1] = [0]*self.size[1]

    #обходим лабиринт, размещая объекты
    def _bypass(self, count, name):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if count > 0 and self.floor[i][j] == 0 and choice([True, False]):
                    self.floor[i][j] = name
                    count -= 1

    def add_object (self, arr_obj):
        for i in arr_obj:
            self._bypass(i.count, i.name[0])

if __name__ == "__main__":
    m = Maze((3,5))
    m.generate()