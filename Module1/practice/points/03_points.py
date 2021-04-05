class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
points_0 = Point(0, 0)
# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
def distance(p1, p2):
    return (  ((p1.x - p2.x) ** 2) + (( p1.y-p2.y ) ** 2)  ) ** (1/2)

total_len = distance(points_0, points[0])
cur_point = points[0]
for next_point in points:
    new_len = distance(points_0, next_point)
    if new_len > total_len:
        total_len = distance (points_0, next_point)
        koordinate = f"({next_point.x}, {next_point.y})"
    cur_point = next_point
# TODO: your core here...

print("Координаты наиболее удаленной точки = ", koordinate)
