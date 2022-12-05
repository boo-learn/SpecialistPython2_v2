# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x={self.x}, y={self.y}'

    def __add__(self, other_line):        
        return Vector(self.x + other_line.x, self.y + other_line.y)

    def __sub__(self,other_line):
        results = {}
        results['x'] = self.x - other_line.x
        results['y'] = self.y - other_line.y
        return Vector(self.x - other_line.x, self.y - other_line.y)

    def __mul__(self,value):
        return Vector(self.x * value, self.y * value)


line1 = Vector(5,5)
line2 = Vector(10,3)
print(line1)
print(line2)
print(line1 + line2)
print(line1 - line2)
print(line1 * 4)
