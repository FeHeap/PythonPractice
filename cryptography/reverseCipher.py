# -*- coding = utf-8 -*-
# @Time: 2021/7/24 下午 03:56
# @Software: PyCharm

message = 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated += message[i]
    i -= 1

print(translated)
