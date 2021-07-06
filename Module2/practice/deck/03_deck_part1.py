import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        icons = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2660', "Clubs": '\u2663'}
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        else:
            return False


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        suits = ("Hearts", "Diamonds", "Spades", "Clubs")
        values = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def show(self):
        s = f'deck[{len(self.cards)}]: '
        for card in self.cards:
            s += card.to_str() + ', '
        return s[:-2]

    def draw(self, per_hand: int) -> []:
        hand = []
        for i in range(per_hand):
            hand.append(self.cards[0])
            self.cards.pop(0)
        return hand

    def shuffle(self):
        return random.shuffle(self.cards)


class Hand:
    def __init__(self):
        pass


# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())
#
# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
for card in hand:
    print(card.to_str())
