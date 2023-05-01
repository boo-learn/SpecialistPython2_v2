from math import pi


class Sphere:
    def __init__(self, r: int = 1, x: int = 0, y: int = 0, z: int = 0):
        self.__r = r
        self.x = x
        self.y = y
        self.z = z

    @property
    def volume(self) -> float:
        # FIXME: категорически недопустимо округлять результат в методе.
        #  По факту, вы возвращаете неверный результат. Например, вместо 4.12345, возвращаете 4.124
        return round((4 / 3) * pi * (self.__r ** 3), 3)

    @property
    def square(self) -> float:
        return round(4 * pi * (self.__r ** 2), 3)

    def get_radius(self) -> int:
        return self.__r

    def get_center(self) -> tuple:
        return self.x, self.y, self.z
