# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    def __add__(self,o):
        return Vector(self.x+o.x,self.y+o.y)
    def __sub__(self,o):
        return Vector(self.x-o.x,self.y-o.y)
    def __mul__(self,z):
        return Vector(z*self.x, z*self.y)
    def __rmul__(self,z):
        return Vector(z*self.x, z*self.y
