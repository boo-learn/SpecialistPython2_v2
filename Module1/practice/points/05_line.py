class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def dist_to(self, other_point):
        # TODO-1: реализуйте метод
        # Подсказка: смотри пример, Module1/examples/06_object_methods.py
        # Метод - функция внутри класса
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# TODO: Найдите длину ломаной линии
total=0
count=0
for point in points:
    if count==0:
        last=point
        count=count+1
        continue
    else:
        total=total+point.dist_to(last)
    
print("Длина ломаной линии = ", total)

