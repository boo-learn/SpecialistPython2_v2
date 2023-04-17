def distance(p1: dict, p2: dict) -> float:
    """
    Расстояние между двумя точками
    """
    try:
        side_x = p1.get('x') - p2.get('x')
        side_y = p1.get('y') - p2.get('y')
        return (side_x**2 + side_y**2)**0.5
    except Exception as err:
        print(f'Error: {err}')


# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = distance(point1, point2)

print("Расстояние между точками = ", dist)
