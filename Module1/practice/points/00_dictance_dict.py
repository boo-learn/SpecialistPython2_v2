def distance(p1: dict, p2: dict) -> float:
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    p1x = p1["x"]
    p1y = p1["y"]
    p2x = p2["x"]
    p2y = p2["y"]
    result = (((p1x - p2x)**2) + ((p1y - p2y)**2))**0.5
    return float(result)

# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
