import collections

# collections.Counter - вид словаря, который позволяет нам считать количество неизменяемых объектов
counter = collections.Counter()

for word in ['banana', 'egg', 'banana', 'apple', 'apple', 'apple']:
    counter[word] += 1

print("counter=", counter)  # Counter({'apple': 3, 'banana': 2, 'egg': 1})

print("counter.elements()-->", list(counter.elements()))  # ['banana', 'banana', 'egg', 'apple', 'apple', 'apple']
# .elements - возвращает список всех элементов

# Можно создавать так:
counter2 = collections.Counter(a=4, b=2, c=0, d=-2)
print("counter2.elements()-->", list(counter2.elements()))

# А можно и из строки:
counter3 = collections.Counter('abracadabra')
print("counter3.most_common()-->", counter3.most_common())  # [('a', 5), ('b', 2), ('r', 2), ('c', 1), ('d', 1)]
print("counter3.most_common(3)-->", counter3.most_common(3)) # [('a', 5), ('b', 2), ('r', 2)]
# Подробнее тут: https://docs.python.org/3/library/collections.html#collections.Counter