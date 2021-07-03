def distance(p1, p2):
    dist = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2) ** 0.5
    return dist


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
start = Point(0, 0)
lenp = len(points)
a = 0
l = 0
while a < lenp:
    if distance(start, points[a]) > l:
        l = distance(start, points[a])
    a += 1
print(l)
x = 0
b = 0
while l != x:
    x = distance(start, points[b])
    point = points[b]
    b+=1
print (point.x, point.y)

