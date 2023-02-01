import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icons = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Clubs": "\u2663",
            "Spades": "\u2660"
        }
        return f"{self.value}{suit_icons[self.suit]}"

    def equal_suit(self, other_card):

        if self.suit == other_card.suit:
            return True
        return False


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for value in values:
            for suit in suits:
                self.cards.append(Card(value, suit))

    def show(self):
        final_str = f'deck[{len(self.cards)}]'
        str_cards = []
        for card in self.cards:
            str_cards.append(card.to_str())
        return final_str + ", ".join(str_cards)

    def draw(self, x):
        hand, self.cards = self.cards[:x], self.cards[x:]
        return hand

    def shuffle(self):
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании

print(deck.show())
print('─' * 10)
# Тусуем колоду
deck.shuffle()
print(deck.show())
print('─' * 10)
# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
print('─' * 10)
# Выводим список карт "в руке"(список hand)
for hand_item in hand:
    print(hand_item.to_str())
