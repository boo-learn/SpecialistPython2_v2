class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"

    def getter_weight(self):
        return self.weight


class BackPack:  # рюкзак
    def __init__(self, max_weight=0):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self._max_weight = max_weight
        self.__all_in = 0
        self.__price = 0

    def add_item(self, item: Item) -> None:
        """Добавляет предмет(item) в этот рюкзак"""
        if self._max_weight >= self.__all_in + item.weight:
            self.items.append(item)
            self.__all_in += item.weight
            self.__price += item.cost
        # else:
        #     print(f"Предмет {item.name} слишком тяжелый")

    def show_items(self) -> None:
        """Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка"""
        i = 1
        for item in self.items:
            print(f"{i}) {item.show()}")
            i += 1

    def sum_weight(self) -> float:
        """Возвращает суммарный вес всех предметов в рюкзаке"""
        return self.__all_in

    def sum_cost(self) -> int:
        """Возвращает суммарную стоимость всех предметов в рюкзаке"""
        return self.__price

    def add_items(self, items: list[Item]):
        """:param items: Список вещей(объектов класса Item)"""
        dct = {}
        for i in items:
            dct[i.weight] = i
        for key in sorted(dct.keys()):
            if self._max_weight >= self.__all_in + key:
                self.add_item(dct[key])

    def max_weight(self):
        weight_dct = {}
        for i in self.items:
            weight_dct[i.weight] = i.name
        return weight_dct[max(weight_dct.keys())]

    def max_valuable(self):
        price_dct = {}
        for i in self.items:
            price_dct[i.cost/i.weight] = i.name
        return price_dct[max(price_dct.keys())]


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=3)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
items = [
    Item("Запаска", 25, 500),
    Item("Наган", 4, 300),
    Item("Лаптоп", 2.5, 22500),
    Item("Змей", 0.5, 250),
    Item("Шланг", 3, 150),
    Item("Гладиолусы", 0.9, 100),
    Item("Фуа-гра из колибри", 0.1, 10000)
]

backpack.add_items(items)

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()

print(backpack.max_weight())

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
print(backpack.max_valuable())
