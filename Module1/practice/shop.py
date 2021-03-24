#!/usr/bin

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
# Преобразуйте список со словарями в список с объектами

class Item:
    def __init__(self, type, model, cost):
        self.type = type
        self.model = model
        self.cost = cost


def list_to_list(items):
    output_list = []
    for item in items:
        product = Item(item["type"], item["model"], item["cost"])
        output_list.append(product)
    return output_list

object_items = list_to_list(items)
for item in object_items:
    print(item)

print("\n\n")
# Задание-2:
# Выведите все товары в виде нумерованного списка, в формате:
# 1. Phone "Xiaomi Redmi 9" 12980 rub.
# 2. Phone ...
# т.е. сначала тип товара с заглавной буквы, затем наименование в кавычках, затем цена с указанием валюты

def num_list(items):
    for i,item in enumerate(items):
        type_of_good = item["type"][0].upper() + item["type"][1:]
        model_of_good = ' "' + item["model"] + '" '
        cost_of_good = str(item["cost"]) + " rub."
        res = str(i + 1) + ". " + type_of_good + model_of_good + cost_of_good
        print(res)

num_list(items)

print("\n\n")

def num_object_list(items):
    for i,item in enumerate(items):
        type_of_good = item.type[0].upper() + item.type[1:]
        model_of_good = ' "' + item.model + '" '
        cost_of_good = str(item.cost) + " rub."
        res = str(i + 1) + ". " + type_of_good + model_of_good + cost_of_good
        print(res)

num_object_list(object_items)
