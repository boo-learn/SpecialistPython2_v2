# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.__suits = {"Hearts": "\u2665", "Diamonds": "\u2666", "Spades": "\u2660", "Clubs": "\u2663"}

    def to_str(self):
        return f"{self.value}{self.__suits.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in suits:
    for value in values:
        cards.append(Card(value, suit))

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
print(f"cards[{len(cards)}] ", end = "")
for card in cards:
    print(card.to_str(), end=",")
#  кол-во берем от размера списка cards

