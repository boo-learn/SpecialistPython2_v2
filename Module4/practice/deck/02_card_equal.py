# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        return f'{self.value}{self.__suit_mapping[self.suit]}'

    __suit_mapping = {
        'Diamonds': '\u2666',
        'Hearts': '\u2665',
        'Пики': '\u2660',
        'Трефы': '\u2663'
    }

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if self.suit == other_card.suit:
            return True
        else:
            return False


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
