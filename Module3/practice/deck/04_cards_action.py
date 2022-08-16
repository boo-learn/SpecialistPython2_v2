# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
    def __repr__(self): 
        return self.to_str()
    def to_str(self):
        symbols = {
            "Hearts":   "\u2665",
            "Diamonds": "\u2666",
            "Spades":   "\u2663",
            "Clubs":    "\u2660"
        }
        return f"{self.value}{symbols[self.suit]}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        return self.suit==other_card.suit

cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
cards_str=[]
for val in values:
    for suit in suits:
        card=Card(val,suit)
        cards.append(card)
        cards_str.append(card.to_str())


# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
#  кол-во берем от размера списка cards
# 1 вариант
print("Карт всего ",len(cards),", ",str(cards).replace("[","").replace("]",""))

# 2 вариант
print("Карт всего ",len(cards),", ",str(", ".join(cards_str)))
