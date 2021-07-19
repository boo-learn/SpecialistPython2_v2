class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2)**(1/2)
    """
    Расстояние между двумя точками
    """


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

i = 0
linia = 0

while i != len(points) - 2:
    linia = linia + distance(points[i], points[i+1])
    i += 1


print("Длина ломаной линии = ", linia)
