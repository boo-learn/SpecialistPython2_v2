class Item:
    def __init__(self, item_name, item_weight, item_cost):
        self.name = item_name  # Название предмета
        self.weight = item_weight  # Вес предмета, в килограммах
        self.cost = item_cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес: {self.weight} кг цена: {self.cost} руб"


class BackPack:  # рюкзак
    def __init__(self, max_weight=50):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight  # максимальный суммарный вес предметов, которые можно положить в рюкзак

    def add_item(self, item: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        max_weight = self.sum_weight()
        if max_weight + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(f'Предмет {item.name} слишком тяжелый')

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        count = 1
        for item in self.items:
            print(f'{count}. {item.show()}')
            count += 1

    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        weight_items = 0
        for item in self.items:
            weight_items += item.weight
        return weight_items

    def max_weight_item(self):
        max_item = self.items[0]
        for item in self.items:
            if max_item.weight < item.weight:
                max_item = item
        print(f'Самый тяжелый предмет: {max_item.name}')

    def max_valuable_item(self):
        max_item = self.items[0]
        sr_val = max_item.cost / max_item.weight
        for item in self.items:
            if sr_val < (item.cost / item.weight):
                max_item = item
                sr_val = item.cost / item.weight
        print(f'Самый ценный предмет: {max_item.name}')


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=27)

backpack.add_item(Item("Гиря", 25, 500))
backpack.add_item(Item("Арбуз", 4, 300))
backpack.add_item(Item("Ноутбук", 2.5, 22500))
backpack.add_item(Item("Кот", 0.5, 250))
backpack.add_item(Item("Трос", 3, 150))

backpack.show_items()

backpack.max_weight_item()
backpack.max_valuable_item()
