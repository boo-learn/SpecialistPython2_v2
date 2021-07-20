class Card:
     def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
values=[2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
hearts_cards = [str(card)+'\u2665' for card in values]

# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = [str(card)+'\u2666' for card in values]

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
line=""
line=",".join(hearts_cards)
print(line)

