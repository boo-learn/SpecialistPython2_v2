class Money:
    def __init__(self, rubles, kopecks):
        self.rubles = rubles
        if kopecks >= 100:
            self.rubles += kopecks // 100
        self.kopecks = kopecks % 100

    def __repr__(self):
        return f"{self.rubles}руб {self.kopecks}коп"

    def __add__(self, other):
        return Money(self.rubles + other.rubles, self.kopecks + other.kopecks)

    def __sub__(self, other):
        return Money(self.rubles - other.rubles, self.kopecks - other.kopecks)

    def __mul__(self, factor):
        return Money(self.rubles * factor, self.kopecks * factor)

    def __eq__(self, other):
        return self.rubles == other.rubles and self.kopecks == other.kopecks

    def __gt__(self, other):
        if self.rubles == other.rubles:
            return self.kopecks > other.kopecks
        return self.rubles > other.rubles

    def __lt__(self, other):
        if self.rubles == other.rubles:
            return self.kopecks < other.kopecks
        return self.rubles < other.rubles

    def __ne__(self, other):
        if self.rubles == other.rubles:
            return self.kopecks != other.kopecks
        return self.rubles != other.rubles



money = Money(20, 120)
money1 = Money(10, 95)
money2 = Money(20, 121)

print(money)
print(money2)
print(money - money2)
print(money1*5)

print(money == money2)
print(money > money2)
print(money != money2)
