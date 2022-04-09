class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        if self.suit == "Diamonds":
            print('\u2662')
        elif self.suit == "Hearts":
            print('\u2664')
        elif self.suit == "Spades":
            print('\u2667')
        elif self.suit == "Clubs":
            print('\u2661')
        return f'{self.value} {self.suit}'
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        ...

    def equal_suit(self, other_card):
        return self.suit == other_card.suit
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        ...


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
