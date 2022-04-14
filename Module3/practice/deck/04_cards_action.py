class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        dict_1 = {"Hearts": '\u2665', "Diamonds": '\u2666', "Clubs": '\u2663', "Spades": '\u2660'}
        return f"{self.value}{dict_1[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


def sort_key(incominglist):
    return incominglist.suit

cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for i in range (len(values)):
    for suit in suits:
        cards.append(Card(values[i], suit))
print(cards[2].to_str())
# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards

cards.sort(key=sort_key, reverse=False)

print(f"cards:{len(cards)}", end=" ")

for card in cards:
    print(f"{card.to_str()}", end=(', '))
