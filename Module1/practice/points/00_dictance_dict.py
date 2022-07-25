def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции
    x1 = point1['x']
    x2 = point2['x']
    y1 = point1['y']
    y2 = point2['y']
    return ((x1-x2)**2+(y1-y2)**2)**0.5

# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
