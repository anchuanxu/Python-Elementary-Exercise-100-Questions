#python中的列表可以嵌套，这样外层列表就跟数组一样，内层的是对象；不过python的列表数据类型不一定一样，更加的灵活了，

Bonus = 0;
BonusRateList = [[100,0.010],[60,0.015],[40,0.030],[20,0.050],[10,0.075],[0,0.100]];

Profit = int (input('净利润：　'));
Profit /= 10000;

for i in range(0,len(BonusRateList)):
    if (Profit > BonusRateList[i][0]):
        Bonus += ((Profit - BonusRateList[i][0]) * BonusRateList[i][1]);
        Profit = BonusRateList[i][0];

print (Bonus * 10000);