from deck_total import Card, Deck


# Теперь немного сложнее: создадим имитацию одного хода в “Дурака без козырей”:

# 1. Создайте колоду из 52 карт. Перемешайте ее.
# 2. Первый игрок берет сверху 6 карт
# 3. Второй игрок берет сверху 6 карт.
# 4. Игрок-1 ходит:
#     1. игрок-1 выкладывает самую маленькую карту по значению
#     2. игрок-2 пытается бить карту, если у него есть такая же масть но значением больше.
#     3. Если игрок-2 не может побить карту, то он проигрывает.
#     4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
# 5. Выведите в консоль максимально наглядную визуализацию данного игрового хода.
def fool_first_move():

    def fool_defence(card1, hand2):
        for card in sorted(hand2):
            if card.suit == card1.suit and card.value > card1.value:
                print(f'Второй игрок отбился картой {card}')
                hand2.pop(hand2.index(card))
                return card
        print(f'Второй игрок проиграл')
        exit()

    def fool_attack(card2, card1, hand1):
        for card in hand1:
            if card.value == card2.value or card.value == card1.value:
                print(f'Первый игрок подкинул карту {card}')
                hand1.pop(hand1.index(card))
                return card
        print(f'Первому игроку нечего подкидывать')
        exit()
    deck = Deck()
    deck.shuffle()
    hand1 = deck.draw(6)
    hand2 = deck.draw(6)
    card1 = min(hand1)
    print(f'Первый игрок походил картой {card1}')
    hand1.pop(hand1.index(card1))
    while True:
        if len(hand2) != 0:
            card2 = fool_defence(card1, hand2)
        if len(hand1) != 0:
            card1 = fool_attack(card1, card2, hand1)


fool_first_move()
