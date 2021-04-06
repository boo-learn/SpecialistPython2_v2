# Начнем с создания карты
class Card:
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'
    ICONS = {
        HEARTS: '♥',
        DIAMONDS: '♦',
        CLUBS: '♣',
        SPADES: '♠'
    }
    VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def to_str(self):
        return self.value + Card.ICONS[self.suit]

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for value in Card.VALUES:
            for icon in Card.ICONS:
                self.cards += [Card(value, icon)]


    def show(self):
        return f'deck[{len(self.cards)}]:' + ''.join([card.to_str() for card in self.cards])
