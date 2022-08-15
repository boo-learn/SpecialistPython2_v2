def distance(p1, p2):
    
    # TODO: напишите тело функции
    d = (((p2['x']) - p1['x'])**2 + (p2['y'] - p1['y'])**2)**.5
    return d


# Даны две точки на координатной плоскости
point1 = {"x": 5, "y": 5}
point2 = {"x": -10, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
