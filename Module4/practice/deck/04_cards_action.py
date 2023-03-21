for suit in suits:
    for value in values:
        card = Card(value, suit)
        cards.append(card)




cards_str = []
for card in cards:
    cards_str.append(card.to_str())

result = ",".join(cards_str)
print(result)
