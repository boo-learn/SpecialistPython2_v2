class Item:
    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    ...

    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        # TODO: реализуйте метод
        if self.sum_weight() + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(f'Предмет {item.name} слишком тяжелый')

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        # TODO: реализуйте метод
        for i, item in enumerate(self.items, start=1):
            print(i, item.show())

    # TODO: сюда копируем реализацию класса из предыдущего задания
    # TODO: добавьте новое свойство .max_weight - максимальный суммарный вес предметов, которые можно положить в рюкзак

    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        # TODO: реализуйте метод
        return sum(item.weight for item in self.items)

    def sum_cost(self):
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        # TODO: реализуйте метод
        return sum(item.cost for item in self.items)

    def add_items(self, items):
        """
        :param items: Список вещей(объектов класса Item)
        """
        for item in sorted(items, key=lambda item: item.weight):
            self.add_item(item)
        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.


# Создаем предметы
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=7)

# Пытаемся добавлять максимальное кол-во предметов в рюкзак
backpack.add_items(items)

# Выводим все предметы в рюкзаке
backpack.show_items()
