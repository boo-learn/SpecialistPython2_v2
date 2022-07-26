class Item:
    def __init__(self, item_name, item_weight, item_cost):
        self.name = item_name  # Название предмета
        self.weight = item_weight  # Вес предмета, в килограммах
        self.cost = item_cost  # Цена предмета, пусть будет, в рублях

    def show(self):
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес: {self.weight} кг цена: {self.cost} руб"


def show_item(item: Item):
    """
    Возвращает строковое представление объекта Item
    """
    return f"{item.name} вес: {item.weight} кг цена: {item.cost} руб"


# TODO-1: Дополните конструктор класса Item
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)

# TODO-2: запустите программу, посмотрите результаты функции show_item()
print(show_item(item1))
print(show_item(item2))
print(show_item(item3))
print(show_item(item4))

# TODO-3: сделайте функцию show_item(), методом show() класса Item
print(item1.show())
print(item2.show())
print(item3.show())
print(item4.show())

# TODO-4: поместите все объекты item1, item2 ... itemN в список.
#  Выведите элементы в виде нумерованного списка, при выводе используйте метод .show()
items = [
    Item("Гиря", 25, 500),
    Item("Арбуз", 4, 300),
    Item("Ноутбук", 2.5, 22500),
    Item("Кот", 0.5, 250)
]
count = 1
for item in items:
    print(f'{count}. {item.show()}')
    count += 1
