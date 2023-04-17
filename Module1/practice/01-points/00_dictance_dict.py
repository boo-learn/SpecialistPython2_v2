def distance(p1: dict, p2: dict) -> float:
    """
    Расстояние между двумя точками
    """
    x1, y1 = p1["x"], p1["y"]
    x2, y2 = p2["x"], p2["y"]
    return ((x2 - x1) ** 2 + (y2 - y1)**2) ** 0.5


point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
