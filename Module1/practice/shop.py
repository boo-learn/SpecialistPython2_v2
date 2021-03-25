# Задание-1:
# Создайте class Item - класс для товара в интернет магазине
# Преобразуйте список со словарями в список с объектами
class Item:
    def __init__(self, type, model, cost):
        self.type = type
        self.model = model
        self.cost = cost
items1 = [
    {"type": "Phone", "model": "Samsung A10", "cost": 24599},
    {"type": "Notebook", "model": "Lenovo Ideapad 5", "cost": 48200},
    {"type": "Notebook", "model": "HP 255", "cost": 40190},
    {"type": "Phone", "model": "Xiaomi Redmi 9", "cost": 12980},
    {"type": "Headphones", "model": "Apple AirPods Pro", "cost": 18900},
    {"type": "Headphones", "model": "Sennheiser HD 206", "cost": 1235},
]
items2 = []
for i in items1:
    items2.append(Item(i["type"], i["model"], i["cost"]))
# Задание-2:
# Выведите все товары в виде нумерованного списка, в формате:
# 1. Phone "Xiaomi Redmi 9" 12980 rub.
# 2. Phone ...
# т.е. сначала тип товара с заглавной буквы, затем наименование в кавычках, затем цена с указанием валюты
for i in range(len(items2)):
    print(f'{i+1}. {items2[i].type.capitalize()} "{items2[i].model}" {items2[i].cost} rub')
