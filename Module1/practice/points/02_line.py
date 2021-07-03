class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
i=0
lenght=0

while i<=len(points):
    lenght=distance(points[i], points[i+1])+lenght
    i+=1

print("Длина ломаной линии = ", lenght)



"C:\Program Files\Python39\python.exe" C:/Users/lamin_gfslnr1/OneDrive/Документы/pythonProject2/module1/t2.py
Traceback (most recent call last):
  File "C:\Users\lamin_gfslnr1\OneDrive\Документы\pythonProject2\module1\t2.py", line 19, in <module>
    lenght=distance(points[i], points[i+1])+lenght
IndexError: list index out of range
