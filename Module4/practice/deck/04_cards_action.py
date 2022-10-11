# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == "Hearts":
            card_suit = '\u2665'
        elif self.suit == "Diamonds":
            card_suit = '\u2666'
        elif self.suit == "Clubs":
            card_suit = '\u2663'
        elif self.suit == "Spades":
            card_suit = '\u2660'
        return f'{self.value}{card_suit}'

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if self.suit == other_card.suit:
            return True
        else:
            return False

cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for value in values:
    card = Card(value,'Hearts')
    cards.append(card)
    card = Card(value, 'Diamonds')
    cards.append(card)
    card = Card(value, 'Spades')
    cards.append(card)
    card = Card(value, 'Clubs')
    cards.append(card)
# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
visual_cards = []
for card in cards:
    visual_cards.append(card.to_str())

print(f'cards[{len(visual_cards)}]{",".join(visual_cards)}')


#  кол-во берем от размера списка cards
