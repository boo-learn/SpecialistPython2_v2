def distance(p1, p2):
    n = (((point2["x"] - point1["x"])) ** 2 + ((point2["y"] - point1["y"])) ** 2) ** 0.5
    return n


# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
