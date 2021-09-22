from card3 import suits, values, cards
class Card:
    # TODO: сюда копируем реализацию класса карты из предыдущего задания
     def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        symvols = {
            'Spaced': '\u2660',
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Cluds': '\u2663'
        }
        return f"{self.value}{symvols[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
                for suit in suits:
                for value in values:
                all_cards = Card(value, suit)
                cards.append(all_cards)
# Создаем колоду
deck = Deck()
# такой вариант с импортом подходит? Вроде сработал без ошибок.
