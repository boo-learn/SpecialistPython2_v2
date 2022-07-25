# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def distance(p1, p2):
    """
    Расстояние между двумя точками
    """
    # TODO: напишите тело функции


# Даны две точки на координатной плоскости
point1 = {"x": 2, "y": 5}
point2 = {"x": -2, "y": 4}

dist = (pow(point1["x"]-point2["x"], 2) + pow(point1["y"]-point2["y"], 2)) ** (0.5)

print("Расстояние между точками = ", dist)
