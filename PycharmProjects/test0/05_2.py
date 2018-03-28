x = int(input("x:"))
y = int(input("y:"))
z = int(input("z:"))

a = {"x":x,"y":y,"z":z}
print("从小到大排序后结果:")

for w in sorted(a,key=a.get):
    print(w,a[w])