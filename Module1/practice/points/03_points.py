class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

def r(p):
    return (p.x ** 2 + p.y ** 2) ** (1 / 2)

max_len = 0
maxp = Point(0, 0)
for a in points:
    cur = r(a)
    if r(a) > max_len:
        max_len = cur
        maxp = a

print(f"Координаты наиболее удаленной точки = ({maxp.x}, {maxp.y})")
