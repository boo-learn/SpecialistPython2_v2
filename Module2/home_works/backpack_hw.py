class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_w: int):
        self.items = []
        self.max_w = max_w

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.sum_weight() + item.weight > self.max_w:
            print(f"Предмет {item.name} слишком тяжелый")
        else:
            self.items.append(item)

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, v in enumerate(self.items, 1):
            print(i, v.show())

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        weight = 0
        for i in self.items:
            weight += i.weight
        return weight

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        cost = 0
        for i in self.items:
            cost += i.cost
        return cost

    def add_items(self, items: list[Item]):
        """
        :param items: Список вещей(объектов класса Item)
        """
        items.sort(key=lambda x: x.weight)
        for i in items:
            self.add_item(i)

    def max_weight(self):
        if not self.items:
            print("Рюкзак пустой")
        else:
            self.items.sort(key=lambda x: x.weight)
            print(self.items[-1].show())

    def max_valuable(self):
        if not self.items:
            print("Рюкзак пустой")
        else:
            item = self.items[0]
            value = 0
            for i in self.items:
                new_value = i.cost / i.weight
                if new_value > value:
                    value = new_value
                    item = i
            print(item.show())


if __name__ == "__main__":
    # Создаем рюкзак, указываем максимальный вес
    backpack = BackPack(max_w=7)

    # TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
    items = [
        Item("Гиря", 25, 500),
        Item("Арбуз", 4, 300),
        Item("Ноутбук", 2.5, 22500),
        Item("Кот", 0.5, 250),
        Item("Трос", 3, 150),
        Item("Завтрак", 0.5, 450),
        Item("Аптечка", 3, 10000),
    ]

    # TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
    #  поиск предмета реализуйте в виде метода .max_weight()

    # TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
    #  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
    #  поиск предмета реализуйте в виде метода .max_valuable()

    backpack.max_weight()
    backpack.max_valuable()
    backpack.show_items()
    backpack.add_items(items)
    backpack.show_items()
    backpack.max_weight()
    backpack.max_valuable()
