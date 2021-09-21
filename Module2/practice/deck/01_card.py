class Card:
	def __init__(self, value, suit):
		self.value = value
		self.suit = suit
	
	def to_str(self):
		if self.suit == 'Hearts':
			return f"{self.value}♥"
		elif self.suit == 'Diamonds':
			return f"{self.value}♦"
		elif self.suit == 'Spades':
			return f"{self.value}♠"
		else:
			return f"{self.value}♣"

	def equal_suit(self, other_card):
		if self.suit != other_card.suit:
			return False
		else:
			return True



card1 = Card("10", "Hearts")
card2 = Card("A", "Diamonds")


print(card1.to_str())
print(card2.to_str())


if card1.equal_suit(card2):
	print(f"У карт: {card1.to_str()} и {card2.to_str()} одинаковые масти")
else:
	print(f"У карт: {card1.to_str()} и {card2.to_str()} разные масти")
