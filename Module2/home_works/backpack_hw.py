class Item:
    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item):
        """
        Добавляет предмет(item) в этот рюкзак
        """
        free_weight = self.max_weight - self.sum_weight()
        if item.weight <= free_weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")

    def show_items(self):
        """
        Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        i = 1
        for item in self.items:
            print(f'{i}: {item.show()}')
            i += 1

    def sum_weight(self):
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        total_sum = 0
        for item in self.items:
            total_sum += item.weight
        return total_sum

    def heavy_item(self):
        """
        Возвращает вес и название самого тяжелого предмета в рюкзаке
        """

        heavy_item = self.items[0]

        for item in self.items:
            if item.weight > heavy_item.weight:
                heavy_item = item

        print(f'самый тяжелый предмет - {heavy_item.name}, весит {heavy_item.weight} кг')

    def max_valuable(self):

        valuable_item = self.items[0]

        for item in self.items:
            if (item.cost / item.weight) > (valuable_item.cost / valuable_item.weight):
                valuable_item = item

        print ( f'самый ценный предмет - {valuable_item.name}, стоит {valuable_item.cost/valuable_item.weight} на кг веса')

# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=10)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
items = [Item('Книга', 1, 100),
         Item('Ноутбук', 3, 25000),
         Item('Зонтик', 0.5, 500),
         Item('Минералка', 1, 100),
         Item('Кошелек', 0.1, 10000),
         Item('Гиря', 10, 200),
         Item('Пауэрбанк', 1, 2000),
         Item('Черная дыра', 5000000, 0)
         ]

for item in items:
    backpack.add_item(item)

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .heavy_item()

backpack.heavy_item()

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()

backpack.max_valuable()
