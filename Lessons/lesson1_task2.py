# Написать алгоритм поиска простых чисел (делятся только на себя и на 1) в диапазоне от 1 до N.
# В алгоритме будет использоваться вложенный for, что явно говорит о квадратичной сложности,
# на этом стоит акцентировать внимание.

def findSimples(a):
    b = []
    c = 0
    for i in range(1, a + 1):
        flag = True
        for j in range(2, i):
            c += 1
            if (i % j == 0):
                flag = False
                break
        if (flag):
            b.append(i)
    return b, c

a = int(input("Enter any integer: "))
b, c = findSimples(a)
print(f"Prime numbers from 1 to {a}:\n{b}\nNumber of iterations:\n{c}")
