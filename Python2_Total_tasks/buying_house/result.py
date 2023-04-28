class House:
    def __init__(self, area: int, price_per_sm: float):
        self.__area = area
        self.__price = price_per_sm  # цена за кв.метр

    @property
    def area(self):
        return self.__area

    def final_price(self) -> float:
        """
        Возвращает полную цену дома
        """
        return self.__area * self.__price


class Human:
    def __init__(self, name, start_money=0):
        self.name = name
        self.__money = start_money
        self.__house = None  # Изначально у человека нет дома

    @property
    def money(self):
        return self.__money

    def have_house(self) -> bool:
        """
        :return: True - если есть дом, False - если нет
        """
        if self.__house:
            return True
        return False

    def info(self) -> str:
        """
        возвращает строку формата: "<имя> | на счету: <сумма> | дом: <есть/нет>"
        """
        if self.__house:
            have_house = 'есть'
        else:
            have_house = 'нет'
        return f"{self.name} | на счету: {self.__money} | дом: {have_house}"

    def earn_money(self, income: int) -> None:
        """
        Увеличивает текущее кол-во денег на income
        """
        self.__money += income

    def buy_house(self, house: House) -> bool:
        """
        Покупка дома
        Если денег для покупки достаточно:
            в self.__house сохраняем объект покупаемого дома
            тратим деньги на покупку
            возвращаем True
        Если денег недостаточно:
            возвращаем False
        Примечание: Что происходит со старым домом при покупке нового? Он просто исчезает(магия).
        """
        if self.__money >= house.final_price():
            self.__house = house
            self.__money -= house.final_price()
            return True
        else:
            return False
