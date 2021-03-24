class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана последовательным списком точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод
    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Ломаная линия задана последовательным списком точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...
length = 0
for i in range(len(points)-1):
    length += points[i].dist(points[i + 1])

print("Длина ломаной линии = ", length)
