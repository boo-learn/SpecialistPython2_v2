items = [
    {"type": "phone", "model": "Samsung A10", "cost": 24599},
    {"type": "notebook", "model": "Lenovo Ideapad 5", "cost": 48200},
    {"type": "notebook", "model": "HP 255", "cost": 40190},
    {"type": "phone", "model": "Xiaomi Redmi 9", "cost": 12980},
    {"type": "headphones", "model": "Apple AirPods Pro", "cost": 18900},
    {"type": "headphones", "model": "Sennheiser HD 206", "cost": 1235},
]

# Задание-1:
# Создайте class Item - класс для товара в интернет магазине
class Item:
    def __init__(self, item_type, model, cost):
        self.type = item_type
        self.model = model
        self.cost = cost


# Преобразуйте список со словарями в список с объектами
lst_items = []
for item in items:
    lst_items.append(Item(item["type"], item["model"], item["cost"]))

# Задание-2:
# Выведите все товары в виде нумерованного списка, в формате:
# 1. Phone "Xiaomi Redmi 9" 12980 rub.
# 2. Phone ...
# т.е. сначала тип товара с заглавной буквы, затем наименование в кавычках, затем цена с указанием валюты
for i in range(len(lst_items)):
    print(f'{i+1}. {lst_items[i].type.capitalize()} "{lst_items[i].model}" {lst_items[i].cost} rub.')
