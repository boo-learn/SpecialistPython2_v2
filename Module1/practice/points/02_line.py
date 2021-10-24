class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1, p2):
    dist = ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)**0.5
    return dist

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

dis_len=0
for i in range(len(points)):
    if (i+1)<len(points):
        dis_len+=distance(points[i],points[i+1])


print("Длина ломаной линии = ",dis_len )
