# -*- coding = utf-8 -*-
# @Time: 2021/7/8 上午 12:40
# @Software: PyCharm

for i in range(5):
    print(i)
print()
'''
output:
0
1
2
3
4
'''

for i in range(0,10,3): #start form 0, end in 10(excluding 10), step = 3
    print(i)
print()
'''
output:
0
3
6
9
'''

for i in range(-10,-100,-30):
    print(i)
print()
'''
output:
-10
-40
-70
'''
name = "taiwan"
for x in name:
    print(x,end="\t")
print("\n")
'''
output:
t	a	i	w	a	n	
'''

a = ["aa","bb","cc","dd"]
for i in range(len(a)):
    print(i,a[i])
'''
output:
0 aa
1 bb
2 cc
3 dd
'''

i = 0
while i < 5:
    print("The %d cycle in while"%(i+1))
    print("i = %d"%i)
    i += 1
print()

#sum of 1~100
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("The sum of 1~%d: %d"%(n,sum),end="\n\n")

#while:...else:...
count = 0
while count < 5:
    print(count,"less than 5")
    count += 1
else:
    print(count,"not less then 5",end="\n\n")

'''
break #break out of loop
continue #skip this cycle of loop
pass #do nothing
'''

i = 0
while i < 10:
    i = i+1
    print("-"*30)
    if(i == 5):
        break
    print(i)
