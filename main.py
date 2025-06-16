from Map_gener_alg import *
import pickle
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror


class Map:
    def __init__(self, size=(0, 0), arr_object=[]):
        self.size = size
        self.arr_object = arr_object
        self.map = Maze(self.size)

    def init_maze(self):
        try:
            high = int(self.size[0])
            width = int(self.size[1])
            if high == 0 or width == 0:
                raise
        except:
            print("type of size err. Size must be: (int, int)")
            return 1
        self.map = Maze(self.size)
        self.map.generate()

    def add_obj(self):
        summ_of_count = 0
        for i in self.arr_object:
            summ_of_count += i.count
        if summ_of_count >= self.size[0] * self.size[1]:
            print("ERROR: the number of objects exceeds the size of the map")
            return 1
        self.map.add_object(self.arr_object)

    def unite_wall_floor(self):
        if self.size[0] == 0 or self.size[1] == 0:
            return 1

        arr = []
        for i in range(self.size[0] * 2):
            arr.append([0] * self.size[1] * 2)

        for i in range(self.size[0] * 2):
            for j in range(1, self.size[1] * 2, 2):
                # добавляем горизонтальные и вертикальные стенки
                if i % 2 != 0 and self.map.h_arr[i // 2][j // 2]:
                    arr[i][j] = "1"
                    arr[i][j - 1] = "1"
                elif i % 2 == 0 and self.map.v_arr[i // 2][j // 2]:
                    arr[i][j] = "1"
                    arr[i + 1][j] = "1"
                # добавляем элементы пола
                if i % 2 == 0 and self.map.floor[i // 2][j // 2] != 0:
                    arr[i][j] = self.map.floor[i // 2][j // 2]
            arr[i][self.size[1] * 2 - 1] = "1"
        return arr

    def _set_size(self):
        try:
            l = int(self.lenght.get())
            w = int(self.width.get())
            self.size = (l, w)
        except ValueError:
            showerror(title="Size_type_error",
                      message="Size of maze is incorrect")

    def _create_obj_arr(self):
        string = self.obj_field.get("1.0", END)
        inp = string.split()
        self.arr_object = []
        summ_of_count = 0
        if len(inp) % 2 != 0:
            showerror(title="Obj_array_size_error",
                      message="Count of parameters is incorrect")
        for i in range(0, len(inp) - 1, 2):
            try:
                int(inp[i + 1])
            except ValueError:
                showerror(title="Obj_param_type_error",
                          message=("Count of object is incorrect. Error in line: " + str(i + 1)))
            if type(inp[i]) != str:
                showerror(title="Obj_param_type_error",
                          message=("Name is incorrect. Error in line: " + str(i + 1)))
                break
            summ_of_count += int(inp[i + 1])
            self.arr_object.append(Object(inp[i], int(inp[i + 1])))

        if summ_of_count > (self.size[0] * self.size[1]):
            self.arr_object = []
            showerror(title="Obj_param_count_error",
                      message=("The number of objects exceeds the size of the field"))

    def _object_id_output(self):
        arr_id = "id of Your object:\n"
        for i in self.arr_object:
            arr_id = arr_id + i.name + "- " + str(i.id) + "\n"
        self.obj_id.config(text=arr_id)

    def _build_map(self):
        self.canvas.delete("all")
        x = 0
        y = 0
        m_arr = self.unite_wall_floor()
        if m_arr == 1:
            showerror(title="Generate error",
                      message=("You try to generate with wrong input data"))
            return 1
        for k in m_arr:
            for q in k:
                if q == '1':
                    self.canvas.create_rectangle(x, y, x + 10, y + 10, fill='black', outline='black')
                elif q != 0 and q != "1":
                    self.canvas.create_text(x + 5, y + 3, text=q)
                x += 10
            x = 0
            y += 10
        print("buildet")
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self._object_id_output()

    def start_app(self):
        root = Tk()
        root.title("Maze app")
        root.geometry("900x700")

        frame1 = Frame(borderwidth=1, relief=SOLID)

        # поле для вывода визуализации сгенерированного лабиринта
        self.canvas = Canvas(frame1, bg="white", width=700, height=700, scrollregion=(0, 0, 700, 600))
        hbar = Scrollbar(frame1, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=self.canvas.xview)
        vbar = Scrollbar(frame1, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=self.canvas.yview)
        self.canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        self.canvas.pack(side=RIGHT, expand=True, fill=BOTH)

        # меню для ввода параметров размера лабиринта
        name = Label(frame1, text="Size of maze: lenght x width")
        name.pack(anchor=NW)
        self.lenght = Entry(frame1, width=10)
        self.width = Entry(frame1, width=10)
        self.lenght.pack()
        self.width.pack()
        accept_btn = Button(frame1, text="apply", command=self._set_size)
        accept_btn.pack(fill=X)

        # меню для ввода параметров объектов
        name = Label(frame1, text="Object to add (1 obj - 1 line)\nName x Count")
        name.pack(anchor=NW)
        self.obj_field = ScrolledText(frame1, wrap="none", width=20, height=10)
        self.obj_field.pack()
        accept_btn = Button(frame1, text="apply", command=self._create_obj_arr)
        accept_btn.pack(fill=X)
        gener_btn = Button(frame1, text="generate map",
                           command=lambda: [self.init_maze(), self.add_obj(), self._build_map()])
        gener_btn.pack(fill=X)

        self.obj_id = Label(frame1)
        self.obj_id.pack(anchor=NW, side=LEFT)
        frame1.pack(anchor=NW, expand=True)

        root.mainloop()


class Object:
    def __init__(self, name, count):
        try:
            c = int(count)
        except:
            print("type of count error: count must be integer")
        self.name = name
        self.count = count
        self.id = 0


def save_data(obj, n_file):
    with open(n_file + ".pickle", "wb") as file:
        pickle.dump(obj, file)


def load_data(n_file):
    with open(n_file + ".pickle", "rb") as file:
        obj = pickle.load(file)
    return obj


if __name__ == "__main__":
    m = Map()
    m.start_app()
