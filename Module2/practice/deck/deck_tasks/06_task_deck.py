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
    
    def __add__(self, other):
        new_deck = Deck()
        new_deck.cards = self.cards + other.cards
        return new_deck


def main():
    deck1 = Deck()
    deck2 = Deck()
    
    deck104 = deck1 + deck2
    deck104.shuffle()
    deck104.draw(52)
    print(deck104)
    
    count_cards = [0 ,0 ,0, 0]
    for card in deck104:
        count_cards[Deck.suits_order.index(card.suit)] += 1
    for i in range(4):
        print(f"{Deck.suits_order[i]}: {count_cards[i]}, ", end="")
    print()
    
    max_suits = max(count_cards)
    all_max_suits_inds = []
    for i, num_suits in enumerate(count_cards):
        if num_suits == max_suits:
            all_max_suits_inds.append(i)
    for i in all_max_suits_inds:
        print(f"Most of drawn cards are '{Deck.suits_order[i]}'.")
    
if __name__ == "__main__":
    main()
