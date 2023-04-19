class Item:
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, name: str, weight: float | int, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях
        self.__value = self.cost / self. weight

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"

    def get_value(self):
        return self.__value


class BackPack:  # рюкзак
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    
    def __init__(self, max_weight=30):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_total_weight = max_weight
        self.__items_weight = 0
        self.__items_cost = 0
        self.__item_max_weight = None
        self.__item_max_vaule = None
        
    def add_items(self, items_list: list[Item]) -> None:
        """
        Добавляет предметы(items) в этот рюкзак
        """
        sorted_by_weight = self.__sort_items_by_weight(items_list)

        for item in sorted_by_weight:
            if self.__items_weight + item.weight <= self.max_total_weight:
                self.items.append(item)
                self.__items_weight += item.weight
                self.__items_cost += item.cost
            else:
                print(f'Предмет {item.name} слишком тяжелый')

        self.__item_max_weight = self.items[-1].name
        self.__item_max_vaule = self.__find_max_value_item(self.items).name

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        for i, item in enumerate(self.items, 1):
            print(f'{i}. {item.show()}')

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        return self.__items_weight

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        return self.__items_cost

    def __sort_items_by_weight(self, items_list: list) -> list:
        items_by_weight = {}
        sorted_items_by_weight = {}
        for item in items_list:
            items_by_weight[item] = item.weight  # make dict {item:weight}
        sorted_weights = sorted(items_by_weight.values())  # sorting weights in separate list
        for weight in sorted_weights:  # make dict {item:weight} sorted by weight
            for item in items_by_weight.keys():
                if items_by_weight.get(item) == weight:
                    sorted_items_by_weight[item] = weight
        return list(sorted_items_by_weight.keys())  # return items list sorted by weight

    def __find_max_value_item(self, items_list: list) -> Item:
        items_by_value = {}
        for item in items_list:
            items_by_value[item] = item.get_value()  # make dict {item:value}
        max_value = max(items_by_value.values())
        for item in items_by_value.keys():
            if item.get_value() == max_value:
                return item

    def max_weight(self):
        return self.__item_max_weight

    def max_valuable(self):
        return self.__item_max_vaule


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=32)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
items = [
    Item("Гиря", 25, 500),
    Item("Топор", 7, 1000),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
    Item("Пылесос", 5, 8000)
    ]

backpack.add_items(items)

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()

print(backpack.max_weight())

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()

print(backpack.max_valuable())
