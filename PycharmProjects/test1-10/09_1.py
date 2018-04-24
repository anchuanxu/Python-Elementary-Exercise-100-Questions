#题目:暂停一秒输出.
#题目分析:使用time模块的sleep()函数.
#代码如下:
import time
#myJ = {1:'a',2:'b'}
#for key,value in dict.items(myJ):
   # print (key,value)
    #time.sleep(1)#暂停一秒
L=['为','什','么','我','不','说','话','因','为','我','想','静','静']
for i in range(len(L)):
    print(L[i])
    time.sleep(1)