p = [31,28,31,30,31,30,31,31,30,31,30,31]# 平年
r = [31,29,31,30,31,30,31,31,30,31,30,31]# 闰年

year = int(input('年:\n'))
month = int(input('月:\n'))
day = int(input('日:\n'))

if (year % 100 == 0) or (year % 4 == 0) and (year % 100 != 0):
    d = r
else:
    d = p

days = sum(d[0:month-1])+day
print(" %d年%d月%d日是该年的第%s天."%(year,month,day,days))