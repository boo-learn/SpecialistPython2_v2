from deck_total import Card, Deck


# TODO: Создайте две колоды по 52 карты. Перемешайте их вместе - в итоге получится одна колода из 104 карт.
#   Выбросите/вытяните половину карт. Узнайте, какой/каких мастей в колоде осталось больше всего?
def two_shuffle_decks():

    def ratio_deck(deck):
        ratio_deck = {"Hearts": 0, "Diamonds": 0, "Clubs": 0, "Spades": 0}
        for key in ratio_deck.keys():
            for card in deck:
                if card.suit == key:
                    ratio_deck.update({key: ratio_deck.get(key) + 1})
        for key in ratio_deck.keys():
            if ratio_deck.get(key) == max(ratio_deck.values()):
                print(key)

    deck1 = Deck()
    deck2 = Deck()
    deck3 = deck1 + deck2
    deck3.shuffle()
    deck3.draw(len(deck3.cards)//2)
    ratio_deck(deck3)

two_shuffle_decks()
