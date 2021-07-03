class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


def area(triangle):
    a = triangle[0].dist_to(triangle[1])
    b = triangle[0].dist_to(triangle[2])
    c = triangle[1].dist_to(triangle[2])

    hp = (a + b + c) / 2

    return (hp * (hp - a) * (hp - b) * (hp - c)) ** 0.5


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

d = {}
for point in points:
    if point.color == "red":
        d.setdefault("red", []).append(point)
    else:
        d.setdefault("green", []).append(point)

h_p_r = area(d.get("red"))
h_p_g = area(d.get("green"))

print("Площадь красного треугольника = ", h_p_r)
print("Площадь зеленого треугольника = ", h_p_g)
