# -*- coding = utf-8 -*-
# @Time: 2021/7/24 下午 04:26
# @Software: PyCharm

message = 'This is my secret message.'
key = 13
mode = 'encrypt' #may be encrypt or decrypt
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'
LENGTH = len(SYMBOLS)
translated = ''

for symbol in message:

    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        if mode == 'encrypt':
            translatedIndex = (symbolIndex + key) % LENGTH
        elif mode == 'decrypt':
            translatedIndex = (symbolIndex - key + LENGTH) % LENGTH

        translated += SYMBOLS[translatedIndex]

    else:
        translated += symbol

print(translated)