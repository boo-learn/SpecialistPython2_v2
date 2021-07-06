import random

class Card:
    suits = {
        "Hearts":   '\u2665',
        "Spades":   '\u2660',
        "Clubs":    '\u2663',
        "Diamonds": '\u2666'
    }

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        pass

    def to_str(self):
        return f"{self.value}{Card.suits[self.suit]}"
        pass

    def equal_suit(self, other_card):
        return  self.suit == other_card.suit


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for suit, _ in Card.suits.items():
            for value in Deck.values:
                self.cards.append(Card(value, suit))


    def show(self):
        deck_str = f"deck[{len(self.cards)}]: "
        for i, card in enumerate(self.cards):
            deck_str += f"{card.to_str()}"
            if i < len(self.cards)-1:
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

# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
# Тусуем колоду
deck.shuffle()
print(deck.show())

# Возьмем 5 карт "в руку"
hand = deck.draw(5)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
print(show_hand(hand))
