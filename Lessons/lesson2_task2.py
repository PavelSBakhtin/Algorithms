# Написать алгоритм быстрой сортировки (quicksort).

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

def quickSort(arr, sPos, ePos):
    leftPos = sPos
    rightPos = ePos
    insex = int((sPos + ePos) / 2)
    pivot = arr[insex]
    while True:
        while arr[leftPos] < pivot:
            leftPos += 1
        while arr[rightPos] > pivot:
            rightPos -= 1
        if leftPos <= rightPos:
            if leftPos < rightPos:
                arr[leftPos], arr[rightPos] = arr[rightPos], arr[leftPos]
            leftPos += 1
            rightPos -= 1
        if leftPos > rightPos:
            break
    if leftPos < ePos:
        quickSort(arr, leftPos, ePos)
    if sPos < rightPos:
        quickSort(arr, sPos, rightPos)
    return arr

b = randNums()
print(b)
print(quickSort(b, 0, len(b) - 1))
