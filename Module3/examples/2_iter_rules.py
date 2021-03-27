# ================================
#    Принципы работы итераторов
# ================================

test_list = [1, 2, 3, 4, 'END']
# Когда вы пишете
for el in test_list:
    print(test_list)

# Python выполняет:
# 1. Вызывает метод __iter__(): test_list.__iter__()
#   Метод __iter__() должен вернуть объект, у которого есть метод __next__()
# 2. Цикл for..in каждую итерацию вызывает метод __next__()
#   __next__() при каждом вызове возвращает следующий элемент итератора
# 3. Когда элементы итератора заканчиваются, метод __next__() возбуждает исключение StopIteration
#   for..in завершает свою работу, когда перехватывает это исключение

# Проведем обход элементов списка test_list вручную (без цикла)

print("Итерируем вручную...")
# Получаем объект-итератор
test_list_iter = iter(test_list)
# Функция iter() просто вызывает метод __iter__()

print(next(test_list_iter))
print(next(test_list_iter))
print(next(test_list_iter))
print(next(test_list_iter))
print(next(test_list_iter))

print(next(test_list_iter))  # Будет возбуждено исключение StopIteration


