class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# TODO: your core here...




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Метод
    def dist(self):
        return ((self.x + self.y) ** 2) ** 0.5

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# TODO: your core here...
length = 0
max_dist = 0
coords = ()
for i in range(len(points)-1):
    if points[i].dist() > max_dist:
        max_dist = length
        coords = (points[i].x, points[i].y)

print("Координаты наиболее удаленной точки = ", coords)
