# Необходимо сравнить скорость работы 2 алгоритмов вычисления чисел Фибоначчи и определить,
# какой из них работает быстрее. Так различия начнутся уже с 40 члена последовательности.

import time

def fbRecurs(n):
    if (n <= 2):
        return 1
    else:
        return fbRecurs(n - 1) + fbRecurs(n - 2)

def fbLine(n):
    if (n <= 2):
        return 1
    else:
        fin = []
        fin.append(1)
        fin.append(1)
        for i in range(2, n):
            j = fin[i - 1] + fin[i - 2]
            fin.append(j)
        return fin[n - 1]

for i in range(10, 46, 5):
    st_l = time.time()
    time.sleep(1)
    fbLine(i)
    end_l = time.time()
    tl = end_l - st_l
    st_r = time.time()
    time.sleep(1)
    fbRecurs(i)
    end_r = time.time()
    tr = end_r - st_r
    print(f"N: {i}; line duration: {tl}; recursive duration: {tr}")

# N: 10; line duration: 1.0000569820404053; recursive duration: 1.0000572204589844
# N: 15; line duration: 1.0000572204589844; recursive duration: 1.0000572204589844
# N: 20; line duration: 1.0000572204589844; recursive duration: 1.0020573139190674
# N: 25; line duration: 1.0000572204589844; recursive duration: 1.0250585079193115
# N: 30; line duration: 1.0000572204589844; recursive duration: 1.2700724601745605
# N: 35; line duration: 1.0000572204589844; recursive duration: 4.092234134674072
# N: 40; line duration: 1.0000572204589844; recursive duration: 36.34407877922058
# N: 45; line duration: 1.0000572204589844; recursive duration: 391.43538880348206
