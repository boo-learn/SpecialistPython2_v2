class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    res = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
    return res

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
point_0 = points[0]
del points[0]
# TODO: Найдите длину ломаной линии

lst_dist = []


for i in points:

    res = distance(i, point_0)

    lst_dist.append(res)

    point_0 = i
   
    print(res)

lst_dist.sort()
point_res = sum(lst_dist)

print("Длина ломаной линии = ", point_res)
