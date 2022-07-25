
def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    AC = point2[1]["x"] - point1[1]["x"]
    BC = point2[1]["y"] - point1[1]["y"]
    AB = (AC * AC + BC * BC) ** 0.5
    return AB
# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)





