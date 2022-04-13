# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_d = {"Hearts": '\u2665', "Diamonds": '\u2666', "Spades": '\u2663', "Clubs": '\u2660'}
        return (f"{self.value}{suit_d[self.suit]}")

    def equal_suit(self, other_card):
        return True if self.suit == other_card.suit else False

# TODO-1: метод возвращает True - если масти карт равны или False - если нет

suit_d = {"Hearts":'\u2665',"Diamonds":'\u2666',"Spades":'\u2663',"Clubs":'\u2660'}
# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
