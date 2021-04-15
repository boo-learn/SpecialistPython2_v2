# collections.OrderedDict - ещё один похожий на словарь объект, но он помнит порядок, в котором ему были даны ключи.
import collections

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
o_dict = collections.OrderedDict(sorted(d.items(), key=lambda t: t[0]))
print(o_dict)  # OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

# Методы, которых нет у обычного словаря:
# popitem(last=True) - удаляет последний элемент если last=True, и первый, если last=False.
# move_to_end(key, last=True) - добавляет ключ в конец если last=True, и в начало, если last=False.

# Подробнее тут: https://docs.python.org/3/library/collections.html#collections.OrderedDict