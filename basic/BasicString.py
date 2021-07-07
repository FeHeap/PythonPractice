# -*- coding = utf-8 -*-
# @Time: 2021/7/8 上午 06:50
# @Software: PyCharm

#In Python3 Source file, the default of <str> is utf-8
word = 'string'
sentence = "this is a sentence"
paragraph = """
    this is a paragraph
    which consists of multi-line
"""

print(word)
print(sentence)
print(paragraph)

#my_str = "I'm a student."
my_str = 'I\'m a student.'
print(my_str,end="\n\n")

#my_str = "Jason said \"I like you.\""
my_str = 'Jason said "I like you."'
print(my_str,end="\n\n")

str = "taiwan"
print(str)
print(str[0:5]) #[start:end]
print(str[0:6:2]) #[start:end:step]
print(str[:3]) #tai
print(str[3:]) #wan
print(str + ", hello!") #Use '+' to connect strings
print(str * 3)
print("hello\ntaiwan")  #Use '\' to achieve the function of escape
print(r"hello\ntaiwan") #Adding 'r' before a string display original string without escape


'''
#common str method
--------------------------
bytes.decode(encoding='utf-8',errors='strict')
encode(encoding='utf-8',errors='strict')
isalnum()
isalpha()
isdigit()
isnumeric()
join(seq)
len(string)
lstrip()
rstrip()
split(str="",num=string.count(str))
'''