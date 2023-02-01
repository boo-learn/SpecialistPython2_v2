# Начнем с создания карты
class Card:
    def __init__(self, value: str, suit: str):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self) -> str:
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        if self.suit == "Hearts":
            icon = "\u2665"
        elif self.suit == "Diamonds":
            icon = "\u2666"
        elif self.suit == "Clubs":
            icon = "\u2663"
        elif self.suit == "Spades":
            icon = "\u2660"
        return f"{self.value}{icon}"

    def equal_suit(self, other_card: "Card") -> bool:
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit == other_card.suit

cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей

for suit in suits:
    for value in values:
        cards.append(Card(value, suit))


# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
print(f"cards: [{len(cards)}]", end=" ")

for card in cards:
    if card != cards[-1]:
        print(f"{card.to_str()}", end=", ")
    else:
        print(f"{card.to_str()}")
