# Запуск тестов:  python -m pytest tests\
from Python2_Total_tasks.buying_house.result import House


def test_create_house_and_final_price():
    house1 = House(20, 0.5)
    assert house1.area == 20
    assert house1.final_price() == 10
    house2 = House(120, 2.25)
    assert house2.area == 120
    assert house2.final_price() == 270
    house3 = House(1, 3.75)
    assert house3.area == 1
    assert house3.final_price() == 3.75
