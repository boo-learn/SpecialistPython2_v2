# Начнем с создания карты
import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {"Hearts": '\u2665',
                 "Diamonds": '\u2666',
                 "Spades": '\u2660',
                 "Clubs": '\u2663'}
        return f'{self.value}{icons[self.suit]}'

    def equal_suit(self, other_card):   # сравниваем масти
        return self.suit == other_card.suit

    def more(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
        if values.index(self.value) > values.index(other_card.value) or \
           (values.index(self.value) == values.index(other_card.value) and
            suits.index(self.suit) > suits.index(other_card.suit)):
            return True
        else:
            return False

    def less(self, other_card):
        if self.more(other_card):
            return False
        else:
            return True

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self.cards = list()
        for s in suits:
            for v in values:
                # card = Card(v,s)
                self.cards.append(Card(v, s))

    def show(self):
        deck_str = f'deck[{len(self.cards)}]:'
        for c in self.cards:
            deck_str += c.to_str()+','
        return deck_str[0:-1]

    def draw(self, x):
        # deck_hand = self.cards[0:x]
        # self.cards = self.cards[x:]
        # мой вариант:
        deck_hand = list()
        for _ in range(x):
            deck_hand.append(self.cards.pop(0))
        return deck_hand

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())
#
# # Возьмем 5 карт "в руку"
hand = deck.draw(5)
# # Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# # Выводим список карт "в руке"(список hand)
for c in hand:
    print(c.to_str(), end=',')






# # Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")   # "Diamonds"
card3 = Card("6", "Clubs")
card4 = Card("Q", "Spades")
print()
print(card1.more(card2))
print(card1.less(card2))

#
# # Выведем карты на экран в виде: 10♥ и A♦
# print(card1.to_str())
# print(card2.to_str())
# print(card3.to_str())
# print(card4.to_str())
#
# # Проверим, одинаковые ли масти у карт
# if card1.equal_suit(card2):
#     print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
# else:
#     print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
