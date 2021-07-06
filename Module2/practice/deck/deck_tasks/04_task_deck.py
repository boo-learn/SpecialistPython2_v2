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
    values = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits_order = ["Spades", "Clubs", "Diamonds", "Hearts"]
    
    def __init__(self):
        self.cards = []
        self.points = 0
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
    
    def draw_one(self):
        if len(self.cards) == 0:
            return None
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)
        pass


def main():
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle()
    deck2.shuffle()
    
    for i in range(36):
        c1 = deck1.draw_one()
        c2 = deck2.draw_one()
        print(f"Step {i+1}: {c1} vs {c2} | point goes to ", end="")
        if c1 > c2:
            deck1.points += 1
            print("Deck 1!")
        elif c2 > c1:
            deck2.points += 1
            print("Deck 2!")
        else:
            print("nobody!")
    
    print("Total score:")
    print(f"    Deck 1 - {deck1.points}")
    print(f"    Deck 2 - {deck2.points}")
    
    
if __name__ == "__main__":
    main()
