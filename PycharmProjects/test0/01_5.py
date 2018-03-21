num=[1,2,3,4]
i=0
for a in num:
    for b in num:
        for c in num:
            if(a!=b)and(b!=c)and(c!=a):
                i+=1
                print(a,b,c)
print('总数是:',i)