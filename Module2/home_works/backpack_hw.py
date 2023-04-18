class BackPack:
    def __init__(self, max_weight: float):
        self.items = []
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        self.items.append(item)

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.show()}")

    def max_weight_1(self) -> Item:
        """
        Возвращает самый тяжелый предмет в рюкзаке
        """
        max_weight_item = None
        max_weight = -1
        for item in self.items:
            if item.weight > max_weight:
                max_weight = item.weight
                max_weight_item = item
        return max_weight_item

    def max_valuable_1(self) -> Item:
        """
        Возвращает самый ценный предмет в рюкзаке
        """
        max_valuable_item = None
        max_valuable = -1
        for item in self.items:
            item_valuable = item.cost / item.weight
            if item_valuable > max_valuable:
                max_valuable = item_valuable
                max_valuable_item = item
        return max_valuable_item


item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)
item5 = Item("Планшет", 1, 35500)

# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=30)

backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
backpack.add_item(item5)

#backpack.show_items()

max_weight_item = backpack.max_weight_1()
print(f"Самый тяжелый предмет в рюкзаке: {max_weight_item.show()}")

max_valuable_item = backpack.max_valuable_1()
print(f"Самый ценный предмет в рюкзаке: {max_valuable_item.show()}")

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
...

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
