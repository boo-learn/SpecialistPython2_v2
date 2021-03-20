class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self):
        return ((self.x + self.y) ** 2) ** 0.5


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


tmp1 = 0
tmp2 = 0

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
for i in range(len(points)):
    tmp1 = points[i].dist()
    if tmp1 > tmp2:
        tmp2 = tmp1
    else:
        continue

# TODO: your core here...

print("Координаты наиболее удаленной точки = ", tmp2)
