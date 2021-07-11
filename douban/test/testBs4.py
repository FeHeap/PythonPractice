# -*- coding = utf-8 -*-
# @Time: 2021/7/11 上午 09:22
# @Software: PyCharm

'''
BeautifulSoup4將複雜的HTML文檔轉成一個複雜的樹型結構，每個節點都是Python對象可以歸納為4種：

- Tag
- NavigableString
- BeautifulSoup
- Comment
'''
import re

from bs4 import BeautifulSoup

file = open("baidu.html","rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html,"html.parser")

print(bs.title)
print(bs.a)
print(bs.head)

print(type(bs.head)) #<class 'bs4.element.Tag'>
#1.Tag  標籤及其內容;拿到它所找到的第一個內容

print(bs.title.string)
print(type(bs.title.string)) #<class 'bs4.element.NavigableString'>
#2.NavigableString  標籤裡的內容(字符串)


print(type(bs)) #<class 'bs4.BeautifulSoup'>
#3.BeautifulSoup    表示整個文檔

print(bs.name)
print(bs)

print(bs.a.string)
print(type(bs.a.string)) #<class 'bs4.element.Comment'>
#4.Comment  是一個特殊的NavigableString，輸出內容不包含註釋符號

#--------------------------------------

#文黨的遍歷
print(bs.head.contents)
print(bs.head.contents[1])
#更多內容，搜索BeautifulSoup文檔


#文黨的搜索

#(1)find_all()
#字符串過濾：會查找與字符串完全匹配的內容
t_list = bs.find_all("a")
print(t_list)

import re
#正規表達視搜索：使用search()方法來匹配內容
t_list = bs.find_all(re.compile("a"))
print(t_list)

#1.方法：傳入一個函數(方法)，根據函數的要求來搜索
def name_is_exists(tag):
    return tag.has_attr("name")

t_list = bs.find_all(name_is_exists)

for item in t_list:
    print(item)

#2.kwargs   參數
t_list = bs.find_all(id="head")
t_list = bs.find_all(href="http://news.baidu.com")
t_list = bs.find_all(class_=True)
for item in t_list:
    print(item)

#3.text參數
t_list = bs.find_all(text="hao123")
t_list = bs.find_all(text=["hao123","地圖","貼吧"])
t_list = bs.find_all(text=re.compile("\d")) #應用正規表達式來查找特定文本的內容(標籤裡的字符串)
for item in t_list:
    print(item)


#4.limit參數
t_list = bs.find_all("a",limit=3)

for item in t_list:
    print(item)

#css選擇器
t_list = bs.select('title') #通過標籤來查找
t_list = bs.select(".mnav") #通過類名來查找
t_list = bs.select("#u1") #通過id來查找
t_list = bs.select("a[class='bri']") #通過屬性來查找
t_list = bs.select("head > title") #通過子標籤來查找
for item in t_list:
    print(item)

t_list = bs.select(".mnav ~ .bri")
print(t_list[0].get_text())
