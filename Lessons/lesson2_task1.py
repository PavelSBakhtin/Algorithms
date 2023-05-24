# Необходимо написать один из простых алгоритмов сортировки, имеющий сложность O(n^2).
# Можно выбрать из пузырьковой сортировки, сортировки вставками и сортировки выбором.

import random
import time

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
                n[j], n[j + 1] = n[j + 1], n[j]
    return n

def insertSort(n):
    for i in range(len(n) - 1):
        for j in range(i + 1, len(n)):
            if n[j] < n[i]:
                n[i], n[j] = n[j], n[i]
    return n

def choiceSort(n):
    for i in range(len(n) - 1):
        mPos = i
        for j in range(i + 1, len(n)):
            if n[j] < n[mPos]:
                mPos = j
        if (mPos != i):
            n[mPos], n[i] = n[i], n[mPos]
    return n

b = randNums()
print(b)
st_b = time.time()
time.sleep(1)
et_b = time.time()
tb = et_b - st_b
print(f"{bubbleSort(b)} : {tb}")
st_i = time.time()
time.sleep(1)
et_i = time.time()
ti = et_i - st_i
print(f"{insertSort(b)} : {ti}")
st_c = time.time()
time.sleep(1)
et_c = time.time()
tc = et_c - st_c
print(f"{choiceSort(b)} : {tc}")
