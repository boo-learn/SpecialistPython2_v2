# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        self.suit_dict = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2660', "Clubs": '\u2663'}

    def to_str(self):
        return f"{self.value}{self.suit_dict[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

#cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]

# TODO-1: в список cards добавьте ВСЕ карты всех мастей
cards = [Card(val, suit_val) for suit_val in suits for val in values]

# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
print(f"cards[{len(cards)}]", ','.join([card.to_str() for card in cards]))
