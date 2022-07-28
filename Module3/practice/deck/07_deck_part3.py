import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits_list = ["Hearts", "Clubs", "Diamonds", "Spades"]
        suits_list_code = ['\u2661', '\u2667', '\u2662', '\u2664']
        return f'{self.value}{suits_list_code[suits_list.index(self.suit)]}'

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit

    def more(self, other_card):
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
        return values.index(self.value) > values.index(other_card.value) or (
                values.index(self.value) == values.index(other_card.value) and suits.index(self.suit) > suits.index(
            other_card.suit))

    def less(self, other_card):
        return not (self.more(other_card))


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
        return f"Deck [{len(self.cards)} {', '.join(card.to_str() for card in self.cards)}"

    def draw(self, x):
        drawn_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return drawn_cards

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды

card1 = Card ("10", "Diamonds")
card2 = Card ("8", "Hearts")
card3 = Card ("10", "Hearts")
card4 = Card ("Q", "Diamonds")

# Тестируем методы .less() и .more()
if card1.more(card2):
    print(f"{card1.to_str()} больше {card2.to_str()}")
else:
    print(f"{card1.to_str()} меньше {card2.to_str()}")
if card1.less(card3):
    print(f"{card1.to_str()} меньше {card3.to_str()}")
else:
    print(f"{card1.to_str()} больше {card3.to_str()}")
if card1.less(card4):
    print(f"{card1.to_str()} меньше {card4.to_str()}")
else:
    print(f"{card1.to_str()} больше {card4.to_str()}")
