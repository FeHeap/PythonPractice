# -*- coding = utf-8 -*-
# @Time: 2021/7/8 上午 12:55
# @Software: PyCharm

for i in range(1,10,1):
    for j in range(1,i+1,1):
        print("%d*%d=%d"%(i,j,i*j),end=" ")
    print()
print()

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%d" % (i, j, i * j), end=" ")
        j += 1
    print()
    i += 1