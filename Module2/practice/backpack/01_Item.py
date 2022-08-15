class Item:
    def __init__(self,name,weight,cost,batch):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях
        self.batch = batch  # Цена предмета, пусть будет, в рублях


    def show(self):
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost} кол-во в партии:{self.batch}"


# V TODO-1: Дополните конструктор класса Item
item1 = Item("Гиря", 25, 500, 10)
item2 = Item("Арбуз", 4, 300, 100)
item3 = Item("Ноутбук", 2.5, 22500, 1)
item4 = Item("Кот", 0.5, 250, 1)

# V TODO-2: запустите программу, посмотрите результаты функции show_item()
# print(item1.show_item())
# print(item2.show_item())
# print(item3.show_item())
# print(item4.show_item())


# TODO-3: сделайте функцию show_item(), методом show() класса Item
print(item1.show())
print(item2.show())
print(item3.show())
print(item4.show())

# TODO-4: поместите все объекты item1, item2 ... itemN в список.
#  Выведите элементы в виде нумерованного списка, при выводе используйте метод .show()
items = [item1, item2, item3, item4]
for item in items:
    print(item.show())
