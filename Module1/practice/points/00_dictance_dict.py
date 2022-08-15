from math import sqrt


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    
    dist_1 = sqrt((p2["x"] - p1["x"]) ** 2 + (p2["y"] - p1["y"]) ** 2)
    return dist_1

# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": 3, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
