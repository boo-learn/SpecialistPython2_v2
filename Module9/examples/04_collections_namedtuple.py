import collections

car = collections.namedtuple('Car', 'color max_speed')
# Или так:
# car = collections.namedtuple('Car', ['color',  'max_speed'])
my_car = car('red', 160)
# Car(color='red' , mileage=3812.4)

print(my_car.color)
# Можно использовать операцию * - распаковка
print(*my_car)  # red 160
# Можно обращаться по индексу
print(my_car[0])  # red
# Именованный кортеж умеет выводить себя красиво:
print(my_car)  # Car(color='red', max_speed=160)

# Но менять атрибуты после создания, нельзя:
# my_car.color = 'blue' # вызовет исключение

# именованные кортежи - краткая форма для создания вручную эффективно работающего с памятью неизменяемого класса.

# Подробнее тут: https://docs.python.org/3/library/collections.html#collections.namedtuple
