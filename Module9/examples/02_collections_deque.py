import collections

queue = collections.deque()

print(queue)  # deque([]) - пустая очередь

queue.append("read book")  # Добавляет элмент в очередь
queue.append("sleep")  # Добавляет элмент в очередь
print(queue)  # deque(['read book', 'sleep'])

queue.popleft()  # Удаляет первый(левый) элемент очереди
print(queue)  # deque(['sleep'])

# Методы очереди:

# append(x) - добавляет x в конец.
#
# appendleft(x) - добавляет x в начало.
#
# clear() - очищает очередь.
#
# count(x) - количество элементов, равных x.
#
# extend(iterable) - добавляет в конец все элементы iterable.
#
# extendleft(iterable) - добавляет в начало все элементы iterable (начиная с последнего элемента iterable).
#
# pop() - удаляет и возвращает последний элемент очереди.
#
# popleft() - удаляет и возвращает первый элемент очереди.
#
# remove(value) - удаляет первое вхождение value.
#
# reverse() - разворачивает очередь.
#
# rotate(n) - последовательно переносит n элементов из начала в конец (если n отрицательно, то с конца в начало).

# Подробнее тут: https://docs.python.org/3/library/collections.html#collections.deque
