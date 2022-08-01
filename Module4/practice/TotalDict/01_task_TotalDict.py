# Разработать класс TotalDict со следующими возможностями:
# 1. Объект выводит себя в консоли как обычный словарь, НО с символами TD: в начал
# 2. При сложении объектов TotalDict значения элементов с одинаковыми ключами суммируются
# 3. Добавить метод .most_expensive() выводящий все элементы в виде списка кортежей,
# упорядоченного по убыванию по значениям
# 4. Метод .most_expensive() можно передать целое число, ограничивающее кол-во возвращаемых значений

class TotalDict(dict):
    pass
    def __str__(self):
        return f"TD: {dict.__str__(self)}"
    def __add__(self,other):
        new_dict=self
        for el_key,el_value in other.items():
            if el_key in new_dict:
                new_dict[f"{el_key}"]=el_value+new_dict[f"{el_key}"]
            else:
                new_dict[f"{el_key}"] = el_value
        return new_dict
    def most_expensive(self,n=None):

        list_dict=[]
        for el_key,el_value in self.items():
            tup_dict=el_key,el_value
            list_dict.append(tup_dict)

        def for_sort(el):
           return el[1]
        list_dict.sort(key=for_sort,reverse=True)

        new_list=[]
        if n is not None:
            for i in range(n):
                new_list.append(list_dict[i])
        else:
            new_list=list_dict
        return new_list

items1 = TotalDict(milk=250, bread=120, meat=450.6)
items2 = TotalDict(juice=99.9, fish=120, milk=50.2)
print(items1)  # TD:{'milk': 250, 'bread': 120, 'meat': 450.6}

all_items = items1 + items2
print(all_items)  # TD:{'milk': 300.2, 'bread': 120, 'meat': 450.6, 'juice': 99.9, 'fish': 120}

print(all_items.most_expensive())  # [('meat', 450.6), ('milk', 300.2), ('bread', 120), ('fish', 120), ('juice', 99.9)]

print(all_items.most_expensive(3))  # [('meat', 450.6), ('milk', 300.2), ('bread', 120)] <-- только 3 кортежа
