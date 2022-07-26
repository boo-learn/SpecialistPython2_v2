# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты
        if suit == "Hearts":
            self.__suit = "\u2665"
        elif suit == "Diamonds":
            self.__suit = "\u2666"
        elif suit == "Spades":
            self.__suit = "\u2660"
        elif suit == "Clubs":
            self.__suit = "\u2663"

    def to_str(self):
        return f"{self.value}{self.__suit}"

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        else: return False

# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
