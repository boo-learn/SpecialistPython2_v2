class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name # Название предмета
        self.weight = weight # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight  # максимальный суммарный вес предметов, которые можно положить в рюкзак

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.sum_weight() + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(item.name, 'не помещается в рюкзак')

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        total_weight = 0
        for item in self.items:
            total_weight += item.weight
        return total_weight


    def add_items(self, items: list[Item]):
        """
        :param items: Список вещей(объектов класса Item)
        """
        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.
        items.sort(key=lambda x: x.weight)
        for item in items:
            self.add_item(item)

    def max_weight_item(self):
        max_weight_item = self.items[0]
        for item in self.items:
            if item.weight > max_weight_item.weight:
                max_weight_item = item
        return max_weight_item

    def max_valuable_item(self):
        max_valuable_item = self.items[0]
        for item in self.items:
            if item.cost/item.weight > max_valuable_item.cost/max_valuable_item.weight:
                max_valuable_item = item
        return max_valuable_item


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=10)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

backpack.add_items(items)

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()
print('Самый тяжелый предмет в рюкзаке - это', backpack.max_weight_item().show())

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
print('Самый ценный предмет в рюкзаке - это', backpack.max_valuable_item().show())
