class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(x1, x2, y1, y2):
    dist = ((x2 - x1)**2 + (y2-y1)**2)**0.5
    return dist

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
# for i in range(len(points)):

d = []
for i in range(len(points)-1):
    
    xi = points[i].x
    xj = points[i+1].x
    yi = points[i].y
    yj = points[i+1].y
    d.append(distance(xi, xj, yi, yj))


# TODO: your core here...
print("Длина ломаной линии = ", sum(d))
