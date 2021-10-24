class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

def distance():
    i = 0
    line = 0
    while i<len(points)-1:
        line+=(((points[i].x - points[i+1].x)**2+(points[i].y-points[i+1].y))**2)**0.5
        i+=1
    return print("Длина ломаной линии = ",line)

distance()
