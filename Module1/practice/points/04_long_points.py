class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        # TODO-1: реализуйте метод
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
point_zero = Point(0, 0)
point_target = None
max_dist = 0
for point in points:
    dist = point_zero.dist_to(point)
    if dist > max_dist:
        max_dist = dist
        point_target = point

print(f"Координаты наиболее удаленной точки = [{point_target.x},{point_target.y}]")
