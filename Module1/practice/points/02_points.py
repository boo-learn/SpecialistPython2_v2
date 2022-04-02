class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return ((p1.x - p2.x)**2 + (p1.y - p2.y) ** 2) ** 0.5

# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

for point in points:
    print(f"Расстояние до точки ({point.x}, {point.y}) =", distance(random_point, point))
