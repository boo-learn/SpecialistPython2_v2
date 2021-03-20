class Point:
    x = 7
    y = 4


# Создадим несколько объектов-точек
point1 = Point()
point2 = Point()

print(point1.x)  # 7
print(point2.x)  # 7

point1.x = 10
print(point1.x)  # 10
print(point2.x)  # 7

Point.x = -15
print(point1.x)  # 10
print(point2.x)  # -15

point1.y = -8