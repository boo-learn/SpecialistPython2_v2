from functools import reduce


def summ_array(include_list: list, flag_min:int, flag_max:int):
    return reduce(lambda x,y: x+y, [val for val in include_list if flag_max >val > flag_min])


if __name__ == '__main__':

    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(summ_array(list1, 4, 8))
