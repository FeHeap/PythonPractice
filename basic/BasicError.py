# -*- coding = utf-8 -*-
# @Time: 2021/7/9 上午 08:04
# @Software: PyCharm

#Catch Error
try:
    print("-----test--1--")
    f = open("test.txt","r")
    print("-----test--2--")
except IOError: #"can't find the file" belongs to IOError
    pass #the code runs after catch Error

try:
    print(num)
#except IOError:    #Error which we want to catch must be consistent
except NameError:
    print("Find Error",end="\n\n")


try:
    print("-----test--1--")
    f = open("test_re.txt","r")
    print("-----test--2--")
    f.close()
    print(num)
except (NameError,IOError): #put Error may happening into ()
    pass

try:
    print("-----test--1--")
    f = open("test_re.txt","r")
    print("-----test--2--")
    f.close()
    print(num)
except (NameError,IOError) as result: #store error message into result
    print("Find Error")
    print(result,end="\n\n")

try:
    print("-----test--1--")
    f = open("test.txt","r")
    print("-----test--2--")
    f.close()
    print(num)
except Exception as result: #Exception can catch all Errors
    print("Find Error")
    print(result,end="\n\n")



# try...finally and Nested
import time
try:
    fptr = open("test_re.txt","r")
    try:
        while True:
            content = fptr.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content,end="")
    finally:
        fptr.close()
        print("file close")
except Exception as result:
    print("Find Error")