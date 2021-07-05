import random

class Card:
    suits = {
        "Hearts" :  '\u2665',
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
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for key, value in Card.suits.items():
            for i in range(2, 11):
                self.cards.append(Card(i, key))
            self.cards.append(Card("J", key))
            self.cards.append(Card("Q", key))
            self.cards.append(Card("K", key))
            self.cards.append(Card("A", key))


    def show(self):
        print(f"deck[{len(self.cards)}]:", end=" ")
        for card in self.cards:
            print(f"{card.to_str()}", end = " ")
        print()

    def draw(self, x):
        cards_draw = []
        cards_left = []
        for i, card in enumerate(self.cards):
            if i < x:
                cards_draw.append(card)
            else:
                cards_left.append(card)
        self.cards = cards_left
        return cards_draw

    def shuffle(self):
        random.shuffle(self.cards)
        pass


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
for c in hand: print(c.to_str(), end=" ")
print()
