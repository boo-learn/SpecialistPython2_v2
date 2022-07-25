class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

     
def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# TODO: Найдите длину ломаной линии
line_length = 0
for i in range(len(points)-1):  
    line_length += distance(points[i], points[i+1])
    

print("Длина ломаной линии = ", line_length)
