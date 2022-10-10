class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name # Название предмета
        self.weight = weight # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight  # максимальный суммарный вес предметов, которые можно положить в рюкзак

    def add_item(self, item: Item) -> None:
        """
        Добавляет предмет(item) в этот рюкзак
        """
        if self.sum_weight() + item.weight <= self.max_weight:
            self.items.append(item)
        else:
            print(item.name, 'не поместился в рюкзак')

    def show_items(self) -> None:
        """
        Выводит(print'ом) все предметы, содержащиеся в рюкзаке в виде нумерованного списка
        """
        i = 1
        for item in self.items:
            print(i, item.show())
            i += 1

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        total_weight = 0
        for item in self.items:
            total_weight += item.weight
        return total_weight

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        total_cost= 0
        for item in self.items:
            total_cost += item.cost
        return total_cost


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
