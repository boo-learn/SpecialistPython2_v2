class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Создаем список из объектов-точек
points = [Point(10, -8), Point(12, 5), Point(-3, 7)]

# Выведем координату x первой точки
print(points[0].x)

# Переберем все точки циклом и выведем их координаты в нужном нам формате(виде)
for point in points:
    print(f"(x:{point.x}, y:{point.y})")