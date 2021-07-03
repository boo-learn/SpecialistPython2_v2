class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
point0 = Point(0, 0)

def leng(p1, p2):
    """
    Расстояние между двумя точками
    """
    #     x1-x2**2 + y1-y2**2
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5
    

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

length_max = 0
length = 0
max_point = 0

for point in points:
    length = leng(point0, point)
    print("Расстояние между точками = ", length)
    if length_max < length:
        length_max = length
        max_point = point
    
print(length_max)
