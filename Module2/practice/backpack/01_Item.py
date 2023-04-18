class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show(self):
        return f"{self.name}; вес:{self.weight}; цена:{self.cost}"


def show_item(item: Item) -> str:
    """
    Возвращает строковое представление объекта Item
    """
    return item.show()


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

print()
# TODO-3: сделайте функцию show_item(), методом show() класса Item
print(item1.show())
print(item2.show())
print(item3.show())
print(item4.show())

print()
# Помещаем все объекты item в список:
items = [item1, item2, item3, item4]
# TODO-4:  Выведите элементы в виде нумерованного списка, при выводе используйте метод .show()
for n, item in enumerate(items):
    print(f"{n+1}. {item.show()}")
