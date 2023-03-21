class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-0: скопируйте реализацию метода из предыдущей задачи
        icons = {
            "Hearts": "\u2665",
            "Diamonds": "\u2666",
            "Spades": "\u2660",
            "Clubs": "\u2663"
        }
        return f"{self.value}{icons[self.suit]}"

    def equal_suit(self, other_card) -> bool:
        # TODO-1: метод возвращает True - если масти карт равны или False - если нет
        if self.suit == other_card.suit:
            return True
        else:
            return False
        

values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#hearts_cards = ['2\u2665', '3\u2665', '4\u2665', '5\u2665', '6\u2665', '7\u2665', '8\u2665', '9\u2665', '10\u2665', 'J\u2665', 'Q\u2665', 'K\u2665', 'A\u2665']
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
hearts_cards = [
    Card("2", "Hearts"),
    Card("3", "Hearts"),
    Card("4", "Hearts"),
    Card("5", "Hearts"),
    Card("6", "Hearts"),
    Card("7", "Hearts"),
    Card("8", "Hearts"),
    Card("9", "Hearts"),
    Card("10", "Hearts"),
    Card("J", "Hearts"),
    Card("Q", "Hearts"),
    Card("K", "Hearts"),
    Card("A", "Hearts")
    ]

#diamonds_cards = ['2\u2666', '3\u2666', '4\u2666', '5\u2666', '6\u2666', '7\u2666', '8\u2666', '9\u2666', '10\u2666', 'J\u2666', 'Q\u2666', 'K\u2666', 'A\u2666']
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = [
    Card("2", "Diamonds"),
    Card("3", "Diamonds"),
    Card("4", "Diamonds"),
    Card("5", "Diamonds"),
    Card("6", "Diamonds"),
    Card("7", "Diamonds"),
    Card("8", "Diamonds"),
    Card("9", "Diamonds"),
    Card("10", "Diamonds"),
    Card("J", "Diamonds"),
    Card("Q", "Diamonds"),
    Card("K", "Diamonds"),
    Card("A", "Diamonds")
    ]
# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
all_cards = []
for card in hearts_cards:
    all_cards.append(card.to_str())
print(", ".join(all_cards))

# cards = [
#     Card("2", "Hearts"),
#     Card("3", "Hearts"),
#     Card("4", "Hearts"),
#     ...]
