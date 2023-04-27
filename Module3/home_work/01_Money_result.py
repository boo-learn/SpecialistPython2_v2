import requests

class Money:
    def __init__(self, rubles=0, kopecks=0):
        self.rubles = rubles
        self.kopecks = kopecks
        self._normalize()

    def _normalize(self):
        self.rubles += self.kopecks // 100
        self.kopecks %= 100

    def __add__(self, other):
        return Money(self.rubles + other.rubles, self.kopecks + other.kopecks)

    def __sub__(self, other):
        return Money(self.rubles - other.rubles, self.kopecks - other.kopecks)

    def __mul__(self, n):
        return Money(self.rubles * n, self.kopecks * n)

    def __lt__(self, other):
        return self.rubles < other.rubles or (self.rubles == other.rubles and self.kopecks < other.kopecks)

    def __le__(self, other):
        return self < other or self == other

    def __eq__(self, other):
        return self.rubles == other.rubles and self.kopecks == other.kopecks

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other

    # добавление вычисления % от суммы:
    def percent(self, percentage):
        total_kopecks = (self.rubles * 100 + self.kopecks) * percentage / 100
        return Money(0, int(round(total_kopecks)))

    # Добавление конвертации:
    @staticmethod
    def _get_exchange_rates():
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                'USD': data['Valute']['USD']['Value'],
                'EUR': data['Valute']['EUR']['Value']}

    def convert(self, currency):
        currency = currency.upper()
        exchange_rates = self._get_exchange_rates()

        if currency not in exchange_rates:
            raise currency

        exchange_rate = exchange_rates[currency]
        total_rubles = self.rubles + self.kopecks / 100
        converted_value = total_rubles / exchange_rate

        return round(converted_value, 2)

    #Добавление отправки-в процессе

# Проверка решений
# Сложение/вычитание/умножение/сравнение
m1 = Money(20, 60)
m2 = Money(10, 45)

m3 = m1 + m2
print(f"Сложение: {m3.rubles} р. {m3.kopecks} к.")

m4 = m1 - m2
print(f"Вычитание: {m4.rubles} р. {m4.kopecks} к.")

m5 = m1 * 2
print(f"Умножение: {m5.rubles} р. {m5.kopecks} к.")

print(f"Равно: {m1 == m2}")
print(f"Не равно: {m1 != m2}")
print(f"Меньше: {m1 < m2}")
print(f"Больше: {m1 > m2}")

# Вычисление %
m6 = m1.percent(21)
print(f"Процент: {m6.rubles} р. {m6.kopecks} к.")

# Конвертация в валюту

usd = m1.convert('USD')
print(f"USD: {usd}")

eur = m1.convert('EUR')
print(f"EUR: {eur}")
