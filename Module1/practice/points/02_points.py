class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
   i = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
   return i

# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

dist0 = distance(points[0], random_point)  # Передаем объекты point1 и point2 в функцию
dist1 = distance(points[1], random_point)  # Передаем объекты point1 и point2 в функцию
dist2 = distance(points[2], random_point)  # Передаем объекты point1 и point2 в функцию
dist3 = distance(points[3], random_point)  # Передаем объекты point1 и point2 в функцию
dist4 = distance(points[4], random_point)  # Передаем объекты point1 и point2 в функцию

print("Расстояние между точками = ", dist0)
print("Расстояние между точками = ", dist1)
print("Расстояние между точками = ", dist2)
print("Расстояние между точками = ", dist3)
print("Расстояние между точками = ", dist4)
