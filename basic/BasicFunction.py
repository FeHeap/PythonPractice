# -*- coding = utf-8 -*-
# @Time: 2021/7/9 上午 06:48
# @Software: PyCharm

#Define function
def printinfo():
    print("---------------------")
    print("  人生苦短，我用Python  ")
    print("---------------------")

#Use function
printinfo()

#Function with parameter
def add2NumDisplay(a,b):
    c = a + b
    print(c)

add2NumDisplay(11,22)

#Function with parameter and return
def add2Num(a,b):
    return a + b

print(add2Num(11,22))
result = add2Num(33,44)
print(result)

#Return values
def divid(a,b):
    shang = a // b
    yushu = a % b
    return shang,yushu #separate values with ','

sh,yu = divid(5,2) #use varibles to store return value
print("quotient:%d, remainder:%d"%(sh,yu),end="\n\n")

'''
#classwork

def printOneLine():
    print("-"*30)

def printNumLine(num):
    for i in range(num):
        printOneLine()

def Sum3Num(a,b,c):
    return a + b + c

def average3Num(a,b,c):
    return Sum3Num(a,b,c)/3
'''

# global variables and local variables
def test1():
    a = 300 #local varible
    print("test1-----修改前: a = %d"%a)
    a = 100
    print("test1-----修改後: a = %d"%a)

def test2():
    a = 500
    print("test2----- a = %d"%a)

test1()
test2()


a = 100 #global variable
def test3():
    print(a)

test3()

#if global variable and local varible have same name
a = 100 #global variable
def test4():
    a = 300 #Priority use local varible
    print("test4-----修改前: a = %d"%a)
    a = 200
    print("test4-----修改後: a = %d"%a)

def test5():
    print("test5----- a = %d"%a)
    #if there is no local varible, default use global variable

test4()
test5()

#use global varible in function
a = 100 #global variable
def test6():
    global a
    print("test6-----修改前: a = %d"%a)
    a = 200
    print("test6-----修改後: a = %d"%a)

def test7():
    print("test7----- a = %d"%a)

test6()
test7()