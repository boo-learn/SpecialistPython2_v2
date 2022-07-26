class Item:
    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self, max_weight):
        self.items = []  # Предметы, которые хранятся в рюкзаке
        self.max_weight = max_weight

    def add_item(self, item: Item):
        free_space = self.max_weight - self.sum_weight()
        if item.weight > free_space:
            print("Превышен максимальный вес рюкзака")
            return
        self.items.append(item)

    def show_items(self):
        print("В рюкзаке: ")
        i = 1
        for item in self.items:
            print(f"{i} {item.show()}")
            i += 1

    def sum_weight(self):
        sum_load = 0
        for item in self.items:
            sum_load += item.weight
        return sum_load

    def sum_cost(self):
        sum_cost = 0
        for item in self.items:
            sum_cost += item.cost
        return sum_cost

    def maximum_weight(self):
        highest_weight = 0
        most_weight_item = ()
        for item in self.items:
            if item.weight > highest_weight:
                most_weight_item = item
                highest_weight = most_weight_item.weight
        return most_weight_item

    def max_valuable(self):
        most_valuable = ()
        highest_value = 0
        for item in self.items:
            if item.cost / item.weight > highest_value:
                most_valuable = item
                highest_value = item.cost / item.weight
        return most_valuable


# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=30)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 4, 2500)
item5 = Item("Книга", 2, 1500)
item6 = Item("Зонтик", 0.6, 700)

backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
backpack.add_item(item5)
backpack.add_item(item6)

heaviest_item = backpack.maximum_weight()
most_valuable_item = backpack.max_valuable()

print(f"Самый тяжелый предмет -  {heaviest_item.name} весом {heaviest_item.weight} кг")
print (f"Самый ценный предмет - {most_valuable_item.name} с ценой за единицу веса {most_valuable_item.cost / most_valuable_item.weight} рублей")
