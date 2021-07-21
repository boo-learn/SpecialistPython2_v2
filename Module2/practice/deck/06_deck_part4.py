import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    # Выводит значение в юникод формате
    def __str__(self):
        icons = {'Hearts': '\u2665',
                'Diamonds': '\u2666',
                'Clubs': '\u2663',
                'Spades': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def __eq__(self, card):
        return self.let_to_int(self.value) == self.let_to_int(card.value)

    def __gt__(self, card):
        return self.let_to_int(self.value) > self.let_to_int(card.value)

    def __lt__(self, card):
        return self.let_to_int(self.value) < self.let_to_int(card.value)

    def __ge__(self, card):
        return self.let_to_int(self.value) >= self.let_to_int(card.value)

    def __le__(self, card):
        return self.let_to_int(self.value) <= self.let_to_int(card.value)

    def __ne__(self, card):
        return self.let_to_int(self.value) != self.let_to_int(card.value)

    def let_to_int(self, value):
        values_of_lets = {
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }
        if value in values_of_lets.keys():
            return int(values_of_lets[value])
        return int(value)

    def equal_suit(self, other_card):
        return other_card.suit == self.suit


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        list_of_cards_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        list_of_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.last_index_card = None
        self.cards = [Card(values, suit=suits) for suits in list_of_suits for values in list_of_cards_values]

    def __str__(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        deck_string = ', '.join(map(lambda card: str(card), self.cards))
        return f'deck[{len(self.cards)}] {deck_string}'

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_slice = []
        for card in self.cards[:x]:
            cards_slice.append(card)
        del self.cards[:x]
        return cards_slice

    def shuffle(self):
        random.shuffle(self.cards)
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if self.last_index_card is None:
            self.last_index_card = 0
        else:
            self.last_index_card += 1
        if self.last_index_card >= len(self.cards):
            raise StopIteration
        return self.cards[self.last_index_card]

deck = Deck()
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
print(deck)  # вместо print(deck.show())
deck.shuffle()
card1, card2 = deck.draw(2)
# 2. Вывод карты в терминал:
print(card1)  # вместо print(card1.to_str())
print(card2)  # вместо print(card1.to_str())
#
# # 3. Сравнение карт: !!!!ДОМАШКА!!!!  <---------------
if card1 > card2:
    print(f"{card1} больше {card2}")
elif card1 < card2:
    print(f"{card1} меньше {card2}")
#
# # 4. Итерация по колоде:  !!!!ДОМАШКА!!!!  <---------------
for card in deck:
    print(card)
#
# 5. Просмотр карты в колоде по ее индексу:
print(deck[6])
#
#
# # Список ВСЕХ magic-методов см. тут: http://pythonworld.ru/osnovy/peregruzka-operatorov.html
