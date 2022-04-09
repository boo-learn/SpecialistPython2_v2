class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits = {
            "Diamonds": "\u2666",
            "Clubs": "\u2663",
            "Hearts": "\u2665",
            "Spades": "\u2660"}
        return f"{self.value}{suits.get(self.suit)}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

for value in values:
    for suit in suits:
        card = Card(value, suit)
        if card not in cards:
            cards.append(card)

# print(len(cards))
# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards

new_cards = []
for card in cards:
    card = card.to_str()
    new_cards.append(card)

print(f"cards{[len(new_cards)]}{new_cards}")
