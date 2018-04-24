def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

print ("请输入你想得到的斐波那契数列的第n项")
a=int(input('n: '))

print (fib(a))

#递归的效果相当的差劲,根本没有办法计算出来,计算机的开销太大.