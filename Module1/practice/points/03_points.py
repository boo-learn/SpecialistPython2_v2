class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
i = 0
maxi = 0
coord = {}
while i < len(points):
    point = points[i]
    ln = (point.x**2 + point.y**2)**0.5
    i += 1
    if ln > maxi:
        maxi = ln
        coord = point.x, point.y

print("Координаты наиболее удаленной точки = ", coord)
