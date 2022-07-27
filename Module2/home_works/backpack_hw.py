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
        free_weight = self.max_weight - self.sum_weight()
        if item.weight <= free_weight:
            self.items.append(item)
        else:
            print(f"Предмет {item.name} слишком тяжелый")

    def show_items(self):
        i = 1
        for item in self.items:
            print(f'{i}: {item.show()}')
            i += 1

    def sum_weight(self):
        total_sum = 0
        for item in self.items:
            total_sum += item.weight
        return total_sum

    def sum_cost(self):
        total_sum = 0
        for item in self.items:
            total_sum += item.cost
        return total_sum
    
    def max_weight_item(self):
        heavy_item = max(self.items, key=lambda item: item.weight)
        print("Самый тяжелый предмет", heavy_item.show())
        
    def max_valuable(self):
        cold_item = max(self.items, key=lambda item: item.cost)
        print("Самый дорогой предмет", cold_item.show())    

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
item1 = Item("Фонарь", 0.5, 500)
item2 = Item("Сух паек", 1, 200)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Нож", 0.5, 700)
item5 = Item("Палатка", 10, 5000)
item6 = Item("Рация", 2, 400)
item7 = Item("Грузы", 5, 1000)
item8 = Item("Стул", 2, 2500)

backpack = BackPack(max_weight=20)

backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item4)
backpack.add_item(item5)
backpack.add_item(item6)
backpack.add_item(item7)
backpack.add_item(item8)
# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
    def max_weight_item(self):
        heavy_item = max(self.items, key=lambda item: item.weight)
        print("Самый тяжелый предмет", heavy_item.show())

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
    def max_valuable(self):
        cold_item = max(self.items, key=lambda item: item.cost)
        print("Самый дорогой предмет", cold_item.show())

        
backpack.max_weight_item()
backpack.max_valuable()      
