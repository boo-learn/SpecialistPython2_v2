class Item:
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, name, weight, cost):
        ...

    def show(self):
        ...


class BackPack:  # рюкзак
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, max_weight: float):
        ...

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        ...

    def show_items(self) -> None:
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        ...


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=...)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
...

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()


class Item:

    def __init__(self, name: str, weight: float, cost: int):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:

    def __init__(self, max_weight: float):
        self.item = []
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:

        if self.sum_weight() + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")

    def show_item(self) -> None:
        for i, item in enumerate(self.item, 1):
            print(f'{i}. {item.show()}')

    def sum_weight(self) -> float:
        current_weight = 0
        for item in self.items:
            current_weight += item.weight
        return current_weight

    def sum_cost(self) -> int:
        current_cost = 0
        for item in self.items:
            current_cost += item.cost
        return current_cost

backpack = BackPack(max_weight=25)
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Кирпич", 10, 100),
]


print(f"самый тяжелый предмет: {backpack.max_weight}")
