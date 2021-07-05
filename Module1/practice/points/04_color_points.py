class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ( (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2 ) ** 0.5


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно что точек каждого цвета ровно три, но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соеденены линиями и образуют треугольник

# Задание-1: доработайте конструкто class Point для хранения цвета точки
# Задание-2: реализуйте метод dist_to()
# Задание-3: вычислите площади треугольников образованных точками разных цветов


def triangle_area(p1, p2, p3):
    return abs(p1.x*p2.y + p2.x*p3.y + p3.x*p1.y - p2.x*p1.y - p3.x*p2.y - p1.x*p3.y) / 2


def count_colored_triangle_area(points, color):
    area = 0
    triangle = []
    for point in points:
        if point.color == color:
            triangle.append(point)
    num_points = len(triangle)
    if num_points != 3:
        print(f"Warning: invalid number of '{color}' points for a triangle: {num_points}")
    else:
        area = triangle_area(*triangle)
    return area


print("Площадь красного треугольника = ", count_colored_triangle_area(points, "red"))
print("Площадь зеленого треугольника = ", count_colored_triangle_area(points, "green"))

