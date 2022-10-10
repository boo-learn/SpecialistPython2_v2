from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = color

    def dist_to(self, other_point: Point) -> float:
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2)**0.5


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
# Все точки одного цвета соединены линиями и образуют треугольник

# TODO-1: доработайте конструктор class Point для хранения цвета точки
# TODO-2: реализуйте метод dist_to()
# TODO-3: вычислите площади треугольников образованных точками разных цветов

# your core here...
red = [point for point in points if point.color == "red"]
green = [point for point in points if point.color == "green"]

red_answer = ((red[1].x - red[0].x)*(red[2].y - red[0].y) - (red[2].x - red[0].x)*(red[1].y - red[0].y))/2
green_answer = ((green[1].x - green[0].x)*(green[2].y - green[0].y) - (green[2].x - green[0].x)*(green[1].y - green[0].y))/2

print("Площадь красного треугольника = ", abs(red_answer))
print("Площадь зеленого треугольника = ", abs(green_answer))
