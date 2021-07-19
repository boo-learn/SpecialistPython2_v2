class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

def distance(points1,points2):
    return ((points1.x -points2.x)**2 + (points1.y-points2.y)**2)**(1/2)

# Задание: Найдите длину ломаной линии
n = 0
Line = 0
while n != len(points)-1:
    Line = Line + distance(points[n],points[n+1])
    n+=1
print("Длина ломаной линии = " , Line )
