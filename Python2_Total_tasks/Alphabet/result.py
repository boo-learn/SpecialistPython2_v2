class Alphabet:
    def __init__(self, lang: str, letters: list):
        self.lang = lang
        self.letters = letters

    def get_letters(self) -> str:
        return "".join(self.letters)

    def letters_num(self) -> int:
        return len(self.letters)

    def get_letter(self, n) -> str:
        try:
            letter = self.letters[n - 1]
            return letter
        except Exception as e:
            raise Exception(e)



russian_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н",
                   "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]

english_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z"]

swedish_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                   "s", "t", "u", "v", "w", "x", "y", "z", "å", "ä", "ö"]
