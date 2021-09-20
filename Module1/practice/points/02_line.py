class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(p1,p2):
    # TODO: your code here
    # x1, y1, x2, y2 = int(),int(),int(),int()
    # p_1 = x1, y1
    # print(x1,y1)
    # p_2 = x2, y2
    # print(x2, y2)
    return  ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...

print("Длина ломаной линии = ", ...)

sum = float()
i = 0
end = len(points)
while i!= end-1:
    sum += distance(points[i],points[i+1])
    i += 1

print(sum)
