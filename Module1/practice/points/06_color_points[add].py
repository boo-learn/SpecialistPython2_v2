import math


class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        """
        Расстояние между двумя точками
        """
        return math.sqrt(
            math.pow((other_point.x - self.x), 2) +
            math.pow((other_point.y - self.y), 2)
        )


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        return abs((
                           (self.b.x - self.a.x) * (self.c.y - self.a.y) -
                           (self.c.x - self.a.x) * (self.b.y - self.a.y)
                   ) / 2
                   )


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно что точек каждого цвета ровно три, но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник
triFirst = []
triSecond = []

for pt in points:
    if pt.color == "red":
        triFirst.append(pt)
    elif pt.color == "green":
        triSecond.append(pt)

triRed = Triangle(triFirst[0], triFirst[1], triFirst[2])
triGreen = Triangle(triSecond[0], triSecond[1], triSecond[2])

print("Площадь красного треугольника =", triRed.get_area())
print("Площадь зеленого треугольника =", triGreen.get_area())
