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

    def __init__(self, max_weight):
        self.items = []
        self.max_weight = max_weight

    def add_item(self, item: Item) -> None:
        free_weight = self.max_weight - self.sum_weight()
        if free_weight >= item.weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")

    def show_items(self):
        for i, item in enumerate(self.items, 1):
            print(f"{i}) {item.show()}")

    def sum_weight(self) -> float:
        """
        Возвращает суммарный вес всех предметов в рюкзаке
        """
        summa = 0
        for item in self.items:
            summa += item.weight
        return summa

    def sum_cost(self) -> int:
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        all_cost = 0
        for item in self.items:
            all_cost += item.cost
        print(all_cost)
        return all_cost

    def max_weight_in(self):
        max_weight_in = 0
        name_best = None
        for item in self.items:
            if item.weight > max_weight_in:
                max_weight_in = item.weight
                name_best = item.name
        return name_best

    def max_valuable(self):
        max_cost_per_weight = 0

        name_best = None
        for item in self.items:
            current_max = item.cost / item.weight
            if max_cost_per_weight < current_max:
                max_cost_per_weight = current_max
                name_best = item.name
        return name_best


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=1)

item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Арбуз2", 2, 300)
item4 = Item("Ноутбук", 2.5, 22500)
item5 = Item("Кот", 0.5, 250)
item6 = Item("Кот_2", 0.1, 250)

backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
backpack.add_item(item5)
backpack.add_item(item6)


print(backpack.max_weight_in())
print(backpack.max_valuable())
