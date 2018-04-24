# 题目：判断101-200之间有多少个素数，并输出所有素数。
#程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。
def prim(m,n):
    arr=[]
    for x in range(m,n+1):
        for y in range(2,int(x ** 0.5)):
            if(x / y)== int(x / y):
                break
            else:
                arr.append(x)
                break
    return arr
print(prim(101,200))