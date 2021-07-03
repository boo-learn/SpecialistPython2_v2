class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

def most_distant (ps):
    max_dist = 0
    x = 0
    y = 0
    for point in ps:
        dist = ((point.x - 0) ** 2 + (point.y - 0) ** 2) ** 0.5
        if dist > max_dist:
            max_dist = dist
            x = point.x
            y = point.y
    return x,y
print("Координаты наиболее удаленной точки = ", most_distant (points))
