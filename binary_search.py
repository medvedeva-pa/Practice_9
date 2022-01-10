import time
from random import randint


def binary_search(item, lst):
    start = time.time()
    list = [randint(0,1000) for i in range(lst)]
    list = sorted(list)

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        number = list[mid]
        if number == item:
            return print(f'{item} is found!', time.time() - start)
        if number > item:
            high = mid - 1
        else:
            low = mid + 1
    return print('no such number in list', time.time() - start)


binary_search(9, 1)         # time - 0.0 seconds
binary_search(9, 100)       # time - 0.0009555816650390625
binary_search(100, 1000)    # time - 0.0010411739349365234 seconds
binary_search(10, 1000000)  # time - 0.6922156810760498 seconds