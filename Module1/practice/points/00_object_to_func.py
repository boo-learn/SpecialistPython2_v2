class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def demo_func(p):  # функция получает объект point в переменную p
    print(f"Координата x: {p.x}")
    print(f"Координата y: {p.y}")


# Создаем объект Точка, с координатами x:2, y:4
point = Point(2, 4)

# Передаем точку в функцию
demo_func(point)
