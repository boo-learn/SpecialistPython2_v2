class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...

print("Длина ломаной линии = ", ...)


def leng(p1, p2):
    """
    Расстояние между двумя точками
    """
    #     x1-x2**2 + y1-y2**2
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
    

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()
length = 0
for i in range(len(points)-1):
    length = leng(points[i], points[i+1]) + length 



print("Расстояние между точками = ", length)
#© 2021 GitHub, Inc.

