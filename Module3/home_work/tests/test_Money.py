import pytest
from Module3.home_work.Money_result import Money


# TDD - разработка через тестирование
def test_create_and_show():
    money1 = Money(12, 35)
    money2 = Money(20, 120)
    money3 = Money(0, 400)
    money4 = Money(1, 405)
    assert str(money1) == "12руб 35коп"
    assert str(money2) == "21руб 20коп"
    assert str(money3) == "4руб 0коп"
    assert str(money4) == "5руб 5коп"


def test_add():
    money1 = Money(12, 35)
    money2 = Money(20, 120)
    money3 = money1 + money2
    assert str(money1) == "12руб 35коп"
    assert str(money2) == "21руб 20коп"
    assert str(money3) == "33руб 55коп"
    assert isinstance(money3, Money)
    money4 = Money(12, 35)
    money5 = Money(20, 90)
    money6 = money4 + money5
    assert str(money4) == "12руб 35коп"
    assert str(money5) == "20руб 90коп"
    assert str(money6) == "33руб 25коп"

    money7 = Money(12, 35)
    money8 = Money(-20, 90)
    money9 = money4 + money5
    assert str(money7) == "12руб 35коп"
    assert str(money8) == "-20руб 90коп"
    assert str(money9) == "33руб 25коп"


def test_sub():
    money1 = Money(22, 35)
    money2 = Money(20, 120)
    money3 = money1 - money2
    assert str(money1) == "22руб 35коп"
    assert str(money2) == "21руб 20коп"
    assert str(money3) == "1руб 15коп"
    assert isinstance(money3, Money)
    money4 = Money(12, 35)
    money5 = Money(20, 90)
    money6 = money4 - money5
    assert str(money4) == "12руб 35коп"
    assert str(money5) == "20руб 90коп"
    assert str(money6) == "-8руб 55коп"
    assert isinstance(money3, Money)
    money7 = Money(20, 90)
    money8 = Money(20, 90)
    money9 = money7 - money8
    assert str(money9) == "0руб 0коп"


# def test_mul():
#     money1 = Money(22, 55)
#     money2 = money1 * 2
#     assert str(money1) == "22руб 55коп"
#     assert str(money2) == "45руб 10коп"
#     assert isinstance(money2, Money)
#     money3 = Money(4, 105)
#     money4 = money3 * 3
#     assert str(money3) == "5руб 5коп"
#     assert str(money4) == "15руб 15коп"
#     assert isinstance(money4, Money)
#
#
# def test_gt():
#     money1 = Money(12, 35)
#     money2 = Money(20, 120)
#     assert money2 > money1
#     money3 = Money(2, 435)
#     money4 = Money(2, 120)
#     assert money3 > money4
#
#
# def test_lt():
#     money1 = Money(12, 35)
#     money2 = Money(20, 120)
#     assert money1 < money2
#     money3 = Money(2, 435)
#     money4 = Money(2, 120)
#     assert money4 < money3
#     assert money4 < money2