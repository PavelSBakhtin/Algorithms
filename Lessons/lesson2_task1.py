# Необходимо написать один из простых алгоритмов сортировки, имеющий сложность O(n^2).
# Можно выбрать из пузырьковой сортировки, сортировки вставками и сортировки выбором.

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

def bubbleSort(n):
    for i in range(0, len(n) - 1):
        for j in range(0, len(n) - 1 - i):
            if n[j] > n[j + 1]:
                temp = n[j]
                n[j] = n[j + 1]
                n[j + 1] = temp
    return n

def directSort(n):
    for i in range(len(n)):
        mPos = i
        for j in range(i, len(n)):
            if n[j] < n[mPos]:
                n[mPos], n[j] = n[j], n[mPos]
    return n

b = randNums()
print(b)
print(bubbleSort(b))
print(directSort(b))
