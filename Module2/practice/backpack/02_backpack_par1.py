class Item:
    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f" {self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self):
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def add_item(self, item: Item):

        # Добавляет предмет(item) в этот рюкзак

        self.items.append(item)
        # TODO: реализуйте метод

    def show_items(self):
        for item in self.items:
           # print(item.show())
            print(f" {item.show()} ")
       # Вывод все предметы, содержащиеся в рюкзаке в виде нумерованного списка
       # return f" {self.items} "
        # TODO: реализуйте метод


#s = [1, 2, 3]
# print(s)
# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)

# Создаем пустой рюкзак
backpack = BackPack()

# Добавляем пару предметов в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)

# Выводим все предметы в рюкзаке
backpack.show_items()
# print(backpack)
# for item in range(len(items)):
   # print(backpack[item].show())
