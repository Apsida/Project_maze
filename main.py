from Map_gener_alg import *
from tkinter import *

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
        print(self.size)

    def start_app(self):
        root = Tk()
        root.title("Maze app")
        root.geometry("900x700")

        name = Label(text="Maze size: Len x Width")
        name.pack(anchor=NW)
        frame = Frame(borderwidth=1, relief=SOLID)
        self.lenght = Entry(frame, width=10)
        self.width = Entry(frame, width=10)
        self.lenght.pack(side=LEFT)
        self.width.pack(side=LEFT)
        accept_btn = Button(frame, text="accept", command=self._set_size)
        accept_btn.pack()
        frame.pack(anchor=NW)

        root.mainloop()


class Object:
    def __init__(self, name, count):
        self.name = name
        self.count = count


if __name__ == "__main__":
    m = Map()
    m.start_app()