# Сюда отправляем решение задачи "Вектор"
# Само задание в файле 01_Vector_task.md

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x 
        self.y = y
        
    def __str__(self):
        return (self.x,self.y)
        
    def __add__(self,other_vector):
        x1 = self.x + other_vector.x
        y1 = self.y + other_vector.y
        
        return (x1,y1)
    
    def __mul__(self , number):
        x1 = self.x * number
        y1 = self.y * number
        
        return (x1,y1)

    def __sub__(self,other_vector):
        x1 = self.x - other_vector.x
        y1 = self.y - other_vector.y
        
        return (x1,y1)
    

vect1 = Vector(5,7)

vect2 = Vector(-4,4)

#print(vect2 *-5)

