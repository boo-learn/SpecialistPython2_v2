class Item:
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self):
        return f" имя: {self.name:10} вес: {self.weight:5} цена: {self.cost:5}"


class BackPack:  # рюкзак
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, max_weight):
        self.items = []
        self.max_weight = max_weight

    def add_item(self, item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if (type(item) == Item):
            self.items.append(item)
        elif (type(item) == list):
            for itm_ in item:
                self.items.append(itm_)

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, itm_ in enumerate(self.items, 1):
            print(f"{i} - {itm_.show()}")

    def maximum_weight(self):
        itm_weight = self.items[0].weight
        itm_search = self.items[0]
        for itm_ in self.items:
            if itm_.weight > itm_weight:
                itm_weight = itm_.weight
                itm_search = itm_
        print(f"Самый тяжелый предмет в рюкзаке - {itm_search.show()} ")

    def max_valuable(self):
        valuable_cost = self.items[0].weight/self.items[0].cost
        valuable_item = self.items[0]
        for itm_ in self.items:
            if itm_.weight/itm_.cost>valuable_cost:
                valuable_cost=itm_.weight/itm_.cost
                valuable_item=itm_
        print(f"Самый ценный предмет в рюкзаке - {valuable_item.show()} ")


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=10)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
item_list = [
    Item("Ручка", 0.1, 100),
    Item("Мышка", 0.3, 900),
    Item("Тетрадка", 0.1, 200),
    Item("Книжка", 0.5, 1500),
    Item("Стол", 10, 10000),
    Item("Стул", 5, 7000),
    Item("Ноутбук", 2, 25000),
    Item("Смартфон", 1, 15000),
]

backpack.add_item(item_list)

backpack.show_items()

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()
backpack.maximum_weight()
# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
backpack.max_valuable()
