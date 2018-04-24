for i in range(1,85):
    if 168 % i == 0:
        j = 168 / i
        if i > j:
            m = (i + j)/2
            n = (i - j)/2
            if m * n - 268 == n * n - 100 and(n*n - 100)%1 == 0:
                print('x =', m * m - 268)
# 有一些bug未完成调试,有可能是边界溢出问题.