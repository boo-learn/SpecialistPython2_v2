class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name
        self.weight = weight
        self.cost = cost

    def show_item(self) -> str:
        """
        Возвращает строковое представление объекта Item
        """
        return f"{self.name} вес:{self.weight} цена:{self.cost}"




# TODO-1: Дополните конструктор класса Item
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)
item3 = Item("Ноутбук", 2.5, 22500)
item4 = Item("Кот", 0.5, 250)

# TODO-2: запустите программу, посмотрите результаты функции show_item()
print(item1.show_item())
print(item2.show_item())
print(item3.show_item())
print(item4.show_item())
