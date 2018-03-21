# use if...elif...else statements to decided

import  sys


x = int(input("净利润: "))

if x<=100000:
    bonus=x*0.1
    print(u"奖金：",bonus,u"元")
elif 100001<x<=200000:
    bonus=10000+(x-100000)*0.075
    print(u"奖金：", bonus, u"元")
elif 200001<x<=400000:
    bonus=10000+7500+(x-200000)*0.05
    print(u"奖金：", bonus, u"元")
elif 400001<x<=600000:
    bonus=10000+7500+10000+(x-400000)*0.03
    print(u"奖金：", bonus, u"元")
elif 600001<x<=1000000:
    bonus=10000+10000+7500+6000+(x-600000)*0.015
    print(u"奖金：", bonus, u"元")
elif 1000000<x<=10000000:
    bonus=0000+10000+7500+6000+6000+(x-1000000)*0.01
    print(u"奖金：", bonus, u"元")