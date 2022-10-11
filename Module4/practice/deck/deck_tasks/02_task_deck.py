from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?
deck = Deck()
# Тусуем колоду
deck.shuffle()
print(deck.show())
# Берем две карты из колоды
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
cards = deck.draw(10)
sum_Hearts = 0
sum_Diamonds = 0
sum_Spades = 0
sum_Clubs = 0
for card in cards:
    if card.suit == 'Hearts':
        sum_Hearts += 1
    if card.suit == 'Diamonds':
        sum_Diamonds += 1
    if card.suit == 'Spades':
        sum_Spades += 1
    if card.suit == 'Clubs':
        sum_Clubs += 1
#print(sum_Hearts, sum_Diamonds, sum_Spades, sum_Clubs)
#print(max(sum_Hearts, sum_Diamonds, sum_Spades, sum_Clubs))
if sum_Hearts == max(sum_Hearts, sum_Diamonds, sum_Spades, sum_Clubs):
    print(f"Hearts")
if sum_Diamonds == max(sum_Hearts, sum_Diamonds, sum_Spades, sum_Clubs):
    print(f"Diamonds")
if sum_Spades == max(sum_Hearts, sum_Diamonds, sum_Spades, sum_Clubs):
    print(f"Spades")
if sum_Clubs == max(sum_Hearts, sum_Diamonds, sum_Spades, sum_Clubs):
    print(f"Clubs")
    
