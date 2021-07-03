class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def leng(p1, p2):
        """
        Расстояние между двумя точками
        """
        #     x1-x2**2 + y1-y2**2
        return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5

class Triangle:
    def __init__(self, p1, p2, p3):
        self.point1 = p1
        self.point2 = p2
        self.point3 = p3

    def perim(self):
        a = self.point1.leng(self.point2)
        b = self.point1.leng(self.point3)
        c = self.point2.leng(self.point3)       
        return a + b + c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        a = self.point1.leng(self.point2)
        b = self.point1.leng(self.point3)
        c = self.point2.leng(self.point3)
        hp = (a + b + c)*0.5
        return (hp*(hp-a)*(hp-b)*(hp-c))**0.5
        
# Треугольник задан координатами трех точек
point1 = Point(2, 4)
point2 = Point(6, 8)
point3 = Point(-2, 0)

triangle1 = Triangle(point1, point2, point3)
# Задание: найдите площадь и периметр треугольника, реализовав методы
triangle1.perim()

print("Периметр треугольника = ", triangle1.perim())
print("Площадь треугольника = ", triangle1.area())

