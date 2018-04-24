i = int(input("净利润："))
I = [1000000,600000,400000,200000,100000,0]
r = [0.01,0.015,0.03,0.05,0.075,0.1]
for j in range(len(I))：
    if i > I[j]:
    b = [0,0,0,0,0,0]
    b[j] = i - I[j]
    for k in range(j+1,len(I)):
        b[k] = I[k-1]
    bonus = sum(map(lambda (i1,i2):i1*i2,zip(b,r)))
    break
print('奖金：　',bonus)