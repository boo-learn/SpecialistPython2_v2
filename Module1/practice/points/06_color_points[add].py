class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = "color"

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** .5


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

# TODO-1: доработайте конструктор class Point для хранения цвета точки
# TODO-2: реализуйте метод dist_to()
# TODO-3: вычислите площади треугольников образованных точками разных цветов

# your core here...
r = abs(0.5 * ((points[2].x - points[0].x) * (points[5].y - points[0].y) - (points[5].x - points[0].x) * (points[2].y - points[0].y)))
g = abs(0.5 * ((points[3].x - points[1].x) * (points[4].y - points[1].y) - (points[4].x - points[1].x) * (points[3].y - points[1].y)))
print("Площадь красного треугольника = ", r)

print("Площадь зеленого треугольника = ", g)
