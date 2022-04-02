class Circle:
    def __init__(self, center_coords, radius):
        self.center__coords = center_coords
        self.radius = radius

    def length(self):

        return 2 * 3,141 * self.radius
    
        # TODO-1: реализуйте метод


    def area(self):

        return 3,141 * (self.radius)**2
        
        # TODO-2: реализуйте метод



# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)

print(f"Длина окружности радиусом {circle1.radius} = {circle1.length}")
print(f"Длина окружности радиусом {circle2.radius} = {circle2.length}")

print(f"Площадь окружности радиусом {circle1.radius} = {circle1.area}")
print(f"Площадь окружности радиусом {circle2.radius} = {circle2.area}")
