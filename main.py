
from Map_gener_alg import *
import pickle
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror

class Map:
    def __init__(self, size=(0,0), arr_object=[]):
        self.size = size
        self.arr_object = arr_object
        self.map = Maze(self.size)

    def init_maze(self):
        self.map = Maze(self.size)
        self.map.generate()

    def add_obj(self):
        self.map.add_object(self.arr_object)

    def unite_wall_floor(self):
        arr = []
        for i in range(self.size[0]*2):
            arr.append([0]*self.size[1]*2)

        for i in range(self.size[0]*2):
            for j in range(1, self.size[1]*2, 2):
                #добавляем горизонтальные и вертикальные стенки
                if i%2 != 0 and self.map.h_arr[i//2][j//2]:
                    arr[i][j] = "1"
                    arr[i][j-1]="1"
                elif i%2 == 0 and self.map.v_arr[i//2][j//2]:
                    arr[i][j] = "1"
                    arr[i+1][j] = "1"
                #добавляем элементы пола
                if i%2 == 0 and self.map.floor[i//2][j//2] != 0:
                    arr[i][j] = self.map.floor[i//2][j//2]
            arr[i][self.size[1]*2-1] = "1"
        return arr

    def _set_size(self):
        try:
            l = int(self.lenght.get())
            w = int(self.width.get())
            self.size = (l, w)
        except ValueError:
            showerror(title="Size_type_error",
                      message="Size of maze is incorrect")

    def _creat_obj_arr(self):
        string = self.obj_field.get("1.0", END)
        inp = string.split()
        self.arr_object=[]
        summ_of_count = 0
        if len(inp)%2 != 0:
            showerror(title="Obj_array_size_error",
                      message="Count of parameters is incorrect")
        for i in range(0, len(inp)-1, 2):
            try:
                int(inp[i+1])
            except ValueError:
                showerror(title="Obj_param_type_error",
                          message=("Count of object is incorrect. Error in line: " + str(i + 1)))
            if type(inp[i]) != str:
                showerror(title="Obj_param_type_error",
                          message=("Name is incorrect. Error in line: " + str(i + 1)))
                break
            summ_of_count += int(inp[i+1])
            self.arr_object.append(Object(inp[i], int(inp[i+1])))

        if summ_of_count > (self.size[0]*self.size[1]):
            self.arr_object = []
            showerror(title="Obj_param_count_error",
                      message=("The number of objects exceeds the size of the field"))

    def _build_map(self):
        self.canv.delete("all")
        x = 0
        y = 0
        m_arr = self.unite_wall_floor()
        print(m_arr)
        for k in m_arr:
            for q in k:
                if q == '1':
                    self.canv.create_rectangle(x, y, x + 10, y + 10, fill='black', outline='black')
                elif q != 0 and q != "1":
                    self.canv.create_text(x+5, y+3, text=q)
                x += 10
            x = 0
            y += 10
        print("buildet")

    def start_app(self):
        root = Tk()
        root.title("Maze app")
        root.geometry("900x700")

        name =Label(text="Help info\nx mean space\n")
        self.canv = Canvas(bg="white", width=650, height=650)
        self.canv.pack(anchor=E, side=LEFT)
        name.pack(anchor=NW, side=TOP)

        #создаём первое поле для ввода настроек размера
        name = Label(text="Size of maze: lenght x width")
        name.pack(anchor=NW)
        frame1 = Frame(borderwidth=1, relief=SOLID)
        self.lenght = Entry(frame1, width=10)
        self.width = Entry(frame1, width=10)
        self.lenght.pack(side=LEFT)
        self.width.pack(side=LEFT)
        accept_btn = Button(frame1, text="accept", command=self._set_size)
        accept_btn.pack(fill=X)
        frame1.pack(anchor=NW)

        # создаём второе поле для ввода объектов
        frame2 = Frame(borderwidth=1, relief=SOLID)
        name = Label(frame2, text= "Object to add (1 obj - 1 line)\nName x Count")
        name.pack(anchor=NW)
        self.obj_field = ScrolledText(frame2, wrap="none", width=20, height=10)
        self.obj_field.pack()
        accept_btn = Button(frame2, text="accept", command=self._creat_obj_arr)
        accept_btn.pack(fill=X)
        frame2.pack(anchor=W)

        # создаём третье поле с основными кнопками работы с лабиринтом
        frame3 = Frame(borderwidth=1, relief=SOLID)
        gener_btn = Button(frame3, text="generate map", command= lambda: [self.init_maze(), self.add_obj()])
        gener_btn.pack(fill=X)
        view_btn = Button(frame3, text="view map", command= self._build_map)
        view_btn.pack(fill=X)
        # save_btn = Button(frame3, text="save map")
        # save_btn.pack(fill=X)
        frame3.pack(anchor=W)

        root.mainloop()

class Object:
    def __init__(self, name, count):
        self.name = name
        self.count = count
        self.id = 0

def save_data(obj, n_file):
    with open(n_file+".pickle", "wb") as file:
        pickle.dump(obj, file)

def load_data(n_file):
    with open(n_file+".pickle", "rb") as file:
        obj = pickle.load(file)
    return obj

if __name__ == "__main__":
    m = Map()
    m.start_app()