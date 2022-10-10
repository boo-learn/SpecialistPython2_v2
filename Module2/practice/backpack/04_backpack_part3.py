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
        # TODO: реализуйте метод так, чтобы из переданного списка предметов выбиралось и помещалось в рюкзак,
        #  максимальное количество, с учетом ограничения общего веса в рюкзаке. Т.е. берем самые легкие предметы.


# Создаем предметы
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
]

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=7)

# Пытаемся добавлять максимальное кол-во предметов в рюкзак
backpack.add_items(items)

# Выводим все предметы в рюкзаке
backpack.show_items()
