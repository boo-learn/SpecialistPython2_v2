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

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
point_0 = Point(0, 0)

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты

lst_dist = []
dict_dist = {}

for i in points:
    res = distance(i, point_0)
    lst_dist.append(res)
    dict_dist[res]=i
    print(res)

lst_dist.sort()

point_res = dict_dist[lst_dist[-1]]
print("Координаты наиболее удаленной точки = ", point_res.x, ',', point_res.y)
