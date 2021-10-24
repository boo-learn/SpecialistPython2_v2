class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance():
    return (((points[0].x - points[1].x)**2+(points[0].y-points[1].y))*2)**0.5

points=[]
point1 = Point(2, 4)
points.append(point1)
point2 = Point(5, -2)
points.append(point2)



print("Расстояние между точками = ", distance())
