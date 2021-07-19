class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(points1,points2):
    return ((points1.x -points2.x)**2 + (points1.y-points2.y)**2)**(1/2)



# Дано две точки на координатной плоскости
points1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()


print("Расстояние между точками = ", distance(points1,point2))
