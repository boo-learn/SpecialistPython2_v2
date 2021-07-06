def more(self, other_card):
    while card1 > card2
        return ("more than")


def less(self, other_card):
    while card1 < card2
        return ("less than")


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.value = value
        self.suit = suit
    def to_str(self):
        icons = {
            "Hearts": "\u2665",
            "Clubs": "\u2663",
            "Diamonds": "\u2666",
            "Spades":"\u2660"
        }
        return f"{self.value}{icons[self.suit]}"
    def equal_suit(self, other_card):
        return self.suit == other_card.suit
        # return("same suit")
# class Deck:
#     pass
#     # TODO: сюда копируем реализацию класса колоды из предыдущего задания


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
