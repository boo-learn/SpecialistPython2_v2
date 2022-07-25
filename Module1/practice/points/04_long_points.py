class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        
def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
zero_point = Point(0,0)
distances = {point: distance(point, zero_point) for point in points}
farest_point = max(distances, key=distances.get)
print(f"Координаты наиболее удаленной точки = ({farest_point.x,farest_point.y})" )
