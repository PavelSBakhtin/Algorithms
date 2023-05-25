# После успешной сортировки массива на нем можно использовать бинарный поиск.
# Необходимо реализовать алгоритм бинарного поиска по элементам.
# Алгоритм использует подход «разделяй и властвуй», его удобно писать с помощью рекурсии.

import random

def randNums():
    a = []
    l = random.randint(6, 9)
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
                n[j], n[j + 1] = n[j + 1], n[j]
    return n

def binSearch(arr, sPos, ePos, value):
    if sPos > ePos:
        return -1
    else:
        pivot = int((ePos - sPos) / 2 + sPos)
    if arr[pivot] < value:
        return binSearch(arr, pivot + 1, ePos, value)
    elif arr[pivot] > value:
        return binSearch(arr, sPos, pivot - 1, value)
    else:
        return pivot

b = randNums()
v = random.randint(1, 9)
print(b)
a = bubbleSort(b)
print(a)
print("Value is =", v)
print("Position is =", binSearch(a, 0, len(b), v))
