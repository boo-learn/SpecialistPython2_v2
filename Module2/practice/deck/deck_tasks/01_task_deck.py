# Сюда отправляем решение первой задачи с колодой
import random


class Card:
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {
            "Hearts": '\u2665',
            "Diamonds": '\u2666',
            "Clubs": '\u2663',
            "Spades": '\u2660',
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        value_index_self = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other_card.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits.index(self.suit)
            suit_index_other = Deck.suits.index(other_card.suit)
            return suit_index_self > suit_index_other
        return value_index_self > value_index_other

    def less(self, other_card):
        value_index_self = Deck.values.index(self.value)
        value_index_other = Deck.values.index(other_card.value)
        if value_index_self == value_index_other:
            suit_index_self = Deck.suits.index(self.suit)
            suit_index_other = Deck.suits.index(other_card.suit)
            return suit_index_self < suit_index_other
        return value_index_self < value_index_other


class Deck:
    values = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A")
    suits = ("Spades", "Clubs", "Diamonds", "Hearts")

    def __init__(self):
        self.cards = []
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        for suit in Deck.suits:
            for value in Deck.values:
                card = Card(value, suit)
                self.cards.append(card)

    def show(self):
        deck_str = f"deck[{len(self.cards)}]"
        for card in self.cards:
            deck_str += card.to_str() + ","
        return deck_str

    def draw(self, x):
        cards_draw = self.cards[0:x]
        self.cards = self.cards[x:]
        return cards_draw

    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
deck.shuffle()
# print(deck.show())
card1, card2 = deck.draw(2)
#
if card1.more(card2):
    print(f"карта {card1.to_str()} больше карты {card2.to_str()}")
if card1.less(card2):
    print(f"карта {card1.to_str()} меньше карты {card2.to_str()}")
