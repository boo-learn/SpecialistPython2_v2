class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.sum_weight() + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, item in enumerate(self.items, 1):
            print(f'{i}. {item.show()}')

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        current_weight = 0
        for item in self.items:
            current_weight += item.weight
        return current_weight

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        current_cost = 0
        for item in self.items:
            current_cost += item.cost
        return current_cost

    def add_items(self, items: list[Item]):
        """
        :param items: Список вещей(объектов класса Item)
        """
        items.sort(key=lambda item: item.weight)
        for item in items:
            self.add_item(item)

    def heavest(self):  # max_weight уже занято атрибутом
        return max(self.items, key=lambda item: item.weight)

    def most_valuable(self): # для единообразия с heavest()
        return max(self.items, key=lambda item: item.cost / item.weight)


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=20)

# Создаем 5-8 предметов и добавляем их в рюкзак
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
    Item("Кольцо", 0.02, 10000)
]
for item in items:
    backpack.add_item(item)

# В рюкзаке найдите самый тяжелый предмет и выведите его на экран
print(f"Самый тяжелый предмет: {backpack.heavest().show()}")

# В рюкзаке найдите самый ценный предмет и выведите его на экран
# ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
print(f"Самый ценный предмет: {backpack.most_valuable().show()}")
