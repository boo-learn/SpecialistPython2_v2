class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self) -> str:
        sign = self.suit.replace("Hearts", '\u2661').replace("Diamonds", '\u2662').replace("Spades", '\u2660').replace("Clubs", '\u2663')
        return f"{self.value} {sign}"

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

for value in values:
    for suit in suits:
        card = Card(value, suit)
        cards.append(card)

str = ''
for card in cards:
    str = str + card.to_str() + ', '
print("cards", len(cards), str[:-2])

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
