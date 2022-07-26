class Item:
    def __init__(self, item_name, item_weight, item_cost):
        self.name = item_name  # Название предмета
        self.weight = item_weight  # Вес предмета, в килограммах
        self.cost = item_cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес: {self.weight} кг цена: {self.cost} руб"


class BackPack:  # рюкзак
    def __init__(self):
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def add_item(self, item: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        # TODO: реализуйте метод
        self.items.append(item)

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        # TODO: реализуйте метод
        count = 1
        for item in self.items:
            print(f'{count}. {item.show()}')
            count += 1


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)

# Создаем пустой рюкзак
backpack = BackPack()

# Добавляем пару предметов в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)

# Выводим все предметы в рюкзаке
backpack.show_items()
