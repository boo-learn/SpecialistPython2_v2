class Item:
    def __init__(self, name: str, weight: float, cost: int):
        self.name = name  # Название предмета
        self.weight = weight  # Вес предмета, в килограммах
        self.cost = cost  # Цена предмета, пусть будет, в рублях

    def show(self) -> str:
        # Возвращает строковое представление объекта Item
        return f"{self.name} вес:{self.weight} цена:{self.cost}"


class BackPack:  # рюкзак
    def __init__(self):
        self.items = []  # Предметы, которые хранятся в рюкзаке

    def add_item(self, item: Item) -> None:
        self.items.append(item.name)
        self.items.append(item.weight)
        self.items.append(item.cost)

    def show_items(self) -> None:
        return f"Предметы {self.items}"
        # TODO: реализуйте метод


# Создаем предметы
item1 = Item("Гиря", 25, 500)
item2 = Item("Арбуз", 4, 300)

# Создаем пустой рюкзак
backpack = BackPack()

# Добавляем пару предметов в рюкзак
backpack.add_item(item1)
backpack.add_item(item2)

# Выводим все предметы в рюкзаке
print(backpack.show_items())
