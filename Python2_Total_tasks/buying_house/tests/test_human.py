# Запуск тестов:  python -m pytest tests\
from Python2_Total_tasks.buying_house.result import House, Human


def test_info():
    human1 = Human("Алексей")
    assert "0" in human1.info()
    assert "Алексей" in human1.info()
    assert "нет" in human1.info()
    human2 = Human("Петр", start_money=10000)
    assert "10000" in human2.info()
    assert "Петр" in human2.info()
    assert "нет" in human2.info()


def test_earn_money():
    human1 = Human("Алексей")
    human1.earn_money(20000)
    assert human1.money == 20000
    human1.earn_money(20000)
    assert human1.money == 40000
    human2 = Human("Петр", start_money=10000)
    assert human2.money == 10000
    human2.earn_money(5500)
    assert human2.money == 15500
    human2.earn_money(500)
    assert human2.money == 16000


def test_have_house():
    house1 = House(20, 1500)
    human1 = Human("Алексей")
    assert not human1.have_house()
    human1._Human__house = house1  # Используем хак, для установки дома без покупки
    assert human1.have_house()


def test_buy_house():
    house1 = House(20, 1500)  # price 30_000
    house2 = House(120, 2500.5)  # price 300_060

    human1 = Human("Алексей", start_money=30_000)

    assert not human1.have_house()
    assert human1.money == 30_000

    human1.buy_house(house1)
    assert human1.have_house()
    assert human1.money == 0

    human2 = Human("Иван", start_money=300_000)
    assert not human2.have_house()
    assert human2.money == 300_000

    assert not human2.buy_house(house2)         # дом немного дороже, чем есть денег
    assert not human2.have_house()              # дом купить не удалось
    assert human2.money == 300_000              # все деньги на месте

    human2.earn_money(100)              # подзаработаем немного денег
    assert human2.buy_house(house2)     # теперь должно хватить
    assert human2.money == 40           # денег нет :-(
    assert human2.have_house()          # зато есть дом!
