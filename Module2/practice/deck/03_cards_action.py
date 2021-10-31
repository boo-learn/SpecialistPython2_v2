class Card:
    pass
    # TODO: сюда копируем реализацию класса карты из предыдущего задания


cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ....
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        icon_suits = {'Hearts': '\u2661', 'Diamonds': '\u2662', 'Clubs': '\u2667', 'Spades': '\u2664'}
        return f'{self.value}{icon_suits[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
for value in values:
    card = Card(value, 'Hearts')
    hearts_cards.append(card)

diamonds_cards = []
for value in values:
    card = Card(value, 'Diamonds')
    diamonds_cards.append(card)

clubs_cards = []
for value in values:
    card = Card(value, 'Clubs')
    clubs_cards.append(card)

spades_cards = []
for value in values:
    card = Card(value, 'Spades')
    spades_cards.append(card)

old_cards=spades_cards+clubs_cards+hearts_cards+diamonds_cards

cards_str = ''
for card in old_cards:
    cards_str += card.to_str()

print(*cards_str,sep=',')
