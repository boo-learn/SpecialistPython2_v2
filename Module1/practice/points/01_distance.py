class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(point1, point2):
    return((point1.x - point2.y)**2+(point2.x - point2.y)**2)**0.5
    
point1 = Point(2, 4)
point2 = Point(5, -2)

distance(point1, point2)
