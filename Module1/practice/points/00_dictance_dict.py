def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    dist = ((p2["x"] - p1["x"]) ** 2 + (p2["y"] - p1["y"]) ** 2) ** 0.5

    return dist


# Даны две точки на координатной плоскости
point1 = {"x": 5, "y": 0}
point2 = {"x": 25, "y": 0}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
