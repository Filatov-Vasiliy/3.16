def braun(n, m):
    print('Введите матрицу')
    Matrix = [[0] * m for i in range(n)]
    for i in range(n):
        for j in range(m):
            Matrix[i][j] = int(input())
    print('кол-во итераций')
    N = int(input())
    count = 1
    alpha = 0
    betta = 0
    sum1 = 0
    sum2 = 0
    max = 0
    min = 10000000
    a = 1  #
    b = 1  # выбранная стратегия
    v = 0  # цена игры
    p = [float(0)] * m
    q = [float(0)] * n
    max_alpha = [0] * m
    min_betta = [0] * n
    p[0] = 1
    q[0] = 1
    while (count <= N):
        for i in range(m):
            sum1 = 0
            for j in range(n):
                sum1 = sum1 + Matrix[i][j] * q[j]
            max_alpha[i] = sum1
        max = -1000000000
        for i in range(m):
            if max < max_alpha[i]:
                max = max_alpha[i]
                a = i
        alpha = max
        for j in range(n):
            sum2 = 0
            for i in range(m):
                sum2 = sum2 + Matrix[i][j] * p[i]
            min_betta[j] = sum2
        min = 100000000000
        for j in range(n):
            if min > min_betta[j]:
                min = min_betta[j]
                b = j
        betta = min
        v = (alpha + betta) / 2
        for i in range(m):
            if i != a:
                p[i] = float(count * p[i]) / (count + 1)
            else:
                p[i] = (count * p[i] + 1) / (count + 1)
        for j in range(n):
            if j != b:
                q[j] = (count * q[j]) / (count + 1)
            else:
                q[j] = (count * q[j] + 1) / (count + 1)
        print(count)
        print(alpha)
        print(betta)
        print(v)
        print(p)
        print(q)
        count += 1
    print('Ответ:')
    print(p)
    print(q)
    print(v)


n = int(input())
m = int(input())
braun(n, m)
