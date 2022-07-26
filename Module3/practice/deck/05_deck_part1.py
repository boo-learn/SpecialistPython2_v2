# Начнем с создания карты

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_dict = {
            'Hearts': '\u2665',
            'Diamonds': '\u2666',
            'Spades': '\u2660',
            'Clubs': '\u2663'
        }

    def to_str(self):
        return self.value + self.suit_dict.get(self.suit)

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        # TODO-1: конструктор добавляет в список self.cards все(52) карты
        for card_suit in suits:
            for card_value in values:
                self.cards.append(Card(card_value, card_suit))


    def show(self):
        visual_view = ''
        for card in self.cards:
            visual_view += f'{card.to_str()}, '
        return f'deck[{len(self.cards)}]:{visual_view[:-2]}'

# Создаем колоду
deck = Deck()
# Выводим колоду в формате указанном в основном задании
print(deck.show())
