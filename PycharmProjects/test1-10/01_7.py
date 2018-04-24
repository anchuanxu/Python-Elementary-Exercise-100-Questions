from itertools import permutations

for i in permutations([1,2,3,4],3):
    k = ''
    for j in range(0,len(i)):
        k = k + str(i[j])
    print(int(k))