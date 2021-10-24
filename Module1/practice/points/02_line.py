class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

def distance(a, b):
    ab = ((b.x - a.x)**2 + (b.y - a.y)**2)**0.5
    return ab

def long(list_point):
    long = 0
    for el in range(len(list_point)-1):
        long += distance(list_point[el], list_point[el+1])
    return long


print("Длина ломаной линии = ", long(points))
