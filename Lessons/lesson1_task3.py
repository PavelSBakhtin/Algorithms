# 1. Необходимо написать алгоритм поиска всех доступных комбинаций (посчитать количество)
# для количества кубиков K с количеством граней N.
# 2. У вас есть 2 варианта на выбор количество кубиков может быть строго ограничено
# (4 кубика, например), либо их количество будет динамическим. Выбор за вами.
# 3. Если вы реализуете простой вариант, обращаем внимание, что данное решение имеет сложность O(n^4),
# то, если количество кубиков сделать переменной, она трансформируется в O(n^k),
# что будет представлять собой экспоненциальную сложность. Для второго решения очевидно,
# что его сложность O(n^k) с самого начала.

def cubeCount(n):
    res = 0
    for i in range(1, n + 1):
        for j in range(0, n):
            for x in range(0, n):
                for y in range(0, n):
                    i += 1
                    j += 1
                    x += 1
                    y += 1
                    res += 1
    return res

def combiCount(k, n):
    if (k > 0):
        return recursCount(1, k, n)
    else: return 0

def recursCount(d, k, n):
    count = 0
    for i in range(1, n + 1):
        if (d == k):
            count += 1
        else:
            count += recursCount(d + 1, k, n)
        i += 1
    return count

k = int(input("Enter the number of cubes: "))
n = int(input("Enter the number of faces: "))
print('Choose an option:\n1. Four cubes and N faces\n2. K cubes and N faces')
m = int(input('Selection: '))
while True:
    if m == 1:
        print(f"Four cubes and N faces, combinations: {cubeCount(n)}")
    if m == 2:
        print(f"K cubes and N faces, combinations: {combiCount(k, n)}")
        break
    else:
        continue
