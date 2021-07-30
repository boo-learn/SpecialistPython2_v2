import random

class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __repr__(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Clubs": '\u2663',
            "Spades": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def __lt__(self, other_card):  # <
        value_index_self = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other_card.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits.index(self.suit)
            suit_index_other = Deck.suits.index(other_card.suit)
            return suit_index_self < suit_index_other
        return value_index_self < value_index_other

    def __gt__(self, other_card):  # >
        value_index_self = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other_card.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits.index(self.suit)
            suit_index_other = Deck.suits.index(other_card.suit)
            return suit_index_self > suit_index_other
        return value_index_self > value_index_other


class Deck:
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    suits = ("Spades", "Clubs", "Diamonds", "Hearts")
    weight_card = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11)
    weight_card_A = (2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 1)


    def __init__(self):
        self.index_last_card = -1
        self.cards = []
        for suit in Deck.suits:
            for value in Deck.values:
                card = Card(value, suit)
                self.cards.append(card)

    def __repr__(self):
        deck_str = f"deck[{len(self.cards)}]"
        for card in self.cards:
            deck_str += str(card) + ","
        return deck_str

    def __getitem__(self, index):
        return self.cards[index]

    def draw(self, x):
        cards_draw = self.cards[0:x]
        self.cards = self.cards[x:]
        return cards_draw

    def shuffle(self):
        random.shuffle(self.cards)

    def __iter__(self):
        self.index_last_card = -1
        return self

    def __next__(self):
        self.index_last_card += 1
        if self.index_last_card >= len(self.cards):
            raise StopIteration
        return self.cards[self.index_last_card]

if __name__ == '__main__':

    deck = Deck()
    for card in deck:
        print(card)

