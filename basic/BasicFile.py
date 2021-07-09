# -*- coding = utf-8 -*-
# @Time: 2021/7/9 上午 07:43
# @Software: PyCharm
'''
"r" 讀，若文件不存在，報錯
"w" 寫，若文件不存在，建檔；若文件存在，複寫
"a" 寫
"rb" 以二進制的方式讀
"wb" 以二進制的方式寫
'''

'''
#open默認模式為"r"
f = open("test.txt") #若文件不存在，報錯
'''

f = open("test.txt","w") #打開文件
f.write("hello world, I am here!\n") #將字串寫入文件中
f.write("hello world, I am here!\n")
f.write("hello world, I am here!\n")
f.write("hello world, I am here!\n")
f.write("hello world, I am here!\n")
f.close()

#read方法，讀取指定字符在文件頭部，每執行一次向後移動指定字符數
f = open("test.txt","r")
content = f.read(5)
print(content) #hello
content = f.read(11)
print(content) # world, I a
f.close()

f = open("test.txt","r")
content = f.readlines() #一次性讀取全部文件為列表，每行一個字符串元素
print(content)
i = 1
for temp in content:
    print("%d:%s"%(i,temp),end="")
    i += 1
f.close()


f = open("test.txt","r")
content = f.readline()
print("1:%s"%content,end="")
content = f.readline()
print("2:%s"%content,end="")
f.close()

import os #好用的檔案操作函示庫
os.rename("test.txt","test_re.txt")