import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    # Выводит значение в юникод формате
    def to_str(self):
        icons = {'Hearts': '\u2665',
                'Diamonds': '\u2666',
                'Clubs': '\u2663',
                'Spades': '\u2660'}
        return f'{self.value}{icons[self.suit]}'

    def equal_suit(self, other_card):
        return other_card.suit == self.suit


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        list_of_cards_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        list_of_suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(values, suit=suits) for suits in list_of_suits for values in list_of_cards_values]

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        deck_string = ', '.join(map(lambda card: card.to_str(), self.cards))
        return f'deck[{len(self.cards)}] {deck_string}'

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        cards_slice = []
        for card in self.cards[:x]:
            cards_slice.append(card.to_str())
        del self.cards[:x]
        return cards_slice


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
print(hand)
# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
print(deck.show())
# Выводим список карт "в руке"(список hand)
# print(...)
