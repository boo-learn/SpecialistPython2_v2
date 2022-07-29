class Item:

    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name:10} вес:{self.weight:3} цена:{self.cost:5}"
    # TODO: сюда копируем реализацию класса из предыдущего задания


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        # TODO: реализуйте метод
        if type(item) == Item:
            current_weight = 0
            for it in self.items:
                current_weight += it.weight
            if ((current_weight + item.weight) < self.max_weight):
                self.items.append(item)
            else:
                print(f"Предмет {item.name} слишком тяжелый")

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        # TODO: реализуйте метод
        i = 1
        for it in self.items:
            print(f'{i}) - {it.show()}')
            i += 1

    # TODO: сюда копируем реализацию класса из предыдущего задания
    # TODO: добавьте новое свойство .max_weight - максимальный суммарный вес предметов, которые можно положить в рюкзак

    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        # TODO: реализуйте метод
        sum_allweight = 0
        for items in self.items:
            sum_allweight += items.weight
        return sum_allweight

    def sum_cost(self):
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        # TODO: реализуйте метод
        sum_allcost = 0
        for items in self.items:
            sum_allcost += items.cost
        return sum_allcost

    # TODO: сюда копируем реализацию класса из предыдущего задания

    def add_items(self, items):
        """
        :param items: Список вещей(объектов класса Item)
        """
        print(type(items))
        if type(items) == list:
            current_weight = 0
            for itm_ in items:
                if ((current_weight + itm_.weight) < self.max_weight):
                    self.items.append(itm_)
                    current_weight += itm_.weight

        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.


def sort_key(incominglist):
    return incominglist.weight


# Создаем предметы
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

items.sort(key=sort_key, reverse=False)

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=7)

# Пытаемся добавлять максимальное кол-во предметов в рюкзак
backpack.add_items(items)

# Выводим все предметы в рюкзаке
backpack.show_items()

print(f" Суммарный вес всех предметов - {backpack.sum_weight()}")
