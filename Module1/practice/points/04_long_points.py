print("Task 4")
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point: Point) -> float:
        # TODO-0: скопируйте реализацию из предыдущей задачи
        return ((self.x - other_point.x)** 2 + (self.y - other_point.y)** 2)** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO-1: найдите точку наиболее удаленную от начала координат и выведите ее координаты
distance_from_zero = 0
for index, point in enumerate(points):
    if distance_from_zero < point.dist_to(Point(0,0)):
        distance_from_zero = point.dist_to(Point(0,0))
        i = index


print(f"Координаты наиболее удаленной точки = ({points[i].x}, {points[i].y})")
