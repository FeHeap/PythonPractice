# -*- coding = utf-8 -*-
# @Time: 2021/7/9 上午 04:03
# @Software: PyCharm

nameList = [] # an empty list

nameList = ["Sam", "Jack", "Fe"]
print(nameList[0])
print(nameList[1])
print(nameList[2])
print()

testList = [1, "test"]  #list is able to consist of multiple type of varible
print(type(testList[0]))
print(type(testList[1]))
print()

nameList = ["Sam", "Jack", "Fe"]

for name in nameList:
    print(name)
print()

print(len(nameList),end='\n\n') # len(list) return the length of list

lenght = len(nameList)
i = 0
while i < lenght:
    print(nameList[i])
    i += 1
print()

#增: 【append】
nameList = ["Sam", "Jack", "Fe"]

print("-----增加前，名單列表的數據-----")
for name in nameList:
    print(name)

nametemp = input("請輸入增加學生的姓名：")
nameList.append(nametemp) #在末尾追加一個元素

print("-----增加後，名單列表的數據-----")
for name in nameList:
    print(name)

#增: 【extend】
a = [1, 2]
b = [3, 4]
a.append(b) #將 b 列表當作一個元素，加入到 a 列表中
print(a)

a.extend(b) #將 b 列表中的每一個元素，逐一追加到 a 列表中
print(a)

#增: 【insert】
a = [0,1,2]
a.insert(1,3) #第一個變量表示下標，第二的表示元素(對象)
print(a) #指定下標位置插入元素
print()

#刪 【del】 【pop】 【remove】
movieName = ["加勒比海盜", "駭客樂園", "第一滴血", "指環王", "指環王", "速度與激情"]

print("-----刪除前，電影列表的數據-----")
for name in movieName:
    print(name)

del movieName[2] #指定位置刪除一個元素
movieName.pop() #彈出末尾最後一個元素
movieName.remove("指環王") #直接刪除指定內容的元素(若有多個相同內容的元素，刪除找到的第一個)

print("-----刪除後，電影列表的數據-----")
for name in movieName:
    print(name)
print()

#改
nameList = ["Sam", "Jack", "Fe"]

print("-----修改前，名單列表的數據-----")
for name in nameList:
    print(name)

nameList[1] = "Luder" #修改指定下標的元素內容

print("-----修改後，名單列表的數據-----")
for name in nameList:
    print(name)
print()

#查 【in，not in】
nameList = ["Sam", "Jack", "Fe"]

findName = input("請輸入要查找的學生姓名：")
if findName in nameList:
    print("在學員名單中找到相同的名字")
else:
    print("沒有找到")


a = ["a","b","c","a","b"]
print(a.index("a",1,4)) #可以查找指定下標範圍的元素，並返回找到對應數據的下標
'''
print(a.index("a",1,3)) #範圍區間，左閉右開 【1，3)
                        #找不到會報錯
'''

print(a.count("b")) #統計某元素出現幾次
print(a.count("c"))

a = [1,4,2,3]
print(a)
a.reverse() #將列表所有元素反轉
print(a)
a.sort() #升序
print(a)
a.sort(reverse=True) #降序
print(a)

schoolNames = [[],[],[]] #有三個元素的列表，每個元素都是一個空列表
schoolNames = [["北京大學","清華大學"],["南開大學","天津大學","天津師範大學"],["山東大學","中國海洋大學"]]
print(schoolNames[0][0],end="\n\n")

offices = [[],[],[]]
names = ["A","B","C","D","E","F","G","H"]
import random
for name in names:
    offices[random.randint(0,2)].append(name)
print(offices)
for office in offices:
    print("辦公室 %d 的人數為：%d"%(offices.index(office)+1,len(office)))
    for name in office:
        print("%s"%name,end="\t")
    print()
    print("-"*20)

