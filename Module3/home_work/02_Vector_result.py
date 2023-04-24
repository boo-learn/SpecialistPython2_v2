
class Vector:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"{self.x}, {self.y}"

    def __add__(self, vector2):
        __x = self.x + vector2.x
        __y = self.y + vector2.y
        return Vector(__x, __y)

    def __sub__(self, vector2):
        __x = self.x - vector2.x
        __y = self.y - vector2.y
        return Vector(__x, __y)

    def __mul__(self, n):
        __x = self.x * n
        __y = self.y * n
        return Vector(__x, __y)
