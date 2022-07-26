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
hearts_cards = []
hearts_cards2 = ''
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
my_suit = 'Hearts'
for value in values:
    hearts_cards.append(Card(value,my_suit))
    hearts_cards2 += f'{Card(value,my_suit).to_str()}, '
hearts_cards2 = hearts_cards2[:-2]
diamonds_cards = []
diamonds_cards2 = ''
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
my_suit = 'Diamonds'
for value in values[::-1]:
    diamonds_cards.append(Card(value,my_suit))
    diamonds_cards2 += f'{Card(value,my_suit).to_str()}, '
diamonds_cards2 = diamonds_cards2[:-2]
# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(hearts_cards2)
print(diamonds_cards2)
