from Map_gener_alg import *

class Map:
    def __init__(self, size, arr_object):
        self.size = size
        self.arr_object = arr_object
        self.map = Maze(size)
        self.map.generate()

    def add_obj(self):
        self.map.add_object(self.arr_object)

class Object:
    def __init__(self, name, count):
        self.name = name
        self.count = count

if __name__ == "__main__":
    x1 = Object("Chest", 2)
    x2 = Object("EbakaBabaka", 10)
    array = [x1,x2]
    s = 5
    a = Map(s,array)
    a.add_obj()
    for i in range(s):
        print(a.map.maze[i])