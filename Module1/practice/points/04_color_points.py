class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    # Расстояние между двумя точками
    def dist_to(self, other_point):
        return ((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2) ** 0.5

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        self.a = self.point1.dist_to(self.point2)
        self.b = self.point2.dist_to(self.point3)
        self.c = self.point3.dist_to(self.point1)

    # Площадь треугольника
    def area(self):
        return (self.perimeter() / 2 * (self.perimeter() / 2 - self.a) * \
                                       (self.perimeter() / 2 - self.b) * \
                                       (self.perimeter() / 2 - self.c)) ** 0.5

    # Периметр треугольника
    def perimeter(self):
        return self.a + self.b + self.c

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

greenPoints = [point for point in points if point.color == 'green']
redPoints = [point for point in points if point.color == 'red']
# for point in points:
#     if point.color == 'green':
#         greenPoints += [point]
#     elif point.color == 'red':
#         redPoints  += [point]

# Треугольники заданы координатами трех точек
greenTtriangle = Triangle(*greenPoints)
redTtriangle = Triangle(*redPoints)

# Задание-3: вычислите площади треугольников образованных точками разных цветов
print(f"Площадь красного треугольника = {redTtriangle.area()}")
print(f"Площадь зеленого треугольника = {greenTtriangle.area()}")
