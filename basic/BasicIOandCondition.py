# -*- coding = utf-8 -*-
# @Time: 2021/7/7 下午 10:56
# @Software: PyCharm

print("std output String")

a = 10

print("this is a varible: ",a)
print()

'''
About keyword:
>>> import keyword
>>> keyword.kwlist
'''

#Formatted output
age = 18
print("My name is %s, I am a  %s"%("Fe","Taiwaner"))
print("I am %d years old"%age)
print("aaa","bbb","ccc")
print("www","baidu","com",sep=".")
print("hello",end="")
print("world",end="\t")
print("python",end="\n")
print("end")
print()

'''
password = input("Please input password:")
print("The password which you inputted is:",password)
print("The type of input is ",type(password)) #<class 'str'>
'''

a = int("123") #transform <int> into <str>
print(type(a)) #<class 'int'>
b = a + 100
print(b)
print()

#conditional expressions
'''
False: 0, None
True: others

if condition1:
    Execute statement 1
elif condition2:
    Execute statement 2
else:
    Execute statement 3
'''
if False:
    print("True")
else:
    print("False")
if 101:
    print("True")
else:
    print("False")
print("end")
print()


score = 87
if score >= 90 and score <= 100:
    print("Get A in this test")
elif score >= 80 and score < 90:
    print("Get B in this test")
elif score >= 70 and score < 80:
    print("Get C in this test")
elif score >= 60 and score < 70:
    print("Get D in this test")
else:
    print("Get E in this test")
print()

xingBie = 1 # 1 represent man, 0 represent woman
danShen = 1 # 1 represent single, 0 represent unavailable
if xingBie == 1:
    print("man")
    if danShen == 1:
        print("我給你介紹一個吧？")
    else:
        print("你給我介紹一個吧？")
else:
    print("Women")
    print("...")
print()

import random  #import random library
x = random.randint(0,2) #random return integer 0~2
print("randonm:",x)
print()