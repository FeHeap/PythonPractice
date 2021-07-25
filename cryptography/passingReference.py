# -*- coding = utf-8 -*-
# @Time: 2021/7/25 下午 09:24
# @Software: PyCharm

def eggs(someParameter):
    someParameter.append('Hello')

spam = [ 1, 2, 3 ]
eggs(spam)
print(spam)