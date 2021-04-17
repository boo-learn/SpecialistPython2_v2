# Разработать класс TotalDict со следующими возможностями:
class TotalDict(dict):
    def __repr__(self):
        return 'TD: ' + super().__repr__()
    
    def __add__(self, other):
        new_dict = self.copy()
        for el in other:
            if el in self:
                new_dict[el] += other[el]
            else:
                new_dict[el] = other[el]
        return TotalDict(new_dict)
    
    def most_expensive(self, num=None):
        lst = list(self.items())
        lst.sort(key=(lambda x: -x[1]))
        return TotalDict(lst[:num])


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
