class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

def distance(point1: Point, point2: Point):
    '''
    Расстояние между двумя точками
    :param point1: объект типа Point
    :param point2: объект типа Point
    :return: возвращает скалярное расстояние между двумя точками
    '''
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

# Задание: Найдите длину ломаной линии

i = 0
d = 0

while i < len(points):
    if i > 0:
        d += distance(points[i-1], points[i])
    i += 1


print("Длина ломаной линии = ", d)
