# -*- coding = utf-8 -*-
# @Time: 2021/7/24 下午 04:34
# @Software: PyCharm

message = 'guv6(v6(z!(6rp5r7(zr66ntr+'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()_+-=[]{}|;:<>,/'
LENGTH = len(SYMBOLS)

for key in range(LENGTH):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            if symbol in SYMBOLS:
                symbolIndex = SYMBOLS.find(symbol)
                translatedIndex = (symbolIndex - key + LENGTH) % LENGTH
                translated += SYMBOLS[translatedIndex]
            else:
                translated += symbol

    print("Key #%d: %s"%(key,translated))
