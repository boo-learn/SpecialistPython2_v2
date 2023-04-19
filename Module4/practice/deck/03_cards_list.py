values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in values:
    hearts_cards.append(value + "\u2661")
diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in values:
    diamonds_cards.append(value + "\u2662")
# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
print(hearts_cards)
