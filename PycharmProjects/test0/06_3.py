def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return  fibs

print("请输入你想得到的斐波那契前N项")
a = int(input('n:'))

print(fib(a))