    ...
 class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:
    def __init__(self):
        self.items = []

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
