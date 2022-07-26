class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        suits = {'Diamonds': '\u2666', 'Hearts': '\u2665', 'Spades': '\u2660', 'Clubs': '\u2663'}
        return f"{self.value}{suits[self.suit]}"

    def equal_suit(self, other_card):
        return self.suit == other_card.suit


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = [Card(value,"Hearts") for value in values]
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

diamonds_cards = [Card(value,"Diamonds") for value in values]
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
hearts_cards_list=''
for value in hearts_cards:
    hearts_cards_list = hearts_cards_list + ","+ value.to_str()
# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
print(hearts_cards_list)
