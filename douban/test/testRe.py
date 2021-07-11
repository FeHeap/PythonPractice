# -*- coding = utf-8 -*-
# @Time: 2021/7/11 上午 10:59
# @Software: PyCharm

#正規表達式：字符串模式 (判斷字符串是否符合一定的標準

import re
#創建模式對象

pat = re.compile("AA") #此處的AA，是正規表達式，用來去驗證其他的字符串
m = pat.search("CBA") #search字符串備校驗的內容
print(m) #None

m = pat.search("ABCAA")
print(m) #<re.Match object; span=(3, 5), match='AA'>

m = pat.search("AABCAADDCCAAA") #search方法，進行比對查找
print(m) #<re.Match object; span=(0, 2), match='AA'>


#沒有模式對象
m = re.search("asd","Aasd") #前面的字符串是規則(模板)，後面的字符串是被校驗的對象
print(m) #<re.Match object; span=(1, 4), match='asd'>

print(re.findall("a","ASDaDFGAa"))  #前面字符串是規則(正規表達式)，後面的字符串是被校驗的對象
print(re.findall("[A-Z]","ASDaDFGAa"))  #['A', 'S', 'D', 'D', 'F', 'G', 'A']
print(re.findall("[A-Z]+","ASDaDFGAa")) #['ASD', 'DFGA']

#sub
print(re.sub("a","A","abcdcasd")) #找到a用A替換，在第三個字符串中查找"a"

#建議在正規表達式中，被比較的字符串前面加r，不用擔心轉譯字符的問題
a = r"\aabd-\'"
print(a)