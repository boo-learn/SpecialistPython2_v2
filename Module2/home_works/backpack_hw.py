class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight
        self.sum_w = 0
        self.cost_s = 0

    def add_item(self, item: Item) -> None:
        if self.sum_w + item.weight <= self.max_weight:
            self.items.append(item)
            self.sum_w += item.weight
        else:
            print("overweight!")

        # TODO: реализуйте метод

    def show_items(self) -> None:
        for n, item in enumerate(self.items, 1):
            print(f"Num: {n}, {item.show()}")

    def sum_weight(self) -> float:
        return self.sum_w

    def sum_cost(self) -> int:
        return self.cost_s

    def max_weight_method(self):
        return sorted(self.items, key = lambda i: i.weight, reverse=True)[0]

    def max_valuable(self):
        return sorted(self.items, key = lambda i: i.cost, reverse=True)[0]

# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight = 10)

# Создаем предметы
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

backpack.add_item(items[1])
backpack.add_item(items[2])
backpack.add_item(items[3])
backpack.add_item(items[4])


print(f"самый тяжелый предмет : {backpack.max_weight_method().name}, {backpack.max_weight_method().weight}")
print(f"самый ценный предмет : {backpack.max_valuable().name}, {backpack.max_valuable().cost}")

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
