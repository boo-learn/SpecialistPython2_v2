class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"

    def __lt__(self, other):
        return self.weight < other.weight



class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.sum_weight() + item.weight < self.max_weight:
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
        items.sort()
        for item in items:
            self.add_item(item)


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
