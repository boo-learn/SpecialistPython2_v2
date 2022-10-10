class Item:

    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(item) -> str:
        return f"{item.name} вес:{item.weight} цена:{item.cost}"
    # TODO: сюда копируем реализацию класса из предыдущего задания


class BackPack:  # рюкзак

    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.sum_weight()+item.weight > self.max_weight:
            print(f"Предмет {item.name} слишком тяжелый")
        else:
            self.items.append(item)
        # TODO: реализуйте метод

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for index, item in enumerate(self.items):
            print(index + 1, item.show())

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        weight = 0
        for item in self.items:
            weight += item.weight
        return weight
        # TODO: реализуйте метод

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        cost = 0
        for item in self.items:
            cost += item.cost
        return cost

    # TODO: сюда копируем реализацию класса из предыдущего задания



    def add_items(self, items):
        """
        :param items: Список вещей(объектов класса Item)
        """
        items.sort(key=lambda x: x.weight)
        for item in items:
            self.add_item(item)

    def max_weight_item(self):
        weight_list = []
        for item in backpack.items:
            weight_list.append(item.weight)
            maximum = max(weight_list)
        for item in backpack.items:
            if item.weight == maximum:
                return item.name

    def max_valuable(self):
        value_list = []
        for item in backpack.items:
            value_list.append(item.cost/item.weight)
            maximum = max(value_list)
        for item in backpack.items:
            if item.cost/item.weight == maximum:
                return item.name






        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.
# Создаем рюкзак, указываем максимальный вес


# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
items = [Item('Мяч', 1, 300),
         Item('Банка', 5, 100),
         Item('Наушники', 0.2, 300),
         Item('Кошелек', 0.3, 20000),
         Item('Телефон', 0.5, 10000),
         Item('Термос', 2, 2000)]
backpack = BackPack(max_weight=10)
backpack.add_items(items)
#print(backpack.show_items())

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()
print(backpack.max_weight_item())
# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
print(backpack.max_valuable())
