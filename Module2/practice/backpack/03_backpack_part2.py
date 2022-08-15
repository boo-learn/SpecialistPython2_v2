class Item:
    def __init__(self,name,weight,cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях


    def show(self):
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"
    # TODO: сюда копируем реализацию класса из предыдущего задания



class BackPack:  # рюкзак

    # TODO: сюда копируем реализацию класса из предыдущего задания
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        res = self.max_weight - sum(item1.weight for item1 in self.items) - item.weight
        if res > 0:
            self.items.append(item)
        else:
            print(f'Предмет {item.name} слишком тяжелый')

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """

        for n, item in enumerate(self.items, 1):
            print(n, item.show())


    # TODO: добавьте новое свойство .max_weight - максимальный суммарный вес предметов, которые можно положить в рюкзак

    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        # TODO: реализуйте метод

        max_weight_all = sum(item.max_weight for item in self.items)

        return

    def sum_cost(self):
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        # TODO: реализуйте метод

        sum_cost = sum(item.cost for item in self.items)


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
