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
    def __init__(self, max_weight: float):
        self.items = []
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак, если его вес не превышает максимальный вес рюкзака.
        """
        if self.sum_weight() + item.weight > self.max_weight:
            print(f"Предмет {item.name} слишком тяжелый")
        else:
            self.items.append(item)

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item.show()}")

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        return sum(item.weight for item in self.items)

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        return sum(item.cost for item in self.items)


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=30)

# Пытаемся добавлять предметы в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)

# Выводим все предметы в рюкзаке
backpack.show_items()
