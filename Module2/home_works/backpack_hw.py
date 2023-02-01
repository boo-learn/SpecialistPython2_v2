class Item:
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):

        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, max_weight: float):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        summa = 0
        for item in self.items:
            summa += item.weight
        return summa

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        free_weight = self.max_weight - self.sum_weight()

        if free_weight >= item.weight:
            self.items.append(item)

        else:
            print(f'Предмет {item.name} слишком тяжелый')

    def show_items(self) -> None:
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, item in enumerate(self.items):
            print(f'{i + 1}) {item.show()}')

    def max_weight_items(self):

        heaviest_item = max(self.items, key=lambda item: item.weight)

        print(heaviest_item.name)

    def max_valuable(self):

        expensive_item = max(self.items, key=lambda item: item.cost/item.weight)

        print(expensive_item.name)

# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=20)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак

item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)
item5 = Item("Инструменты", 2, 800)
item6 = Item("Кроссовки", 0.2, 600)

backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
backpack.add_item(item5)
backpack.add_item(item6)

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()

backpack.max_weight_items()

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()

backpack.max_valuable()
