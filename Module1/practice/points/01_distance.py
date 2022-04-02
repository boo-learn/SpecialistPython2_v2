class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
   return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

dist = distance(point1, point2)  # Передаем объекты point1 и point2 в функцию

print("Расстояние между точками = ", dist)
