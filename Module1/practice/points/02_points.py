class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    return ((p2.x - p1.x)**2 +  (p2.y - p1.y)**2)**0.5

# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

list_ = []
for point in points:
    list_.append(distance(random_point, point))
print (list_)
