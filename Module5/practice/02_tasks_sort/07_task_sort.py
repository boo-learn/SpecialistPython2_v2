# Рекламная акция
# В сети магазинов "Н-Аудио" проводится рекламная акция. Каждый второй товар – бесплатно.
# Естественно, кассирам дано указание пробивать товары в таком порядке, чтобы магазин потерял как можно меньше денег.
# По списку товаров определите максимальную сумму в чеке.
#
# Вход: натуральное число товаров (N < 1000) и далее N натуральных чисел – цены товаров.
# Выход: одно число – максимальная сумма чека.

# Пример
# Вход:
# 5 2 1 10 50 10
# Выход:
# 70
# Пояснение:
# Возможен такой порядок: 10 2 50 1 10

from math import ceil

def bubble_sort(nums, key=lambda x: x, reverse=False):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if reverse:
                expr = key(nums[i]) < key(nums[i + 1])
            else:
                expr = key(nums[i]) > key(nums[i + 1])
            if expr:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    return nums


def get_cart_price(cart):
    """Получает списоц цен на товары в корзине и даёт скидку на самые дешевые товары по акции 1+1"""
    sorted_cart = bubble_sort(cart, reverse=True)
    products_to_pay = ceil(len(sorted_cart) / 2)
    return sum(cart[:products_to_pay])


if __name__ == '__main__':
    cart = [5, 2, 1, 10, 50, 10]
    print(get_cart_price(cart))
    cart = [10, 2, 50, 1, 10]
    print(get_cart_price(cart))
