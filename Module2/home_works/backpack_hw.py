class Item:
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def __init__(self, name, weight, cost):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self):
        print('Предмет {}'.format(self.name))
        print('Вес {}'.format(self.weight))
        print('Стоимость {}'.format(self.cost))
        print()


class BackPack:  # рюкзак
    max_valuable_in_backpack = 0
    max_weight_in_backpack = 0
    
    def __init__(self, max_weight: float):
        self.max_weight = max_weight
        self.items = {}
    
    # TODO-0: копируем реализацию всех методов из практики или дописываем самостоятельно
    def add_item(self, item: Item) -> None:
        self.items[item.name] = [item.weight, item.cost]

    def show_items(self) -> None:
        print('В рюкзаке находятся')
        for key, value in self.items.items():
            print(key)
    
    def max_valuable(self):        
        for key, value in self.items.items():
            if value[1] > BackPack.max_valuable_in_backpack:
                BackPack.max_valuable_in_backpack = value[1]
    
    def def_max_weight(self):
        for key, value in self.items.items():
            if value[0] > BackPack.max_weight_in_backpack:
                BackPack.max_weight_in_backpack = value[0]

# Создаем рюкзак, указываем максимальный вес
backpack = BackPack(max_weight=...)


item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 3, 300)
item3 = Item("Дыня", 4, 430)
item4 = Item("Футбольный мяч", 1, 1000)
item5 = Item("Ноутбук", 3, 5700)

item1.show()
item2.show()
item3.show()
item4.show()
item5.show()

backpack = BackPack(35)
backpack.add_item(item1)
backpack.add_item(item2)
backpack.add_item(item3)
backpack.add_item(item5)

backpack.show_items()

backpack.max_valuable()
print('Стоимость самого ценного предмета {}'.format(BackPack.max_valuable_in_backpack))

backpack.def_max_weight()
print('Самый тяжелый предмет {}'.format(BackPack.max_weight_in_backpack))


# TODO-1: Создаем 5-8 предметов и добавляем их в рюкзак
...

# TODO-2: В рюкзаке найдите самый тяжелый предмет и выведите его на экран
#  поиск предмета реализуйте в виде метода .max_weight()

# TODO-3: В рюкзаке найдите самый ценный предмет и выведите его на экран
#  ценным предметом, считать предмет, с самым высоким значение цены на единицу веса
#  поиск предмета реализуйте в виде метода .max_valuable()
