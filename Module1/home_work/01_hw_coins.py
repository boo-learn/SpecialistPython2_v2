class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + \
                (self.y - other_point.y) ** 2) ** 0.5


def area(points: list) -> float:
    perimetr = 0
    area = 0
    lines = []
    cur_point = points[0]    
    for point in points[1:]:
        dist = cur_point.dist_to(point)
        perimetr += dist
        lines.append(dist)
        cur_point = point
    else:
        dist = cur_point.dist_to(points[0])
        perimetr += dist
        lines.append(dist)
    half_per = perimetr / 2
    area = (half_per * (half_per - lines[0]) * (half_per - lines[1]) * \
             (half_per - lines[2])) ** 0.5    
    return area


points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]

red_triangle = []
green_triangle = []
for point in points:
    if point.color == 'red':
        red_triangle.append(point)
    else:
        green_triangle.append(point)

area_red = area(red_triangle)
area_green = area(green_triangle)

print("Площадь красного треугольника = ", round(area_red, 2))
print("Площадь зеленого треугольника = ", round(area_green, 2))
