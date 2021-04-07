class SuperStr(str):
    """Суперстрока!"""

    def is_repeatance(self, s):
        s = str(s)
        if len(self.__str__()) != 0:
            return self.__str__().replace(s, '') == ''

    def is_palindrome(self):
        reversed_string = self.__str__()[::-1]
        return self.__str__() == reversed_string


if __name__ == '__main__':
    super_str = SuperStr('*****')
    print(super_str)
    print(super_str.is_palindrome())
    print(super_str.is_repeatance('*'))
    super_str = SuperStr('шалаш')
    print(super_str)
    print(super_str.is_palindrome())
    print(super_str.is_repeatance('*'))
    super_str = SuperStr('hello')
    print(super_str)
    print(super_str.is_palindrome())
    print(super_str.is_repeatance('*'))
