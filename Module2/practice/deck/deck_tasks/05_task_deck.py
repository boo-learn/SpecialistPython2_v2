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
    
    def __repr__(self):
        deck_str = f"deck[{len(self.cards)}]: "
        for i, card in enumerate(self.cards):
            deck_str += f"{card}"
            if i < len(self.cards) - 1:
                deck_str += ", "
        return deck_str

    def __getitem__(self, index):
        return self.cards[index]
    
    def __iter__(self):
        self.index_last_card = -1
        return self

    def __next__(self):
        self.index_last_card += 1
        if self.index_last_card >= len(self.cards):
            raise StopIteration
        return self.cards[self.index_last_card]


class FoolPlayer:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def draw_least(self):
        return self.hand.pop(self.hand.index(min(self.hand)))
    
    def try_beat(self, unbeaten_card):
        self.hand.sort()
        for card in self.hand:
            if card.suit == unbeaten_card.suit and card > unbeaten_card:
                return self.hand.pop(self.hand.index(card))
        return None
    
    def try_draw_same_value(self, table):
        for my_card in self.hand:
            for card in table:
                if my_card.value == card.value:
                    return self.hand.pop(self.hand.index(my_card))
        return None
    
    def __repr__(self):
        s = f"{self.name} has "
        for card in self.hand:
            s += str(card) + " "
        return s


def main():
    deck = Deck()
    deck.shuffle()
    p1 = FoolPlayer("Player 1", deck.draw(6))
    p2 = FoolPlayer("Player 2", deck.draw(6))
    print(p1)
    print(p2)
    c1 = p1.draw_least()
    print(f"{p1.name} draws {c1} to the table.")
    table = [c1, ]
    while len(p2.hand) > 0:
        c1_beat = p2.try_beat(c1)
        if not c1_beat:
            print(f"{p2.name} can't beat {c1}, he has lost!")
            break
        table.append(c1_beat)
        print(f"{p2.name} has beaten {c1} with {c1_beat}!")
        c1 = p1.try_draw_same_value(table)
        if not c1:
            print(f"{p1.name} has nothing to draw, {p2.name} has beaten off!")
            break
        else:
            print(f"{p1.name} draws {c1} for {c1_beat}!")
    if len(p2.hand) == 0:
        print(f"{p2.name} has beaten off with all his hand!")
    
    
if __name__ == "__main__":
    main()
