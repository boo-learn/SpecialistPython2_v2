class Item:
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []
        self.max_weight = max_weight

    def add_item(self, item: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        free_weight = self.max_weight - self.sum_weight()
        if item.weight <= free_weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")

    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        total_sum = 0
        for item in self.items:
            total_sum += item.weight
        return total_sum

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        i = 1
        for item in self.items:
            print(f'{i}: {item.show()}')
            i += 1

    def get_max_weight(self):
        max_weight = 0
        item_name = None
        for item in self.items:
            if item.weight > max_weight:
                max_weight = item.weight
                item_name = item.name
        print(f'Самый тяжелый предмет- {item_name} с весом {max_weight} кг')

    def get_max_valuable(self):
        max_value = 0
        item_name = None
        for item in self.items:
            cost_per_weight = int(item.cost / item.weight)
            if cost_per_weight > max_value:
                max_value = cost_per_weight
                item_name = item.name
        print(f'Самый ценный предмет- {item_name} с ценой {max_value}')


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=35)

item1 = Item("Пачка бумаги", 1, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)
item5 = Item("Дыня", 3, 350)

backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
backpack.add_item(item5)

backpack.show_items()
backpack.get_max_weight()
backpack.get_max_valuable()
