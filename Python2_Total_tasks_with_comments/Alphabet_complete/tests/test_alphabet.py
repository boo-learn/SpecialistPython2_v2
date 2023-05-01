# Запуск тестов:  python -m pytest tests\
from Python2_Total_tasks.Alphabet.result import Alphabet

russian_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н",
                   "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

english_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z"]

swedish_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]


def test_get_letters():
    ru_alphabet = Alphabet("russian", russian_letters)
    assert ru_alphabet.get_letters() == "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    en_alphabet = Alphabet("english", english_letters)
    assert en_alphabet.get_letters() == "abcdefghijklmnopqrstuvwxyz"

    sw_alphabet = Alphabet("swedish", swedish_letters)
    assert sw_alphabet.get_letters() == "abcdefghijklmnopqrstuvwxyzåäö"


def test_letters_num():
    ru_alphabet = Alphabet("russian", russian_letters)
    assert ru_alphabet.letters_num() == 33

    en_alphabet = Alphabet("english", english_letters)
    assert en_alphabet.letters_num() == 26

    sw_alphabet = Alphabet("swedish", swedish_letters)
    assert sw_alphabet.letters_num() == 29


def test_get_letter():
    ru_alphabet = Alphabet("russian", russian_letters)
    assert ru_alphabet.get_letter(1) == "а"
    assert ru_alphabet.get_letter(5) == "д"
    assert ru_alphabet.get_letter(33) == "я"

    en_alphabet = Alphabet("english", english_letters)
    assert en_alphabet.get_letter(1) == "a"
    assert en_alphabet.get_letter(6) == "f"
    assert en_alphabet.get_letter(26) == "z"

    sw_alphabet = Alphabet("swedish", swedish_letters)
    assert sw_alphabet.get_letter(1) == "a"
    assert sw_alphabet.get_letter(8) == "h"
    assert sw_alphabet.get_letter(29) == "ö"
