class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

def length(ps):
    length = 0
    i = 0
    while i < len(ps)-1:
        dist = ((ps[i].x - ps[i+1].x) ** 2 + (ps[i].y - ps[i+1].y) ** 2) ** 0.5
        length += dist
        i += 1
    return length
print("Длина ломаной линии = ", length(points))
