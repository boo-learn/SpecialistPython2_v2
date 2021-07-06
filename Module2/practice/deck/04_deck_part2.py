import random

class Card:
    suits = {
        "Hearts": '\u2665',
        "Spades": '\u2660',
        "Clubs": '\u2663',
        "Diamonds": '\u2666'
    }
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    suits_order = ["Spades", "Clubs", "Diamonds", "Hearts"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        pass

    def to_str(self):
        return f"{self.value}{Card.suits[self.suit]}"
        pass

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        value_index_self  = Card.values.index(self.value)
        value_index_other = Card.values.index(other_card.value)
        if value_index_self > value_index_other:
            return True
        elif value_index_self < value_index_other:
            return False
        else:  # equal values
            suit_index_self = Card.suits_order.index(self.suit)
            suit_index_other = Card.suits_order.index(other_card.suit)
            if suit_index_self > suit_index_other:
                return True
            elif suit_index_self < suit_index_other:
                return False
            else:
                print("Warning: two same", self.to_str(), "cards!")
                return False

    def less(self, other_card):
        value_index_self = Card.values.index(self.value)
        value_index_other = Card.values.index(other_card.value)
        if value_index_self < value_index_other:
            return True
        elif value_index_self > value_index_other:
            return False
        else:  # equal values
            suit_index_self = Card.suits_order.index(self.suit)
            suit_index_other = Card.suits_order.index(other_card.suit)
            if suit_index_self < suit_index_other:
                return True
            elif suit_index_self > suit_index_other:
                return False
            else:
                print("Warning: two same", self.to_str(), "cards!")
                return False


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for suit, _ in Card.suits.items():
            for value in Card.values:
                self.cards.append(Card(value, suit))

    def show(self):
        deck_str = f"deck[{len(self.cards)}]: "
        for i, card in enumerate(self.cards):
            deck_str += f"{card.to_str()}"
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

def show_hand(hand_list):
    hand_str = f"hand[{len(hand_list)}]: "
    for i, card in enumerate(hand_list):
        hand_str += f"{card.to_str()}"
        if i < len(hand_list) - 1:
            hand_str += ", "
    return hand_str

def compare_two_cards(c1, c2):
    if c1.more(c2):
        print(f"{c1.to_str()} больше {c2.to_str()}")
    elif c1.less(c2):
        print(f"{c1.to_str()} меньше {c2.to_str()}")
    else:
        print(f"{c1.to_str()} равно {c2.to_str()}")

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

# compare_two_cards(Card("2", "Hearts"), Card("K", "Hearts"))
# compare_two_cards(Card("Q", "Hearts"), Card("Q", "Diamonds"))
# compare_two_cards(Card("Q", "Hearts"), Card("Q", "Clubs"))
# compare_two_cards(Card("Q", "Spades"), Card("Q", "Diamonds"))
