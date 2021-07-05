class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def dist_to(self, other_point):
    #     return ()

class Triangle:
    # point1 = Point()
    # point2 = Point()
    # point3 = Point()
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perimeter(self):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3
        #length of point1 to point 2 + length point2 to point 3 + point 3 to point 1
        length_1 = ((self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2) ** 0.5
        length_2 = ((self.point2.x - self.point3.x) ** 2 + (self.point2.y - self.point3.y) ** 2) ** 0.5
        length_3 = ((self.point3.x - self.point1.x) ** 2 + (self.point3.y - self.point1.y) ** 2) ** 0.5



    #def area(self):
        # Для нахождения площади, используйте формулу Герона
       # ...


        # Треугольник задан координатами трех точек
        point1 = Point(2,4)
        point2 = Point(12, 8)
        point3 = Point(-2,6)
        triangle1 = Triangle(Point(2, 4), Point(12, 8), Point(-2, 0))
        # Задание: найдите площадь и пеиметр треугольника, реализовав методы

# TODO: your core here...
        perimeter_amount = length_3 + length_2 + length_1
        print( "Периметр треугольника = ", perimeter_amount)
print("Площадь треугольника = ", ...)
