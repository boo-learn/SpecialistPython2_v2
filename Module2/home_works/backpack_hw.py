class Item:
    def __init__(self, name,weight,cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях
    def __repr__(self):
        return '{' + self.name + ', ' + str(self.weight) + ', ' + str(self.cost) + '}'
    def show(self):
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"

class BackPack:  # рюкзак
    def __init__(self,max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight #максимальный суммарный вес предметов, которые можно положить в рюкзак

    def add_item(self, it: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        self.items.append(it)
        #print(it.show())

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        #print(self.items)
        for it in self.items:
            #print(it.name)
            print(it.show())

    # TODO: добавьте новое свойство .max_weight - максимальный суммарный вес предметов, которые можно положить в рюкзак
    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        res_sum=0
        for it in self.items:
            #print(it.name)
            res_sum=res_sum + it.weight
        return res_sum

    def sum_cost(self):
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        res_cost=0
        for it in self.items:
            #print(it.name)
            res_cost=res_cost + it.cost
        return res_cost

    def add_items(self, items):
        """
        :param items: Список вещей(объектов класса Item)
        """
        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.
        print(items)
        items.sort(key=lambda x: x.weight)
        print(items)
        for it in items:
            if (self.sum_weight()+it.weight)<=self.max_weight: #то добавляем
                self.add_item(it)
            else: #перебор
                print("Не могу добавить ",it)
    def max_weight_item(self):
        self.items.sort(key=lambda x: x.weight, reverse=True)
        print(self.items)
        return self.items[0]
    def max_valuable(self):
        self.items.sort(key=lambda x: x.weight*x.cost, reverse=True)
        print(self.items)
        return self.items[0]
# Создаем предметы
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=30)


# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
backpack.add_items(items)
print("В рюказаке ",backpack.items," предметов")

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()
print(backpack.max_weight_item())

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
print(backpack.max_valuable())
