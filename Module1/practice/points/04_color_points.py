import math
class Point:
    def __init__(self, x, y, color = ""):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)


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
# Все точки одного цвета соеденены линиями и образуют треугольник

# Задание-1: доработайте конструкто class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов
class Triangle:
    a = 0
    b = 0
    c = 0
    def __init__(self, points):
        self.a = points[0].distance(rpoints[1])
        self.b = points[0].distance(rpoints[2])
        self.c = points[1].distance(rpoints[2])
    def area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

rpoints = []
gpoints = []
for point in points:
    if point.color == "red":
        rpoints.append(point)
    elif point.color == "green":
        gpoints.append(point)

print("Площадь зеленого треугольника = ", Triangle(rpoints).area())
print("Площадь красного треугольника = ", Triangle(gpoints).area())
