"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана последовательным списком точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...
# my code

print("Длина ломаной линии = ", ...)
"""

# Решение

import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Ломаная линия задана последовательным списком точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

# TODO: your core here...
# my code
p0  = points[0]
result = 0.0
for i in range(1,len(points)-1):
    p = points[i]
    otr = math.sqrt((p0.x-p.x)**2 + (p0.y-p.y)**2)
    p0=p
    result =result + otr
    
    

print(f"Длина ломаной линии = {result}")


# Не судите строго, за неуспиваемость в классе! 
# Просто сложно акцентрировать внимание на решении задач, 
# без знания синтаксиса языка.
# В любом случае, я пришёл получать знания в программировании,
# Для воплощения задуманных мной интернет проектов! 

# Благодарю за понимание...
