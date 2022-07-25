class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
      
    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Дан список из произвольного количества точек:
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
pointStart = Point(0, 0)
point_max = Point(0, 0)
dist = 0
# TODO: найдите точку наиболее удаленную от начала координат и выведите ее координаты
for point in points:
  if dist < pointStart.dist_to(point):
    dist = pointStart.dist_to(point)
    point_max = point
    
print("Координаты наиболее удаленной точки = ", "x: ", point_max.x , "y: ", point_max.y)
