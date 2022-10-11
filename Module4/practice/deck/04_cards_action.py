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


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
hearts_cards = []
diamonds_cards = []
clubs_cards = []
spades_cards = []
deck_card = []

for i in values:
    hearts_cards.append(Card(i,suits[0]))
    diamonds_cards.append(Card(i,suits[1]))
    clubs_cards.append(Card(i,suits[2]))
    spades_cards.append(Card(i,suits[3]))

deck_card.append(hearts_cards)
deck_card.append(diamonds_cards)
deck_card.append(clubs_cards)
deck_card.append(spades_cards)

suits = []
for i in deck_card:
    for j in i:
        suits.append(j.to_str())
    print("Количество карт ", len(i),*suits, sep=', ')
    suits.clear()


