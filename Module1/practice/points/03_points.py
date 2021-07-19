import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return math.sqrt((p2.y - p1.y) ** 2 + (p2.x - p1.x) ** 2)

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

max_point = max([(distance(i, Point(0,0)), i) for i in points])
print(f"Координаты наиболее удаленной точки = {max_point[1].x, max_point[1].y}")
