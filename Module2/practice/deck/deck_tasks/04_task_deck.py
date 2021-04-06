import random


class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    SPADES = 'Spades'
    CLUBS = 'Clubs'
    SUITS = {
        HEARTS: '♥',
        DIAMONDS: '♦',
        SPADES: '♣',
        CLUBS: '♠',
    }
    SUITS_POWER = {
        'Hearts': 3,
        'Diamonds': 2,
        'Spades': 1,
        'Clubs': 0
    }
    VALUES = {
        '2': 0,
        '3': 1,
        '4': 2,
        '5': 3,
        '6': 4,
        '7': 5,
        '8': 6,
        '9': 7,
        '10': 8,
        'J': 9,
        'Q': 10,
        'K': 11,
        'A': 12,
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return self.to_str()

    def __str__(self):
        return self.to_str()

    def to_str(self):
        return f'{self.SUITS[self.suit]}{self.value}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        if self.VALUES[self.value] == other_card.VALUES[other_card.value]:
            return self.SUITS_POWER[self.suit] > other_card.SUITS_POWER[other_card.suit]
        else:
            return self.VALUES[self.value] > other_card.VALUES[other_card.value]

    def less(self, other_card):
        return not self.more(other_card)



class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        for suit in Card.SUITS:
            for value in Card.VALUES:
                self.cards.append(Card(suit=suit, value=value))

    def show(self):
        return f'deck[{len(self.cards)}]:{self.cards}'

    def draw(self, count):
        cards_in_hand = self.cards[:count]
        self.cards = self.cards[count:]
        return cards_in_hand

    def shuffle(self):
        self.cards = random.sample(self.cards, len(self.cards))


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()
    print(deck.show())
    # Берем две карты из колоды
    card1, card2 = deck.draw(2)

    # Тестируем методы .less() и .more()
    if card1.more(card2):
        print(f"{card1.to_str()} больше {card2.to_str()}")
    if card1.less(card2):
        print(f"{card1.to_str()} меньше {card2.to_str()}")
