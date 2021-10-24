class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

def distance(a):
    ab = ((0 - a.x)**2 + (0 - a.y)**2)**0.5
    return ab

def long(list_point):
    long = 0
    for el in range(len(list_point)):
        long2 = distance(list_point[el])
        if long < long2:
            long = long2
            coordinate = [list_point[el].x, list_point[el].y]

    return (long, coordinate)





print("Координаты наиболее удаленной точки = ", long(points))
