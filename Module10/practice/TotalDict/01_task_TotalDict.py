# Разработать класс TotalDict со следующими возможностями:
class TotalDict(dict):
    def __repr__(self):
        res = super().__repr__()
        return "TD:" + res

    def __add__(self, other_td):
        new_dict = self
        for el in other_td:
            if el in self:
                new_dict[el] += other_td[el]
            else:
                new_dict[el] = other_td[el]
        return new_dict

    def most_expensive(self, number=None):
        my_list = []
        i = 0
        for key, value in self.items():
            my_list.append((key, value))
            i += 1
            if i == number:
                break
        my_list.sort(key=lambda x: x[1], reverse=True)
        return my_list

# 1. Объект выводит себя в консоли как обычный словарь, НО с символами TD: в начал
items1 = TotalDict(milk=250, bread=120, meat=450.6)
items2 = TotalDict(juice=99.9, fish=120, milk=50.2)
print(items1)  # TD:{'milk': 250, 'bread': 120, 'meat': 450.6}
# 2. При сложении объектов TotalDict значения элементов с одинаковыми ключами суммируются
all_items = items1 + items2
print(all_items)  # TD:{'milk': 300.2, 'bread': 120, 'meat': 450.6, 'juice': 99.9, 'fish': 120}

# 3. Добавить метод .most_expensive() выводящий все элементы в виде списка кортежей,
# упорядоченного по убыванию по значениям
print(all_items.most_expensive())  # [('meat', 450.6), ('milk', 300.2), ('bread', 120), ('fish', 120), ('juice', 99.9)]

# 4. Метод .most_expensive() можно передать целое число, ограничивающее кол-во возвращаемых значений
print(all_items.most_expensive(3))  # [('meat', 450.6), ('milk', 300.2), ('bread', 120)] <-- только 3 кортежа
