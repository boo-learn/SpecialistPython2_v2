# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point x:{self.x}, y:{self.y}"


class NamedPoint(Point):
    def __init__(self, name, x, y):
        Point.__init__(self, x, y)
        self.name = name

    def __str__(self):
        return f"Point {self.name} ({self.x}:{self.y})"


class Vector:
    def __init__(self, name, x, y):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return f'Vector {self.name} ({self.x}:{self.y})'

    def __add__(self, other_v):
        x = self.x + other_v.x
        y = self.y + other_v.y
        name = self.name + '+' + other_v.name
        return Vector(name, x, y)

    def __sub__(self, other_v):
        x = self.x - other_v.x
        y = self.y - other_v.y
        name = self.name + '-' + other_v.name
        return Vector(name, x, y)

    def __mul__(self, num):
        new_x = self.x * num
        new_y = self.y * num
        new_name = self.name + '*' + str(num)
        return Vector(new_name, new_x, new_y)


# Создание точек
point1 = NamedPoint('A', 2, 3)
point2 = NamedPoint('B', 11, 9)
point3 = NamedPoint('C', 2, 1)
point4 = NamedPoint('D', 10, 8)
print(point1)
print(point2)
print(point3)
print(point4)

# Создание векторов
vector_ab = Vector(point1.name + point2.name, point2.x - point1.x, point2.y - point1.y)
vector_cd = Vector(point3.name + point4.name, point4.x - point3.x, point4.y - point3.y)
print(vector_ab)
print(vector_cd)

# Сложение векторов
sum_v = vector_ab + vector_cd
print(f'{vector_ab} + {vector_cd} = {sum_v}')

# Вычитание векторов
sub_v = vector_ab - vector_cd
print(f'{vector_ab} - {vector_cd} = {sub_v}')

# Умножение вектора на число
mult_v = vector_ab * 2
print(f'{vector_ab} * 2 = {mult_v}')
