def distance(p1: dict, p2: dict) -> float:
    """
    Расстояние между двумя точками
    """

    return ((p1["x"] - p2["x"]) ** 2 - (p1["y"] - p2["y"]) ** 2) ** 0.5



# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
