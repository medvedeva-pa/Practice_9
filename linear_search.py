import time
from random import randint


def linear_search(item, lst):
    start = time.time()

    list = [randint(0,1000) for i in range(lst)]
    if item in list:
       print(f'{item} is found!')
    else:
        print('no such number in list')
    print(time.time() - start)


linear_search(9, 1)         #time - 0.0006844997406005859 seconds
linear_search(9, 100)       #time - 0.0 seconds
linear_search(99, 1000)     #time - 0.0010008811950683594 seconds
linear_search(99, 1000000)  #time - 0.5784823894500732 seconds