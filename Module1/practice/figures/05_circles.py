import math
class Circle:
    def __init__(self, center_coords, radius):
        self.center_coords=center_coords
        self.radius=radius
    def dist_cen(self, other_circle):
        return math.sqrt((self.center_coords[0]-other_circle.center_coords[0])**2+(self.center_coords[1]-other_circle.center_coords[1])**2)

    def intersect(self, other_circle):
       if self.dist_cen(other_circle)<= self.radius+other_circle.radius:
           return True
       else:
           return False

# Окружности заданы координатами центров и радиусами
circle1 = Circle((6, -8), 5)
circle2 = Circle((2, 4), 4)
# Задание: проверьте пересекаются ли данные окружности

if circle1.intersect(circle2):
    print("Окружности пересекаются")
else:
    print("Окружности НЕ пересекаются")
