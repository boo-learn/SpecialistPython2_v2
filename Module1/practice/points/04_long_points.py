class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist_to(self):
        # TODO-1: реализуйте метод
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        return ((self.x) ** 2 + (self.y) ** 2) ** 0.5
# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
max_dist=0
for point in points:
    if point.dist_to()>max_dist:
        max_dist=point.dist_to()
        max_point=point


# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты

print("Координаты наиболее удаленной точки = ", max_point.x, max_point.y)
