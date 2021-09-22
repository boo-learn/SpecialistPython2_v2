# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum_vector(self,other_vector):
        return Vector(self.x + other_vector.x, self.y + other_vector.y)

    def sub_vector(self,other_vector):
        return Vector(self.x - other_vector.x, self.y - other_vector.y)

    def scalar_vector(self,mlt):
        return Vector(self.x * mlt, self.y * mlt)


vect1 = Vector(1, 2)
vect2 = Vector(3, 4)

vect3 = vect1.sum_vector(vect2)
print(vect3.__dict__)
vect3 = vect1.sub_vector(vect2)
print(vect3.__dict__)
vect3 = vect1.scalar_vector(3)
print(vect3.__dict__)
