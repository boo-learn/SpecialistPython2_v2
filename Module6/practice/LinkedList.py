# # import random
# # from enum import Enum
# #
# # # Начнем с создания карты
# # class Card:
# #     class SUITTYPE(Enum):
# #         Spades = 0
# #         Hearts = 1
# #         Diamonds = 2
# #         Clubs = 3
# #
# #     CARDTYPE_LIST = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
# #     CARDTYPE_WEIGHT = {
# #         "2": 2,
# #         "3": 3,
# #         "4": 4,
# #         "5": 5,
# #         "6": 6,
# #         "7": 7,
# #         "8": 8,
# #         "9": 9,
# #         "10": 11,
# #         "J": 12,
# #         "Q": 13,
# #         "K": 14,
# #         "A": 15
# #     }
# #     SUITTYPE_WEIGHT = {
# #         SUITTYPE.Spades: 0,
# #         SUITTYPE.Hearts: 3,
# #         SUITTYPE.Diamonds: 2,
# #         SUITTYPE.Clubs: 1
# #     }
# #
# #     SUIT_ICON = {
# #         SUITTYPE.Spades: "\u2660",
# #         SUITTYPE.Hearts: "\u2665",
# #         SUITTYPE.Diamonds: "\u2666",
# #         SUITTYPE.Clubs: "\u2663",
# #     }
# #
# #     def __init__(self, card_type, suit_type):
# #         self.card_type = card_type
# #         self.suit_type = suit_type
# #
# #     def __repr__(self):
# #         return f"{self.card_type}{Card.SUIT_ICON[self.suit_type]}"
# #
# #     def __eq__(self, other):
# #         return self.suit_type == other.suit_type
# #
# #     def __lt__(self, other):
# #         if self.card_type != other.card_type:
# #             return Card.CARDTYPE_WEIGHT[self.card_type] < Card.CARDTYPE_WEIGHT[other.card_type]
# #         else:
# #             return Card.SUITTYPE_WEIGHT[self.suit_type] < Card.SUITTYPE_WEIGHT[other.suit_type]
# #
# #     def __gt__(self, other):
# #         if self.card_type != other.card_type:
# #             return Card.CARDTYPE_WEIGHT[self.card_type] > Card.CARDTYPE_WEIGHT[other.card_type]
# #         else:
# #             return Card.SUITTYPE_WEIGHT[self.suit_type] > Card.SUITTYPE_WEIGHT[other.suit_type]
# #
# # # Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
# # class Deck:
# #     def __init__(self):
# #         self.__name = "uknown"
# #
# #         self.cards = []
# #         self.card_index = -1
# #         for card_type in Card.CARDTYPE_LIST:
# #             for suit_type in Card.SUITTYPE:
# #                 self.cards.append(Card(str(card_type), suit_type))
# #
# #     @property
# #     def name(self):
# #         return self.__name
# #
# #     @name.setter
# #     def name(self, value):
# #         self.__name = value
# #
# #     def __repr__(self):
# #         s = ""
# #         for i, card in enumerate(self.cards):
# #             if i < len(self.cards):
# #                 s += str(card) + ","
# #             else:
# #                 s += str(card)
# #         return f"Количество карт: {len(self.cards)}, карты: {s}"
# #
# #     def __iter__(self):
# #         self.card_index = -1
# #         return self
# #
# #     def __next__(self):
# #         self.card_index += 1
# #         if self.card_index >= len(self.cards):
# #             raise StopIteration
# #         return self.cards[self.card_index]
# #
# #     def __getitem__(self, item):
# #         return self.cards[item]
# #
# #     def draw(self, x):
# #         card_list = self.cards[0:x]
# #         self.cards = self.cards[x:]
# #         return card_list
# #         """
# #         order = [i for i in range(len(self.cards))]
# #         count = len(order)
# #         card_list = []
# #         for i in range(x):
# #             j = random.randint(0, count - i - 1)
# #             card_list.append(self.cards[j])
# #             self.cards.pop(j)
# #             order[j] = order[count - i - 1]
# #         return card_list
# #         """
# #
# #     def shuffle(self):
# #         random.shuffle(self.cards)
# #         """
# #         order = [i for i in range(len(self.cards))]
# #         count = len(order)
# #         for i in range(len(order)):
# #             j = random.randint(0, count - i - 1)
# #             card = self.cards[i]
# #             self.cards[i] = self.cards[j]
# #             self.cards[j] = card
# #             order[j] = order[count - i - 1]
# #         return True
# #         """
# #
# # deck = Deck()
# # deck.shuffle()
# #
# # print("10 карта:", deck[10])
# #
# # print(min(deck))
# # print(max(deck))
# #
# # for card in deck:
# #     print(card)
#
# # print(list(map(lambda card: card, deck.draw(25))), " ")
# # card1, card2 = deck.draw(2)
# #
# # print(card1)
# # print(card2)
# #
# # print(deck.draw(5))
# #
# # if card1 > card2:
# #     print(f"{card1} больше {card2}")
# # if card1 < card2:
# #     print(f"{card1} меньше {card2}")
# #
# # print(deck)
#
# # import math
# # class Point():
# #     def __init__(self, x, y):
# #         self.x = x
# #         self.y = y
# #     def get_distance(self, point):
# #         return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
# #
# # class Point3D(Point):
# #     def __init__(self, x, y, z):
# #         super().__init__(x, y)
# #         self.z = z
# #     def get_distance(self, point):
# #         return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2 + (self.z - point.z) ** 2)
#
# class Fraction:
#     def __init__(self, fraction_str):  # Дробь в конструктор передается в виде строки
#         # А мы храним дробь в виде
#         text = fraction_str.split(" ")
#         if len(text) > 1:
#             whole = int(text[0])
#             s = text[1]
#         else:
#             whole = 0
#             s = text[0]
#         self.numerator, self.denominator = map(int, s.split("/"))
#         if whole > 0:
#             self.numerator += whole * self.denominator
#
#     def __str__(self):
#         """
#         Возвращает строковое представление в формате: <Целая часть> <числитель>/<знаменатель>
#         Пример: -3 5/7
#         """
#         return ""
#
# fraction = Fraction("3 12/15")
#
# print(fraction.numerator)
# print(fraction.denominator)
"""
import random

def qsort(data, lindex, rindex):
    i = lindex
    j = rindex
    p = (lindex + rindex) >> 1
    while True:
        while data[i] < data[p]:
            i += 1
        while data[j] > data[p]:
            j -= 1
        if i <= j:
            if i < j:
                if p == i:
                    p = j
                elif p == j:
                    p = i
                l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        if i > j:
            break
    if j > lindex:
        qsort(data, lindex, j)
    if i < rindex:
        qsort(data, i, rindex)

# l = [i for i in range(10)]
# random.shuffle(l)

l = [5, 0, 2, 3, 7, 4, 9, 8, 6, 1]
print(l)

qsort(l, 0, len(l) - 1)

print(l)
"""
"""
import random

def quick_sort(data, compare = lambda a, b: a < b, lindex = -1, rindex = -1):
    if lindex < 0:
        lindex = 0
    if rindex < 0:
        rindex = len(data) - 1
    i, j = lindex, rindex
    p = data[(lindex + rindex) // 2]
    count = 0
    while i <= j:
        while compare(data[i], p): i += 1
        while compare(data[p], j): j -= 1
        if i <= j:
            l[i], l[j] = l[j], l[i]
            count += 1
            i, j = i + 1, j - 1
    count += quick_sort(data, compare, lindex, j) if j > lindex else 0 + quick_sort(data, compare, i, rindex) if i < rindex else 0
    return count

def binary_search(l, value, lindex=-1, rindex=-1):
    if lindex == -1:
        lindex = 0
    if rindex == -1:
        rindex = len(l) - 1
    while lindex < rindex:
        index = (lindex + rindex) // 2
        if l[index] < value:
            lindex = index + 1
        elif l[index] > value:
            rindex = index - 1
        else:
            return index
    return -1

# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    return [random.randint(at, to) for _ in range(size)]

l = gen_list(100, 0, 10)

print(l)

l = list(set(l))

# quick_sort(l, lambda a, b: a > b)
print(l)
"""
"""
# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:
employee = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]
# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.

employee.sort(key=lambda a: (a["surname"], a["name"]))
print(employee)
"""
class Node:
    """
    Класс для узла списка. Хранит значение и указатель на следующий узел.
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = 'LinkedList [' + str(current.value) + (',' if current.next is not None else '')
            while current.next is not None:
                current = current.next
                out += str(current.value) + (',' if current.next is not None else '')
            return out + ']'
        return 'LinkedList []'

    def clear(self):
        current = self.first
        while current.next is not None:
            temp = current
            current = current.next
            del temp
        self.__init__()

    def add(self, value):
        """
        Добавляем новое значение value в конец списка
        """
        new_node = Node(value, None)  # Создаем новый узел
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел, т.к. он единственный
            self.last = new_node
            self.first = new_node
        else:
            self.last.next = new_node
            self.last = new_node

    def push(self, value):
        """
        Добавляет элемент со значением value в начало списка
        """
        if self.first is None:  # Если список был пуст
            # self.first и self.last будут указывать на один и тотже узел
            self.last = self.first = Node(value, None)
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def insert(self, value, index):
        i = 0
        prev = None
        next = None
        while True:
            if next is None:
                next = self.first
            else:
                next = next.next

            if i == index:
                new_node = Node(value, next)
                if prev is None:
                    self.first = new_node
                else:
                    prev.next = new_node
                if next is None:
                    self.last = new_node
                return
            i += 1

            prev = next
            if prev is None and next is None:
                break

    def find(self, value):
        """
        Ищет элемент со зачением value
        :param value: значение искомого элемента
        :return: индекс искомого элемента, или ???, если элемент не найден
        """
        # TODO: реализовать поиск элемента
        #   подумать над возвращаемым значением, если элемент со значение value не найден
        raise TypeError("Not implemented")

    def len(self):
        # TODO: сделать более быструю реализацию, т.к. каждый раз проходка по всем элементам - долго
        length = 0
        if self.first is not None:
            current = self.first
            while current.next is not None:
                current = current.next
                length += 1
        return length + 1  # +1 для учета self.first


if __name__ == "__main__":
    L = LinkedList()
    print("empty list = ", L)
    L.add(1)
    L.add(2)
    L.add(3)

    print("list = ", L)

    L.insert(100, 3)

    print("list = ", L)

    L.clear()

    print("list = ", L)

    # TODO: реализовать интерфейс итерации
    # for el in L:
    #     print(el)
    # Напомню принцип работы итератора:
    # iterator_L = iter(L) L.__iter__()
    # next(iterator_L) it.__next__()
    # next(iterator_L)
    # next(iterator_L)
    # next(iterator_L)

    # TODO: реализовать обращение по индексу и изменение значение по индексу
    # print(L[0])
    # L[0] = "new"
    # print(L[0])

    # TODO: реализовать создание нового списка с задание начальных элементов
    # L = LinkedList(2, 4, 6, -12)
    # print(L)
