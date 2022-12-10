# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x1, y1, x2, y2, name: str = 'a'):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.name = name

    def __str__(self):
        vector_img = '\u20D7'
        return f"{self.name}{vector_img} ({self.x1},{self.y1}; {self.x2},{self.y2}) "

    def __add__(self, vector_term):
        new_x1 = self.x1
        new_y1 = self.y1
        new_x2 = vector_term.x2
        new_y2 = vector_term.y2
        new_name = f"{'{0}⃗'.format(self.name)} + {vector_term.name}"
        return Vector(new_x1, new_y1, new_x2, new_y2, new_name)

    def __sub__(self, vector_subtrahend):
        new_x1 = vector_subtrahend.x2
        new_y1 = vector_subtrahend.y2
        new_x2 = self.x2
        new_y2 = self.y2
        new_name = f"{'{0}⃗'.format(self.name)} - {vector_subtrahend.name}"
        return Vector(new_x1, new_y1, new_x2, new_y2, new_name)

    def __mul__(self, scalar: int):
        new_x1 = self.x1
        new_y1 = self.y1
        new_x2 = self.x2 * scalar
        new_y2 = self.y2 * scalar
        new_name = f"{scalar}{self.name}"
        return Vector(new_x1, new_y1, new_x2, new_y2, new_name)


# v1 = Vector(1, 2, 5, 7)
# v2 = Vector(4, 3, 6, 9, "b")
