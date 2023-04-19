# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        if self.suit == "Hearts":
            return f'{self.value}. \u2661 '
        if self.suit == "Diamonds":
            return f'{self.value}. \u2662 '
        if self.suit == "Spades":
            return f'{self.value}. \u2664 '
        if self.suit == "Clubs":
            return f'{self.value}.\u2667 '

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if card1.suit == card2.suit:
            return True


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
