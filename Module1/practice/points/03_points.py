  
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def distance(self, point2) -> object:
        """
        Расстояние между двумя точками
        """
        result = ((self.x - point2.x) ** 2 + (self.y - point2.y) ** 2) ** 0.5
        return result

points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

n = 0
furthest = 0

while n != len(points) - 1:
    if points[0].distance(points[n]):
        furtherst = points[0].distance(points[n])
    n += 1
        
# print(furtherst)

# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

# TODO: your core here...

print(f"Координаты наиболее удаленной точки = {furtherst:.2f}")
