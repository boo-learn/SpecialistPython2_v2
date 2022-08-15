import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return math.sqrt(((self.x - other_point.x) ** 2) + ((self.y - other_point.y) ** 2))


def main():
    point1 = Point(2, 4)
    point2 = Point(5, -2)

    print(f"Расстояние между точками = {point1.dist_to(point2)}")


if __name__ == '__main__':
    main()
