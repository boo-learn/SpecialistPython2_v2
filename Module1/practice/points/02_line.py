class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...
def dist(plist):
    sum_dist = 0
    for i in range(1,len(plist)-1):
        temp_dist = ((plist[i].x - plist[i+1].x) ** 2 + (plist[i].y - plist[i+1].y) ** 2) ** .5
        sum_dist += temp_dist
    return sum_dist


res_dist = dist(points)

print("Длина ломаной линии = ", res_dist)
