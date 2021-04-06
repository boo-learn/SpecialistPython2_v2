# Начнем с создания карты


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.suits = {
            'Hearts': '♥',
            'Diamonds': '♦',
            'Spades': '♣',
            'Clubs': '♠'
        }
        self.suits_power = {
            'Hearts': 3,
            'Diamonds': 2,
            'Spades': 1,
            'Clubs': 0
        }
        self.values = {
            '2': 0,
            '3': 1,
            '4': 2,
            '5': 3,
            '6': 4,
            '7': 5,
            '8': 6,
            '9': 7,
            '10': 8,
            'J': 9,
            'Q': 10,
            'K': 11,
            'A': 12,
        }

    def __str__(self):
        return self.to_str()

    def to_str(self):
        return f'{self.suits[self.suit]}{self.value}'

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        else:
            return False

    def more(self, other_card):
        if self.values[self.value] == other_card.values[other_card.value]:
            if self.suits_power[self.suit] > other_card.suits_power[other_card.suit]:
                return True
            else:
                return False
        elif self.values[self.value] == other_card.values[other_card.value]:
            return True
        else:
            return False

    def less(self, other_card):
        are_more = self.more(other_card)
        if are_more:
            return False
        else:
            return True


# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
    print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")

if card1.more(card2):
    print(f"Карта {card1.to_str()} больше чем {card2.to_str()}")
else:
    print(f"Карта {card1.to_str()} меньше чем {card2.to_str()}")


if __name__ == '__main__':
    print(Card(2, 'Diamonds'))
