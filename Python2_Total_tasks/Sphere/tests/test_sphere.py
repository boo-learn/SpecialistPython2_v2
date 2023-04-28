# Запуск тестов:  python -m pytest tests\
from Python2_Total_tasks.Sphere.result import Sphere


def test_get_volume():
    ru_alphabet = Sphere()
    assert ru_alphabet.volume == 4.189

    ru_alphabet = Sphere(1)
    assert ru_alphabet.volume == 4.189

    ru_alphabet = Sphere(r=2)
    assert ru_alphabet.volume == 33.51

    ru_alphabet = Sphere(r=0)
    assert ru_alphabet.volume == 0.0

    ru_alphabet = Sphere(r=-1)
    assert ru_alphabet.volume == -4.189


def test_get_square():
    ru_alphabet = Sphere()
    assert ru_alphabet.square == 12.566

    ru_alphabet = Sphere(1)
    assert ru_alphabet.square == 12.566

    ru_alphabet = Sphere(r=2)
    assert ru_alphabet.square == 50.265

    ru_alphabet = Sphere(r=0)
    assert ru_alphabet.square == 0.0

    ru_alphabet = Sphere(r=-1)
    assert ru_alphabet.square == 12.566


def test_get_radius():
    ru_alphabet = Sphere()
    assert ru_alphabet.get_radius() == 1

    ru_alphabet = Sphere(1)
    assert ru_alphabet.get_radius() == 1

    ru_alphabet = Sphere(-1)
    assert ru_alphabet.get_radius() == -1


def test_get_center():
    ru_alphabet = Sphere()
    assert ru_alphabet.get_center() == (0, 0, 0)

    ru_alphabet = Sphere(1)
    assert ru_alphabet.get_center() == (0, 0, 0)

    ru_alphabet = Sphere(x=0, y=1, z=2)
    assert ru_alphabet.get_center() == (0, 1, 2)

    ru_alphabet = Sphere(1, 2, 3, 4)
    assert ru_alphabet.get_center() == (2, 3, 4)

    ru_alphabet = Sphere(-1, -2, -3, -4)
    assert ru_alphabet.get_center() == (-2, -3, -4)
