# -*- coding = utf-8 -*-
# @Time: 2021/7/9 上午 05:42
# @Software: PyCharm
'''
changing the element in tuple is not allowed
, but a tuple is able to consist of changeable elements.
ex. list
'''
tup1 = () #an empty tuple
print(type(tup1)) #<class 'tuple'>
tup2 = (50)
print(type(tup2)) #<class 'int'>
tup3 = (50,)
print(type(tup3)) #<class 'tuple'>
tup4 = (50,60,70)
print(type(tup4)) #<class 'tuple'>

tup5 = ("abc","def",2000,2020)
print(tup5[0])
print(tup5[-1])
print(tup5[1:5]) #not error
tup6 = ("abc","def",2000,2020,333,444,555,666)
print(tup6[1:5]) #[1，5)

#增 (connect)
tup8 = (12,34,56)
tup9 = ("abc","xyz")
tup = tup8 + tup9
print(tup,end="\n\n")

#刪
tup10 = (12,34,56)
del tup10   #delete the whole tuple varible

#改
tup7 = (12,34,56)
'''
tup7[0] = 100 #error, changing  is not allowed
'''


'''
key in dict is unique, and is unchangeable
'''
#declaration of dict
info = {"name":"Fe", "age":20}
#visit dict
print(info["name"])
print(info["age"])
#visit a nonexistent key
'''
print(info["gender"]) #error
'''
print(info.get("gender")) #Using method get, visit a nonexistent key, default return: None

print(info.get("gender","m")) #set default value is allowed

#增
info = {"name":"Fe", "age":20}
newID = input("please input new student number: ")
info["id"] = newID
print(info["id"])

#刪
#【del】
info = {"name":"Fe", "age":20}
print("Before deleting: %s"%info["name"])
del info["name"]
'''
#error, visit the key which has been deleted is not allowed
print("After deleting: %s"%info["name"])
'''
info = {"name":"Fe", "age":20}
print("Before deleting: %s"%info)
del info
'''
#error, visit the dict which has been deleted is not allowed
print("After deleting: %s"%info)
'''
#【clear】
info = {"name":"Fe", "age":20}
print("Before cleaning: %s"%info)
info.clear()
print("After cleaning: %s"%info)

#改
info = {"name":"Fe", "age":20}
info["age"] = 18
print(info["age"])

#查
info = {"id":1,"name":"Fe", "age":20}
print(info.keys()) #get all the keys(list)

print(info.values()) #get all the values(list)

print(info.items()) #get all the items(tuple list)

#visit all the keys
for key in info.keys():
    print(key)

#visit all the values
for value in info.values():
    print(value)

#visit all the items
for key,value in info.items():
    print("key = %s, value = %s"%(key,value))
'''
output:
key = id, value = 1
key = name, value = Fe
key = age, value = 20
'''

# using enumerate function get index and value in list at the same time
myList = ["a","b","c","d"]
for i,x in enumerate(myList):
    print(i,x)

'''
transform list into dict
dict([(key1,val1),(key2,val2),...,(keyn,valn)])
ex.
dict([("name","Fe"),("age",20)])
'''