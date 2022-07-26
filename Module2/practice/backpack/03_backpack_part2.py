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
        # TODO: Если предмет не помещается в рюкзак по весу - вывести сообщение "Предмет {name} слишком тяжелый",
        #  и сам предмет не должен быть добавлен в рюкзак.
        #  Если предмет помещает, то добавляем его в рюкзак.
        max_weight = self.sum_weight()
        if max_weight + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(f'Предмет {item.name} слишком тяжелый')

    def show_items(self):
        count = 1
        for item in self.items:
            print(f'{count}. {item.show()}')
            count += 1

    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        # TODO: реализуйте метод
        weight_items = 0
        for item in self.items:
            weight_items += item.weight
        return weight_items

    def sum_cost(self):
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        # TODO: реализуйте метод
        sum_items = 0
        for item in self.items:
            sum_items += item.cost
        return sum_items


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

# Выводим все предметы в рюкзаке
backpack.show_items()
