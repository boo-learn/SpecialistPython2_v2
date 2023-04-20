import random


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        suit_symbols = {"Hearts": "\u2665", "Diamonds": "\u2666",
                        "Clubs": "\u2663", "Spades": "\u2660"}
        return self.value + suit_symbols[self.suit]

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    # TODO-1: реализуем новые методы
    def more(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        if values.index(other_card.value) < values.index(self.value) or (values.index(other_card.value) == values.index(self.value) and suits.index(other_card.suit) < suits.index(self.suit)):
            return True
        else:
            return False

    def less(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        if values.index(other_card.value) > values.index(self.value) or (values.index(other_card.value) == values.index(self.value) and suits.index(other_card.suit) > suits.index(self.suit)):
            return True
        else:
            return False


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        cards_str = []
        for card in self.cards:
            cards_str.append(card.to_str())
        return f"cards[{len(self.cards)}]: " + ", ".join(cards_str)

    def draw(self, x):
        hand_deck = self.cards[:x]
        self.cards = self.cards[x:]
        return hand_deck

    def shuffle(self):
        random.shuffle(self.cards)


deck: Deck = Deck()
print("Новая колода:")
print(deck.show())

print("Перемешанная колода:")
deck.shuffle()
print(deck.show())
#
# print("Возьмём 5 первых карт:")
# # Возьмем 5 карт "в руку"
# hand: list[Card] = deck.draw(5)
# # Выводим список карт "в руке"(список hand)
# for card in hand:
#     print(card.to_str(), end=", ")
#
# print()
# print("Осталось в колоде:")
# print(deck.show())

# Берем две карты из колоды
card1, card2 = deck.draw(2)

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
if card1.less(card2):
    print(f"{card1.to_str()} меньше {card2.to_str()}")
