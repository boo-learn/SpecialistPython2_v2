import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        suit_d = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2663', "Clubs": '\u2660'}
        return f"{self.value}{suit_d[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card): # >
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        index_value1 = values.index(self.value)
        index_value2 = values.index(other_card.value)
        if index_value1 > index_value2:
            return True
        elif index_value1 < index_value2:
            return False
        elif index_value1 == index_value2:
            index_suit1 = suits.index(self.suit)
            index_suit2 = suits.index(other_card.suit)
            return index_suit1 > index_suit2

    def __lt__(self, other_card): # <
        return not self > other_card


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        #          0    1    2    3    4
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(value, suit)
                self.cards.append(card)

    def __str__(self):  # Magic-method
        return f"cards[{len(self.cards)}]{', '.join(map(lambda card: str(card), self.cards))}"

    def draw(self, x): # x = 2
        hand = self.cards[:x]
        self.cards = self.cards[x:]
        return hand

    def shuffle(self):
        random.shuffle(self.cards)
