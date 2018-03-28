# 题目:输入三个整数x,y,z,请把这三个数字由小到大输出.
# 程序分析:互换算法

l = []
for i in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print (l)