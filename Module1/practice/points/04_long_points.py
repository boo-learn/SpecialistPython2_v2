class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist_to(self, other_point):
        # TODO-1: реализуйте метод
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        # Метод - функция внутри класса
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(100, -116), Point(-12, 0)]

maxi=0
for point in points:
    dist=point.dist_to(Point(0, 0))
    if dist>maxi:
        maxi=dist
        maxpoint=point

print("Координаты наиболее удаленной точки = x=", maxpoint.x, ", y=",maxpoint.y)
