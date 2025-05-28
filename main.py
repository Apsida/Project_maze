import tkinter

from Map_gener_alg import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import showerror

class Map:
    def __init__(self, size=(0,0), arr_object=[]):
        self.size = size
        self.arr_object = arr_object

    def init_maze(self):
        self.map = Maze(self.size)
        self.map.generate()

    def add_obj(self):
        self.map.add_object(self.arr_object)

    def _set_size(self):
        self.size = (self.lenght.get(), self.width.get())

    def _creat_obj_arr(self):
        string = self.obj_field.get("1.0",tkinter.END)
        inp = string.split()
        self.arr_object=[]
        if len(inp)%2 != 0:
            showerror(title="Obj_array_size_error",
                      message="Count of parameters is incorrect")
        for i in range(0, len(inp)-1, 2):
            if type(inp[i]) != str or type(inp[i+1]) != int:
                showerror(title="Obj_param_type_error",
                          message=("Parameters type is incorrect. Error in line: " + str(i+1)))
                break
            self.arr_object.append(Object(inp[i], inp[i+1]))

    def start_app(self):
        root = Tk()
        root.title("Maze app")
        root.geometry("900x700")

        name =Label(text="Help info\nx mean space\n")
        name.pack(anchor=NW)

        #создаём первое поле для ввода настроек размера
        name = Label(text="Size of maze: lenght x width")
        name.pack(anchor=NW)
        frame1 = Frame(borderwidth=1, relief=SOLID)
        self.lenght = Entry(frame1, width=10)
        self.width = Entry(frame1, width=10)
        self.lenght.pack(side=LEFT)
        self.width.pack(side=LEFT)
        accept_btn = Button(frame1, text="generate_map", command=self._set_size)
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
        gener_btn = Button(frame3, text="generate map", command= lambda: [self.init_maze, self.add_obj])
        gener_btn.pack(fill=X)
        view_btn = Button(frame3, text="view map")
        view_btn.pack(fill=X)
        save_btn = Button(frame3, text="save map")
        save_btn.pack(fill=X)
        frame3.pack(anchor=W)

        root.mainloop()


class Object:
    def __init__(self, name, count):
        self.name = name
        self.count = count


if __name__ == "__main__":
    m = Map()
    m.start_app()