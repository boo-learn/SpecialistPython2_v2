
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
num = 1
for i in items1:
    items2.append(Item(i["type"], i["model"], i["cost"]))

for i in items2:
    print('{}.'.format(num), i.type, '"{}"'.format(i.model), i.cost, "rub.")
    num += 1
Iphone = Item("phone", "Samsung A10", 24599)
