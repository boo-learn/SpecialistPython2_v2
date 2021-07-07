from functools import reduce


def summ_array(include_list: list):
    include_list.sort(reverse=True)
    return reduce(lambda x, y: x+y, include_list[:10])


if __name__ == '__main__':

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(summ_array(list1))
