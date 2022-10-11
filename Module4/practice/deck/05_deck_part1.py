# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suit_icon = {
        'Hearts':'\u2665',
        'Diamonds':'\u2666',
        'Clubs':'\u2663',
        'Spades':'\u2660',
        }

        return f"{self.value}{suit_icon[self.suit]}"
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦

def equal_suit(card1:Card, card2:Card):
    if card1.suit==card2.suit:
        return True
    else:
        return False

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
        self.cards = []
        for svit in suits:
            for value in values:
                self.cards.append(Card(value,svit))
        # TODO-1: конструктор добавляет в список self.cards все(52) карты

    def show(self)->str:
        card_str = []
        for card in self.cards:
            card_str.append(card.to_str())
        return f"Количество карт в колоде {len(self.cards)}: {', '.join(card_str)}"


deck1 = Deck()
print(deck1.show())
