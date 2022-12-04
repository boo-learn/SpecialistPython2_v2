class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in values:
    value += '\u2665'
    hearts_cards.append(value)
print(hearts_cards)


# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = []
for value in values:
    value += '\u2666'
    diamonds_cards.append(value)
print(diamonds_cards.pop)

##### #не разобрался как убрать заяптые из списка в принте ######

cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
####  и не понял для чего списко cards выше #######
