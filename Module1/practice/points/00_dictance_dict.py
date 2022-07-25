import math


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    return math.sqrt(
        math.pow((p2.get("x") - p1.get("x")), 2) +
        math.pow((p2.get("y") - p1.get("y")), 2)
    )


# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
