from deck_total import Card, Deck

# TODO: Создайте колоду из 52 карт. Перемешайте ее. Вытяните 10 карт сверху
#   и посчитайте карт какой/каких мастей среди вытянутых карт оказалось больше всего?

SUITS = ("Spades", "Clubs", "Diamonds", "Hearts")
TOTAL_CARDS = 10

new_deck = Deck()
new_deck.shuffle()

on_hand = new_deck.draw(TOTAL_CARDS)
suits = [0, 0, 0, 0]

print(f"Выборка из {TOTAL_CARDS} случайных карт:")
for n, c in enumerate(on_hand):
    suits[SUITS.index(on_hand[n].suit)] += 1
    print(on_hand[n], end=" ")

print()
print(f"Распределение мастей в выборке из {TOTAL_CARDS} карт:")
for n, s in enumerate(suits):
    print(f"'{SUITS[n]}': {s}", end=" ")
