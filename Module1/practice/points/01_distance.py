class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return ((p2.x - p1.x)**2 + (p2.y - p2.y)**2 ) ** 0.5

# Даны две точки на координатной плоскости
point1 = Point(2,4)
point2 = Point(5,-2)

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
