# Вам дан английский текст. Закодируйте его с помощью азбуки Морзе:
# https://en.wikipedia.org/wiki/Morse_code#/media/File:International_Morse_Code.svg
# Каждая буква заменяется на последовательность точек и тире.
# В качестве тире используйте обычный дефис: «-», а в качестве точки — точку «.». Например,
# буква «g» превратится в трёхсимвольную строку «—.». Между закодированными буквами нужно ставится ровно один пробел.
# Например, слово «Help» превратится в «…. . .-.. .—.».
# Обратите внимание, что строчные и заглавные буквы кодируются одинаково.


from collections import OrderedDict

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore" \
       " magna aliqua."
d = {
    'a': '-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..',
    'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ',': '.-.-.-', '.': '......', ' ': ' '}
morze_alphabet = OrderedDict(sorted(d.items(), key=lambda t: t[0]))


def morze(text):
    text = text.strip().lower()
    res = ''
    for letter in text:
        res += morze_alphabet[letter]
    res += '..-.-'  # Сигнал конец связи
    return res


if __name__ == '__main__':
    print('Азбука морзе')
    print(text)
    print(morze(text))
