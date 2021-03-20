class Point:
    def __init__(self, x, y): # magic
        self.x = x
        self.y = y
    # Метод
    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Ломаная линия задана последовательным списком точек
points = [Point(12, 4), Point(7, 4), Point(5, 4), Point(0, 4), Point(-12, 4)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...



# print("Длина ломаной линии = ", ...)

# p1 = Point(2, 6)
# p2 = Point(5, 8)
# print(dist(p1, p2))
length = 0
#
for i in range(len(points) - 1):
   length += points[i].dist(points[i + 1])
#
print("Длина ломаной линии = ", length)
#
# my_list1 = list((2, 5, 6, 7))
# my_list2 = list((-2, 5, 6, 7))
#
# my_list1.extend(my_list2)
#
# p1 = Point()
# p2 = Point()
#
# p1.dist(p2)

# class A:
#     def method1(self):
#         pass
#
#     def method2(self):
#         pass
#
# a1 = A()
# a2 = A()
#
# a1.method1()
# a2.method1()
