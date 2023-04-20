class Money:
    def __init__(self, rubles, kopeks=0):
        self.rubles = rubles
        self.kopeks = kopeks

        # Если количество копеек отрицательное, то переводим его в положительное, уменьшая на рубль
        if self.kopeks < 0:
            self.rubles += self.kopeks // 100 - 1
            self.kopeks = 100 + self.kopeks % 100

        # Если количество копеек больше 100, то переводим лишние копейки в рубли
        if self.kopeks >= 100:
            self.rubles += self.kopeks // 100
            self.kopeks %= 100

    def __str__(self):
        return f"{self.rubles}руб {self.kopeks}коп"

    def __add__(self, other):
        rubles = self.rubles + other.rubles
        kopeks = self.kopeks + other.kopeks
        return Money(rubles, kopeks)

    def __sub__(self, other):
        rubles = self.rubles - other.rubles
        kopeks = self.kopeks - other.kopeks
        return Money(rubles, kopeks)

    def __mul__(self, number):
        rubles = self.rubles * number
        kopeks = self.kopeks * number
        return Money(rubles, kopeks)

    def __mod__(self, percent):

        total_kopeks = self.rubles * 100 + self.kopeks
        percent_sum = round(total_kopeks) * percent // 100
        rubles = percent_sum // 100
        kopeks = percent_sum % 100
        return Money(rubles, kopeks)

    def __eq__(self, other):
        return self.rubles == other.rubles and self.kopeks == other.kopeks

    def __lt__(self, other):
        return self.rubles < other.rubles or (self.rubles == other.rubles and self.kopeks < other.kopeks)

    def __gt__(self, other):
        return self.rubles > other.rubles or (self.rubles == other.rubles and self.kopeks > other.kopeks)


# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1)  # 21руб 20коп

# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 5коп

# Создаем две денежные суммы
money_sum1 = Money(20, 60)

# Находим 21% от суммы
percent_sum = money_sum1 % 21
print(percent_sum)  # 4руб 33коп
