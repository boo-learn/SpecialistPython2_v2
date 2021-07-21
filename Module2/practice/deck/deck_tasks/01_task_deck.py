from deck_total import Card, Deck

play_deck = Deck()
play_deck.shuffle()

card1, card2 = play_deck.draw(2)

if card1 > card2:
    print(f"{card1} больше {card2}")
elif card1 < card2:
    print(f"{card1} меньше {card2}")
elif card1 == card2:
    print(f"{card1} равна {card2}")

# Создайте колоду из 52 карт. Перемешайте ее. Вытяните две карты сверху.
# Сравните эти карты и выведите сообщение формата: “карта A♦ больше J♣”
