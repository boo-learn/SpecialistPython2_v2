
def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    dist = ((p1["x"] - p2["x"]) ** 2 + (p1["y"] - p2["y"]) ** 2) ** .5
    return dist


# Даны две точки на координатной плоскости
point1 = {"x": -8, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
