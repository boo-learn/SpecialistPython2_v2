class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        self.x += other.x
        self.y += other.y

    def subtract(self, other):
        self.x -= other.x
        self.y -= other.y

    def multiply(self, value):
        self.x *= value
        self.y *= value
