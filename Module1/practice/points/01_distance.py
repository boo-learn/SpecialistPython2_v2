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
    d = ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
    return d



# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...
dist = distance(point1, point2)
print("Расстояние между точками = ", dist)
print(type(dist))
