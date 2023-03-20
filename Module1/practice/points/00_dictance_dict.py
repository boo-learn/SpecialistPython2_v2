def distance(p1: dict, p2: dict) -> float:
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции

# A(xa, ya) и B(xb, yb) на плоскости: AB = √((xb - xa)2 + (yb - ya)2)
def distance(p1: dict, p2: dict) -> float:
    dist = ((p2["x"] - p1["x"]) ** 2 + (p2["y"] - p1["y"])**2) ** 0.5
    return dist

# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
