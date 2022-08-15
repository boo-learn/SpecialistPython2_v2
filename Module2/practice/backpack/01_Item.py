class Item:
    def __init__(self, name, weight, price):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = price  # Цена предмета, пусть будет, в рублях

    def show_item(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"

    def show(self):
        return f"{self.name} вес:{self.weight} цена:{self.cost}"

item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)

print(item1.show_item())
print(item2.show_item())
print(item3.show_item())
print(item4.show_item())

print(item1.show())
print(item2.show())
print(item3.show())
print(item4.show())

# TODO-4: поместите все объекты item1, item2 ... itemN в список.
#  Выведите элементы в виде нумерованного списка, при выводе используйте метод .show()
items = [item1, item2, item2, item4]
n=0
for item in items:
    n += 1
    print(n, item.show())
