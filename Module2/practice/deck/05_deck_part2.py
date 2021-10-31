class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __repr__(self):
        icon_suits = {'Hearts': '\u2661', 'Diamonds': '\u2662', 'Clubs': '\u2667', 'Spades': '\u2664'}
        return f'{self.value}{icon_suits[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы



    def more(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        values_card = dict(zip(values, list(range(13))))
        return values_card[(self.value)] > values_card[(other_card.value)]


    def less(self, other_card):
        suit_card = {'Hearts':1, 'Diamonds':2, 'Clubs':3, 'Spades':4}
        return suit_card[(self.value)] < suit_card[(other_card.value)]


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)



    def __repr__(self):
        cards_str = f'deck[{len(self.cards)}]: '
        cards_str += ', '.join(str(card) for card in self.cards)
        return cards_str

    def draw(self, x):
        draw = []
        for _ in range(x):
            card = self.cards.pop(0)
            draw.append(card)
        return draw


    def shuffle(self):
        import random
        random.shuffle(self.cards)
        return self.cards



deck = Deck()
deck.shuffle()
print(deck)
# Берем две карты из колоды
card1, card2 = deck.draw(2)


# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1} больше {card2}")
if card1.less(card2):
    print(f"{card1} меньше {card2}")
