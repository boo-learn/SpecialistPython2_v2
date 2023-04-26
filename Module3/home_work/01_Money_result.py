class Money:
    pass
    # TODO: your code here


# TDD - разработка через тестирование
def test_create_and_str():
    money1 = Money(20, 90)
    assert str(money1) == '20руб 90коп'
    money2 = Money(20, 295)
    assert str(money2) == '22руб 95коп'
    money3 = Money(0, 405)
    assert str(money3) == '4руб 5коп'
    money4 = Money(0, 0)
    assert str(money4) == '0руб 0коп'
