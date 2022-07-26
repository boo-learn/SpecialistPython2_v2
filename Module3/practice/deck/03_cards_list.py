class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
diamond_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)

for value in values:
    hearts_cards.append(value + '\u2665')
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in values:
    diamond_cards.append(value + '\u2666')

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥

print(*hearts_cards, sep=', ')
print(*diamond_cards, sep=', ')
cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    ...]
