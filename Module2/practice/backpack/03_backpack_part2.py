class Item:
    def __init__(self, name, weight, cost ):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях
    def show(self):
        return f"{self.name}  вес: {self.weight}, цена: {self.cost}"
    
class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def show_items(self):
        for n, item in enumerate(self.items, 1):
            print(n, item.show())

    def sum_weight(self):
        # summar = 0
        # for item in self.items:
        #     summar += item.weight
        # return summar
        return sum([item.weight for item in self.items])

    def add_item(self, item: Item):
        if self.sum_weight() + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжёлый")
        
    def sum_cost(self):
        return sum([item.cost for item in self.items])


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=30)

# Пытаемся добавлять предметы в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
# TODO: Если предмет не помещается в рюкзак по весу - вывести сообщение "Предмет {name} слишком тяжелый",
#  и сам предмет не должен быть добавлен в рюкзак.
#  Если предмет помещает, то добавляем его в рюкзак.

# Выводим все предметы в рюкзаке
backpack.show_items()
