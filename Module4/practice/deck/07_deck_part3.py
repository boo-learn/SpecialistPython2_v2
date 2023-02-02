import random


class Card:
    def __init__(self, value: str, suit: str):
        self.value = value
        self.suit = suit

    def to_str(self) -> str:
        if self.suit == "Hearts":
            icon = "\u2665"
        elif self.suit == "Diamonds":
            icon = "\u2666"
        elif self.suit == "Clubs":
            icon = "\u2663"
        elif self.suit == "Spades":
            icon = "\u2660"
        return f"{self.value}{icon}"

    def equal_suit(self, other_card: "Card") -> bool:
        return self.suit == other_card.suit

    def more(self, other_card: "Card") -> bool:
        value_volume = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6,
                  '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
        suit_value = {"Hearts":1, "Diamonds":2, "Spades":3, "Clubs":4}
        if value_volume[self.value] == value_volume[other_card.value]:
            return suit_value[self.suit] > suit_value[other_card.suit]
        else:
            return value_volume[self.value] > value_volume[other_card.value]
        

    def less(self, other_card: "Card") -> bool:
        return not self.more(other_card)


class Deck:
    def __init__(self):
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self) -> str:
        list_str_cards = []
        for card in self.cards:
            list_str_cards.append(card.to_str())
        return f"Deck: [{len(self.cards)}] " + ", ".join(list_str_cards)

    def shift(self, num_card: int) -> None:
        self.cards.append(self.cards.pop(num_card-1))

    def draw(self, x) -> list:
        out = self.cards[:x]
        del self.cards[:x]
        return out

    def shuffle(self) -> None:
        random.shuffle(self.cards)

card1 = Card("3", "Clubs")
card2 = Card("3", "Diamonds")

if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
