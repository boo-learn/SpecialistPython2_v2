import random


class Card:
    HEARTS   = "Hearts"
    SPADES   = "Spades"
    CLUBS    = "Clubs"
    DIAMONDS = "Diamonds"
    suits = {
        HEARTS:   '\u2665',
        SPADES:   '\u2660',
        CLUBS:    '\u2663',
        DIAMONDS: '\u2666'
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        pass

    def __repr__(self):
        return f"{self.value}{Card.suits[self.suit]}"
        pass

    def __gt__(self, other):
        value_index_self  = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits_order.index(self.suit)
            suit_index_other = Deck.suits_order.index(other.suit)
            if suit_index_self > suit_index_other:
                return True
        if value_index_self > value_index_other:
            return True
        return False

    def __lt__(self, other):
        value_index_self  = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits_order.index(self.suit)
            suit_index_other = Deck.suits_order.index(other.suit)
            if suit_index_self < suit_index_other:
                return True
        if value_index_self < value_index_other:
            return True
        return False
    
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit


class Deck:
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits_order = ["Spades", "Clubs", "Diamonds", "Hearts"]
    
    def __init__(self):
        self.cards = []
        for suit, _ in Card.suits.items():
            for value in Deck.values:
                self.cards.append(Card(value, suit))

    def __repr__(self):
        deck_str = f"deck[{len(self.cards)}]: "
        for i, card in enumerate(self.cards):
            deck_str += f"{card}"
            if i < len(self.cards) - 1:
                deck_str += ", "
        return deck_str

    def draw(self, x):
        cards_draw = self.cards[0:x]
        self.cards = self.cards[x:]
        return cards_draw

    def shuffle(self):
        random.shuffle(self.cards)
        pass


def main():
    deck = Deck()
    deck.shuffle()
    print(deck)
    card_1, = deck.draw(1)
    card_1 = Card("A", Card.HEARTS)
    print(f"Drawn {card_1} as the first one.")
    while True:
        deck.shuffle()
        card_2 = deck.draw(1)
        if len(card_2) == 0:
            break
        card_2 = card_2[0]
        if card_2 > card_1:
            print(f"Drawn {card_2} which is more than {card_1}.")
            break
        else:
            print(f"Drawn {card_2} which is not more than {card_1}.")
    
    
if __name__ == "__main__":
    main()
