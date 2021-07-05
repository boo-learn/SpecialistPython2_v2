class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
def distance(point1: Point, point2: Point):
    '''
    Расстояние между двумя точками
    :param point1: объект типа Point
    :param point2: объект типа Point
    :return: возвращает скалярное расстояние между двумя точками
    '''
    return ((point1.x - point2.x)**2 + (point1.y - point2.y)**2)**0.5

p0 = Point(0, 0)
d = 0

for pnt in points:
    if d < distance(p0, pnt):
        d = distance(p0, pnt)
        p_max = pnt

print(f"Координаты наиболее удаленной точки = ({p_max.x}, {p_max.y})")
