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


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cards = []
cards_visual = ''
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in suits:
    for value in values:
        cards.append(Card(value,suit))
        cards_visual += f'{Card(value,suit).to_str()}, '
cards_visual = cards_visual[:-2]

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards

print(f'cards[{len(cards)}]{cards_visual}')

#print(", ".join([card.to_str() for card in hearts_cards]))

