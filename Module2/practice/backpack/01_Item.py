class Item:
    def __init__(self, name, weight, cost):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


# TODO-1: Дополните конструктор класса Item
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)

# TODO-3: сделайте функцию show_item(), методом show() класса Item
print(item1.show())
print(item2.show())
print(item3.show())
print(item4.show())

# TODO-4: поместите все объекты item1, item2 ... itemN в список.
#  Выведите элементы в виде нумерованного списка, при выводе используйте метод .show()
items = [item1, item2, item3, item4]
i = 1

print ("Backpack contains: ")
for item in items:
    print (f"{i} {item.show()}")
    i += 1
