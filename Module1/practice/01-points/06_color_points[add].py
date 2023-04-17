from __future__ import annotations


class Point:
    def __init__(self, x: int, y: int, color: str):
        self.x = x
        self.y = y
        self.color = ...

    def dist_to(self, other_point: Point) -> float:
        ...


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три, но порядок точек в списке и значение координат произвольные
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
# TODO-2: реализуйте метод dist_to(), для расчета расстояния между точками
# TODO-3: вычислите площади треугольников образованных точками разных цветов

# your core here...

print("Площадь красного треугольника = ", ...)
print("Площадь зеленого треугольника = ", ...)
