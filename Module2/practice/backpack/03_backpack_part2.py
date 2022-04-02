class Item:
    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"



class BackPack:  # рюкзак
    ...
    # TODO: сюда копируем реализацию класса из предыдущего задания
    # TODO: добавьте новое свойство .max_weight - максимальный суммарный вес предметов, которые можно положить в рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight
        self.__weight = 0
        self.__cost = 0

    def add_item(self, item: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.__weight + item.weight <= self.max_weight:
            self.items.append(item)
            self.__weight += item.weight
            self.__cost += item.cost
        else:
            print(f"Предмет {item.name} слишком тяжел для рюкзака")

    def pop_item(self, item: Item):
        if item in self.items:
            self.items.pop(self.items.index(item))
            self.__weight -= item.weight
            self.__cost -= item.cost
        else:
            print(f"Предмет {item.name} не находится в рюкзаке")

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, item in enumerate(self.items):
            print(f"{i+1}.", item.show())

    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        return self.__weight

    def sum_cost(self):
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        return self.__cost


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

backpack.pop_item(item3)
backpack.pop_item(item2)

backpack.show_items()
