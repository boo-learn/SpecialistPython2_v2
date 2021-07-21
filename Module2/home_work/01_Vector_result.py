class Vector:
    def __init__(self, x, y):
        self.x = x  # Ось X
        self.y = y  # Ось Y
        
    def __str__(self):
        return f'vector ({self.x}, {self.y})'
    
    def __add__(self, v2):
        return f'vector ({self.x + v2.x}, {self.y + v2.y})'
    
    def __sub__(self, v2):
        return f'vector ({self.x - v2.x}, {self.y - v2.y})' 
    
    def __mul__(self, scalar):
        return f'vector ({self.x * scalar}, {self.y * scalar})'
