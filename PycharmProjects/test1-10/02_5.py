#  使用字典控制利润与提成比例的匹配

import math
import math.sort

num = int(input('净利润：　'))
obj = {100:0.01,60:0.015,40:0.03,20:0.05,10:0.075,0:0.1}
keys = obj.keys()
keys.sort()
keys.reverse()
r = 0
for key in keys:
    if num > key:
        r += (num - key) * obj.get(key)
        num = key
print ("今年的奖金为：　",r,"万元.")
