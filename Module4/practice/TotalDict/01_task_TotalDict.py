# Разработать класс TotalDict со следующими возможностями:
class TotalDict(dict):
    def __repr__(self):
        return f"TD:{super().__repr__()}"

    pass

    def __add__(self, other):
        new_dict = self
        for key, value in other.items():
            if key in self:
                new_dict[key] += value
            else:
                new_dict.update({key: value})
        return new_dict

    def most_expensive(self):
        sorted_tuple = sorted(self.items(), key=lambda x: -x[1])
        return sorted_tuple


# 1. Объект выводит себя в консоли как обычный словарь, НО с символами TD: в начал
items1 = TotalDict(milk=250, bread=120, meat=450.6)
items2 = TotalDict(juice=99.9, fish=120, milk=50.2, bread=150)
print(items1)  # TD:{'milk': 250, 'bread': 120, 'meat': 450.6}
print(items2)  # TD:{'milk': 250, 'bread': 120, 'meat': 450.6}
# 2. При сложении объектов TotalDict значения элементов с одинаковыми ключами суммируются
all_items = items1 + items2
print(all_items)  # TD:{'milk': 300.2, 'bread': 120, 'meat': 450.6, 'juice': 99.9, 'fish': 120}

# 3. Добавить метод .most_expensive() выводящий все элементы в виде списка кортежей,
# упорядоченного по убыванию по значениям
print(all_items.most_expensive())  # [('meat', 450.6), ('milk', 300.2), ('bread', 120), ('fish', 120), ('juice', 99.9)]

# 4. Метод .most_expensive() можно передать целое число, ограничивающее кол-во возвращаемых значений
# print(all_items.most_expensive(3))  # [('meat', 450.6), ('milk', 300.2), ('bread', 120)] <-- только 3 кортежа
