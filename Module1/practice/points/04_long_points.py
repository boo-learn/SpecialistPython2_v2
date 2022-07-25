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

start_point = Point(0, 0)
max_dist = 0
goal_point = Point(0,0)
for point in points:
    dist = point.dist_to(start_point)
    if dist > max_dist:
        max_dist = dist
        goal_point = point

print("Координаты наиболее удаленной точки = ", 'x: ', goal_point.x, 'y: ', goal_point.y)
