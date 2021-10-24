
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1,p2):
    a_b= ((p2.x-p1.x)**2+(p2.y-p1.y)**2)**0.5
    return a_b


point1 = Point(2, 4)
point2 = Point(2, -2)
lenght = distance(point1,point2)


print("Расстояние между точками = ", lenght)


