class Item:
    def __init__(self, name, weight, cost ):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях
    def show(self):
        return f"{self.name}  вес: {self.weight}, цена: {self.cost}"


class BackPack:  # рюкзак
    def __init__(self):
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for n, item in enumerate(self.items, 1):
            print(n, item.name)


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
