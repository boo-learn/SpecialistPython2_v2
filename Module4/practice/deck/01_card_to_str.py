# Начнем с создания карты
class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def to_str(self):
        # TODO-1: метод возвращает строковое представление карты в виде: 10♥ и A♦
        icon = ''
        match self.suit:
            case 'Hearts':
                icon = '\u2665'
            case 'Diamonds':
                icon = '\u2666'
            case 'Clubs':
                icon = '\u2663'
            case 'Spades':
                icon = '\u2660'
        return(f'{self.value} {icon}')

# Создадим несколько карт
card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")
card3 = Card("Q", "Spades")
card4 = Card("2", "Clubs")
card5 = Card("J", "Diamonds")

# Выведем карты на экран в виде: 10♥ и A♦
print(card1.to_str())
print(card2.to_str())
print(card3.to_str())
print(card4.to_str())
print(card5.to_str())

# Пример, вывод иконок мастей:
print('\u2661', '\u2665')
print('\u2662', '\u2666')
print('\u2667', '\u2663')
print('\u2664', '\u2660')
