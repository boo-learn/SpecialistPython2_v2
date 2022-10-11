import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icon = {
            'Diamonds': '\u2666',
            'Hearts': '\u2665',
            'Spades': '\u2664',
            'Clubs': '\u2667'
        }
        return f'{self.value}{suit_icon[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы
    def more(self, other_card):
        is_more = False
        value_grade = {
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                '10': 10,
                'J': 11,
                'Q': 12,
                'K': 13,
                'A': 14
            }
        if value_grade[self.value] > value_grade[other_card.value]:
            is_more = True
        elif self.value == other_card.value:
            suit_grade = {
                'Hearts': 4,
                'Diamonds': 3,
                'Clubs': 2,
                'Spades': 1
            }
            if suit_grade[self.suit] > suit_grade[other_card.suit]:
                is_more = True
        return is_more

    def less(self, other_card):
        return not self.more(other_card)


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        cards_str = []
        for card in self.cards:
            cards_str.append(card.to_str())
        return f'cards[{len(self.cards)}]' + ', '.join(cards_str)

    def draw(self, x):
        hand = self.cards[:x]
        self.cards = self.cards[x:]
        return hand

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
