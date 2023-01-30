print("Task 2")


# Дан список из произвольного количества точек:
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
# И произвольная точка на плоскости:
random_point = Point(-12, 10)

for point in points:
    print(f"Расстояние от рандом поинт до {distance(random_point, point)}")
