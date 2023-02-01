from operator import itemgetter, attrgetter
class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self) -> str:
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight: float):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.weight = 0
        self.cost = ...
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        if (self.weight + item.weight) <= self.max_weight:
            self.items.append(item)
            self.weight += item.weight
        else:
            print('Предмет ' + item.name + ' не помещается в рюкзак.')

    def show_items(self) -> None:
        for item in self.items:
            print(item.show())

    def max_weight_meth(self):
        items_sorted = sorted(self.items, key=attrgetter('weight'))
        print(f"Самый тяжелый предметр в рюкзаке: {items_sorted[len(items_sorted)-1].name}")

    def max_valuable(self):
        real_cost = 0
        max_cost = 0
        item_max_cost = None
        for item in self.items:
            real_cost = item.cost/item.weight
            if real_cost > max_cost:
                max_cost = real_cost
                item_max_cost = item.name
        print(f"Самый дорогой предметр в рюкзаке: {item_max_cost}")


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=400)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак

item2 = Item("Арбуз", 4, 300)
item1 = Item("Гиря", 25, 500)
item3 = Item("Ноутбук", 0.5, 22500)
item4 = Item("Кот", 2, 250)
item5 = Item("Пиво", 3, 333)

# Пытаемся добавлять предметы в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
backpack.add_item(item5)

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
backpack.max_weight_meth()

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
backpack.max_valuable()
