class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self) -> str:
        return f"{self.name}, {self.weight}, {self.cost}"


class BackPack:  # рюкзак
    def __init__(self):
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        # TODO: реализуйте метод
        self.items.append(item)

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        # TODO: реализуйте метод
        for one in self.items:
            print(self.items.index(one), one.show())


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)

# Создаем пустой рюкзак
backpack = BackPack()

# Добавляем пару предметов в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)

# Выводим все предметы в рюкзаке
backpack.show_items()
