list = []
a = 1
list.append(a)
b = 1
list.append(b)
for i in range(1,20):
    c = list[i-1]+list[i]
    list.append(c)

print(list)