#Переработанный

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_point):
        ab = ((0 - other_point.x) ** 2 + (0 - other_point.y) ** 2) ** 0.5
        return ab


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]


# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты



def long(list_point):
    point_zero = Point(0, 0)
    long = 0
    for point in list_point:
        long2 = point_zero.distance(point)
        if long < long2:
            long = long2
            coordinate = [point.x, point.y]

    return (long, coordinate)





print("Координаты наиболее удаленной точки = ", long(points))
