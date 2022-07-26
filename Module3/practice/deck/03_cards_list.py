class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        suits = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2667', 'Spades': '\u2664'}
        return f'{self.value}{suits[self.suit]}'


values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
hearts_cards = [Card(value= value, suit='Hearts') for value in values[::1]]

# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
diamonds_cards = [Card(value= value, suit='Diamonds') for value in values[::1]]
# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥

print(', '.join([card.to_str() for card in hearts_cards]))
