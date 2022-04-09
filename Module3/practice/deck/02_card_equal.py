# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        ...
        return f"{self.value}{suits.get(self.suit)}"

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        ...
        return self.suit == other_card.suit

suits = {
"Red diamong": "\u2661",
"Black diamond": "\u2666",
"Red club": "\u2663",
"Black club": "\u2667",
"Red heart": "\u2665",
"Black heart": "\u2661",
"Red spade": "\u2660",
"Black spade": "\u2664"}

# Создадим несколько карт
card1 = Card("10", "Black spade")
card2 = Card("A", "Red heart")
# card1 = Card("6", "Black spade")
# card2 = Card("Q", "Black spade")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
