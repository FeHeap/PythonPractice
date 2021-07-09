# -*- coding = utf-8 -*-
# @Time: 2021/7/9 上午 08:47
# @Software: PyCharm

gushi = """
長相思，在長安。
絡緯秋啼金井闌，微霜悽悽簟色寒。
孤燈不明思欲絕，卷帷望月空長嘆。
美人如花隔雲端。
上有青冥之高天，下有淥水之波瀾。
天長路遠魂飛苦，夢魂不到關山難。
長相思，摧心肝。
日色慾盡花含煙，月明欲素愁不眠。
趙瑟初停鳳凰柱，蜀琴欲奏鴛鴦弦。
此曲有意無人傳，願隨春風寄燕然。
憶君迢迢隔青天。
昔時橫波目，今作流淚泉。
不信妾腸斷，歸來看取明鏡前。
美人在時花滿堂，美人去後花餘牀。
牀中繡被卷不寢，至今三載聞餘香。
香亦竟不滅，人亦竟不來。
相思黃葉落，白露溼青苔。
"""

fptr = open("gushi.txt","w",encoding="utf-8")
fptr.write(gushi.strip())
fptr.close()

try:
    fptr = open("gushi.txt","r",encoding="utf-8")
    try:
        content = fptr.readlines()
    except Exception as result:
        print("Find Error")
    finally:
        fptr.close()
except Exception as result:
    print("Find Error")

fptr = open("copy.txt","w",encoding="utf-8")
for str in content:
    fptr.write(str)
fptr.close()