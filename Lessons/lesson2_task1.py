# Необходимо написать один из простых алгоритмов сортировки, имеющий сложность O(n^2).
# Можно выбрать из пузырьковой сортировки, сортировки вставками и сортировки выбором.

import random

def bubSort(n):
    for i in range(0, len(n) - 1):
        for j in range(0, len(n) - 1 - i):
            if n[j] > n[j + 1]:
                temp = n[j]
                n[j] = n[j + 1]
                n[j + 1] = temp
    return n

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

b = randNums()
print(b)
print(bubSort(b))
