# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

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

def rootSort(num, size, index):
    # Индекс наибольшего элемента - основной
    great = index
    left = (2 * index) + 1
    right = (2 * index) + 2

    # Если левый элемент больше текущего наибольшего - обновляем наибольший элемент
    if left < size and num[left] > num[great]:
        great = left

    # Если правый элемент больше текущего наибольшего - обновляем наибольший элемент
    if right < size and num[right] > num[great]:
        great = right

    # Если наибольший элемент уже не основной - они меняются местами
    if great != index:
        num[index], num[great] = num[great], num[index]
        rootSort(num, size, great)

def pyramidSort(n):
    # Поиск Max из списка
    for i in range(len(n), -1, -1):
        rootSort(n, len(n), i)

    # Max в конец списка
    for i in range(len(n) - 1, 0, -1):
        n[i], n[0] = n[0], n[i]
        rootSort(n, i, 0)

b = randNums()
print(b)
pyramidSort(b)
print(b)
