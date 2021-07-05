class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]
length = 0

x1 = points[0].x
y1 = points[0].y

for point in points:
    x2 = point.x
    y2 = point.y
    dist = distance(x1,y1,x2,y2)
    length += dist
    print(dist)
    x1 = x2
    y1 = y2
# TODO: your core here...

print("Длина ломаной линии = ", length)
