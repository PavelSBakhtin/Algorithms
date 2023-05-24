# Написать алгоритм быстрой сортировки (quicksort).

import random

def randNums():
    a = []
    l = random.randint(5, 7)
    for i in range(l):
        k = random.randint(1, 9)
        r = k
        if r in a:
            r += 10
            a.append(r)
        else:
            a.append(k)
        i += 1
    return a


