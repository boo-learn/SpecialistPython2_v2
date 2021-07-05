class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
l=0
i = 0
# TODO: your core here...
while i<len(points)-1:
    point1=points[i]
    point2=points[i+1]
    l +=distance(point1,point2)
    i+=1
print("Длина ломаной линии = ", l)
