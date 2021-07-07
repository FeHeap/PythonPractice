# -*- coding = utf-8 -*-
# @Time: 2021/7/8 上午 01:11
# @Software: PyCharm
import time

currentTime = time.time()
sec = currentTime % 60
min = (currentTime//60) % 60
hour = (currentTime//(60*60) + 8) % 24
print("Current Time: %02d:%02d:%02d Taipei"%(hour,min,sec))
