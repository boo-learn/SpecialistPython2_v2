class Item:
    ...
    # TODO: сюда копируем реализацию класса из предыдущего задания
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
    ...
    # TODO: сюда копируем реализацию класса из предыдущего задания
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

    def sum_cost(self):
        """
        Возвращает суммарную стоимость всех предметов в рюкзаке
        """
        # TODO: реализуйте метод
        total_sum_cost = 0
        for item in self.items:
            total_sum += item.cost
        return total_sum_cost
    
    def add_items(self, items):
        """
        :param items: Список вещей(объектов класса Item)
        """
        free_weight = self.max_weight - self.sum_weight()
        for i in range(len(items)):
            min_item = min(items, key=lambda item: item.weight)
            if min_item.weight <= free_weight:
                self.items.append(min_item)
                free_weight-=min_item.weight
                items.remove(min_item)
            
        
    def max_weight_x(self):
        max_weight_x = max(self.items, key=lambda item: item.weight)
        return max_weight_x
    
    def max_value(self):
        max_valuable = max(self.items, key=lambda item: item.cost)
        return max_valuable
    
    def show_b(self):
        """
        Возвращает строковое представление объекта Item
        """
        return self.items[4].name

# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=20)

# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
items = [
    Item("Мышь компьютерная", 0.3, 2000),
    Item("Тыква", 4, 300),
    Item("Телефон", 0.5, 15000),
    Item("наушники", 5, 5000),
    Item("Штанга", 20, 7000),
]
backpack.add_items(items)
print(backpack.show_items())

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()



print(backpack.max_weight_x().show())



# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
print(backpack.max_value().show())
