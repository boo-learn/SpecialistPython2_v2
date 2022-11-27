class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - 0) ** 2 + (self.y - 0) ** 2) ** 0.5

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# TODO-1: найдите точку наиболее удаленную от начала координат и выведите ее координаты
max = 0
cord_x = cord_y = 0
for point in points:
    dist = point.dist_to(point)
    print("Расстояние между точками = ", dist)
    
    if max < dist:
        max = dist
        cord_x = point.x
        cord_y = point.y
print(cord_x, cord_y)
    
    
