class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight: int):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        # максимальный суммарный вес предметов, которые можно положить в рюкзак
        self.max_weight = max_weight
        self.current_weight = 0

    # TODO: сюда копируем реализацию класса из предыдущего задания

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.max_weight - self.current_weight >= item.weight:
            self.items.append(item)
            self.current_weight += item.weight
        else:
            print(f"Предмет {item.name} слишком тяжелый")

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        # TODO: реализуйте метод
        for i, item in enumerate(self.items):
            print(f"{i+1}) {item.name}")

    # TODO: добавьте новое свойство .max_weight - максимальный суммарный вес предметов, которые можно положить в рюкзак

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        # TODO: реализуйте метод
        summa = 0
        for item in self.items:
            summa += item.weight
        return summa

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        sum_cost = 0
        # TODO: реализуйте метод
        for item in self.items:
            sum_cost += item.cost
        return sum_cost

    def add_items(self, items: list) -> None:
        items.sort(key=lambda item: item.weight)
        for item in items:
            self.add_item(item)

    def max_weight_item(self) -> None:
        max_w_item = max(self.items, key=lambda item: item.weight)
        print(max_w_item.show())

    def max_valuable(self) -> None:
        max_valuable_item = max(
            self.items, key=lambda item: item.cost/item.weight)
        print(max_valuable_item.show())


# Создаем предметы
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250),
    Item("Трос", 3, 150),
    Item("Титаник", 104, 150),
    Item("Бриллиант", 0.01, 100000)
]

# Создаем пустой рюкзак и указываем его вместимость(в кг)
backpack = BackPack(max_weight=20)

# Пытаемся добавлять максимальное кол-во предметов в рюкзак
backpack.add_items(items)

# Выводим все предметы в рюкзаке
backpack.show_items()
backpack.max_weight_item()
backpack.max_valuable()
