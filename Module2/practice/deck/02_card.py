class Card:
    SUIT = ['♥', '♦', '♣', '♠']
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f'{self.value}{self.suit}'


    def equal_suit(self, other_card):
        return self.suit == other_card.suit
    # Выведем карты на экран в виде: 10♥ и A♦
print(card1)
print(card2)

# Проверим, одинаковые ли масти у карт
if card1.equal_suit(card2):
    print(f"У карт: {card1} и {card2} одинаковые масти")
else:
    print(f"У карт: {card1} и {card2} разные масти")
