class Item:
    def __init__(self, name: str, weight: float | int, cost: int):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self):
        return f"{self.name}; вес:{self.weight}; цена:{self.cost}"


class BackPack:
    def __init__(self, max_weight=0):
        self.items = []
        self.max_weight = max_weight
        self.__total_weight = 0
        self.__total_cost = 0

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.__total_weight + item.weight <= self.max_weight:
            self.items.append(item)
            self.__total_weight += item.weight
            self.__total_cost += item.cost
        else:
            print(f"Предмет '{item.name}' слишком тяжелый!")

    def add_items(self, items_to_add: list[Item]):
        """
        :param items: Список вещей(объектов класса Item)
        """
        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.
        def get_item_weight(temp_item: Item):
            return temp_item.weight

        temp_items = items_to_add
        temp_items.sort(key=get_item_weight)

        for item in temp_items:
            self.add_item(item)

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for n, item in enumerate(self.items):
            print(f"{n + 1}. {item.show()}")

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        return self.__total_weight

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        return self.__total_cost



items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=3)
print(f"Создан рюкзак вместимостью {backpack.max_weight} кг")

# Пытаемся добавлять максимальное кол-во предметов в рюкзак
print()
print("Пытаемся добавлять максимальное кол-во предметов в рюкзак:")
backpack.add_items(items)

# Выводим все предметы в рюкзаке
print()
print("Выводим все предметы в рюкзаке:")
backpack.show_items()
