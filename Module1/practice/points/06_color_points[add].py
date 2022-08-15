class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5
    
    def triangle_square(self, point2, point3):
        a = self.dist_to(point2)
        b = self.dist_to(point3)
        c = point2.dist_to(point3)
        perimeter = (a + b + c)/2
        square = (perimeter * (perimeter - a) * (perimeter - b) * (perimeter - c)) ** 0.5
        print(square)
        return square


points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]

points_red = [point for point in points if point.color == "red"]
points_green = [point for point in points if point.color == "green"]



print("Площадь красного треугольника = ", points_red[0].triangle_square(points_red[1], points_red[2]))
print("Площадь зеленого треугольника = ", points_green[0].triangle_square(points_green[1], points_green[2]))
