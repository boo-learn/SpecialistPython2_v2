class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, op):
        return ((self.x - op.x) ** 2 + (self.y - op.y) ** 2) ** 0.5


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

r = [[], []]
g = [[], []]
pr = 0
pg = 0
for a in points:
    if a.color == "green":
        g[0].append(a)
    else:
        r[0].append(a)
for i in range(3):
    r[1].append(r[0][i - 1].dist_to(r[0][i]))
    g[1].append(g[0][i - 1].dist_to(g[0][i]))
pr = sum(r[1]) / 2
pg = sum(g[1]) / 2
sr = pr
sg = pg
for i in range(3):
    sr *= pr - r[1][i]
    sg *= pg - g[1][i]
sr **= 0.5
sg **= 0.5
print("Площадь красного треугольника = ", sr)
print("Площадь зеленого треугольника = ", sg)
