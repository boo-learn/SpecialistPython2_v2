class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance(fv_p1, fv_p2):
    return ((fv_p1.x-fv_p2.x)**2+(fv_p1.y-fv_p2.y)**2)**0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
i = 0
lenght = 0

while i < len(points) and i < 4:
    lenght = distance(points[i], points[i+1])+ lenght
    i += 1

print("Длина ломаной линии = ", round(lenght))
