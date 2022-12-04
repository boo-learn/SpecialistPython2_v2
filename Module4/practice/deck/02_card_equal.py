# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        card_suits = {'Diamonds':'\u2666' ,'Hearts':'\u2665' , 'Spades':'\u2663' , 'Clubs':'\u2660'}
        return f'{self.value}{card_suits[self.suit]}'

    def equal_suit(self, other_card):
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if self.suit == other_card.suit:
            return True
        else:
            return False


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("11", "Hearts")

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card3):
    print(f"У карт: {card1.to_str()} и {card3.to_str()} - одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card3.to_str()} - разные масти")


if card2.equal_suit(card3):
    print(f"У карт: {card2.to_str()} и {card3.to_str()} - одинаковые масти")
else:
    print(f"У карт: {card2.to_str()} и {card3.to_str()} - разные масти")
