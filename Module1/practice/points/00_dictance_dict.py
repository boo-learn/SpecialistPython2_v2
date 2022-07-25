import math


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции

    # AB = √(xb - xa)2 + (yb - ya)2

    return math.sqrt((p2["x"] - p1["x"]) * (p2["x"] - p1["x"]) + (p2["y"] - p1["y"]) * (p2["y"] - p1["y"]))

# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
