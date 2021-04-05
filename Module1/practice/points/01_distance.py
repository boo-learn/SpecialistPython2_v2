def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    import math
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)



# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)

# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()

# TODO: your core here...
rez = distance(point1, point2)
print("Расстояние между точками = ", round(rez, 2))
