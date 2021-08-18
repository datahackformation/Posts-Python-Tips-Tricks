

from numba import njit

def bubble_sort(lst):
    l = len(lst)
    for x in range(l-1):
        for y in range(0, l-x-1):
            if lst[y] > lst[y+1] :
                lst[y], lst[y+1] = lst[y+1], lst[y]    

@njit()
def bubble_sort_numba(lst):
    l = len(lst)
    for x in range(l-1):
        for y in range(0, l-x-1):
            if lst[y] > lst[y+1] :
                lst[y], lst[y+1] = lst[y+1], lst[y]


# TEST
import time
from random import random

lst = [random() for _ in range(10000)]

start_time = time.time()
bubble_sort(lst)
print('Bubble sort simple:', '%s segundos'%(time.time() - start_time))

start_time = time.time()
bubble_sort_numba(lst)
print('Bubble sort Numba:', '%s segundos'%(time.time() - start_time))