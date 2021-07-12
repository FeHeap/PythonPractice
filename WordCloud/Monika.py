# -*- coding = utf-8 -*-
# @Time: 2021/7/13 上午 02:23
# @Software: PyCharm

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np
import sys

textFile = "Dokidoki.txt"
maskFile = "heart.jpg"
fontSet = "mingliu.ttc"
backgroundColor = 'black'
outputFile = "MonikaOnly.jpg"

#read text file
try:
    file = open(textFile,"r",encoding="utf-8")
    try:
        content = file.read().splitlines()
    except Exception as result:
        print("Find Error")
        sys.exit(0)
    finally:
        file.close()
except FileNotFoundError:
    print("Can't find file \"%s\""%textFile)
    sys.exit(1)

text = ""
for string in content:
    text = text + string + " "

#separate words
cut = jieba.cut(text)
string = ' '.join(cut)

#open the mask img
try:
    img = Image.open(maskFile)
except FileNotFoundError:
    print("Can't find file \"%s\""%maskFile)
    sys.exit(1)

#transform mask img into list
img_array = np.array(img)
try:
    wc = WordCloud(
        background_color=backgroundColor,
        mask=img_array,
        font_path=fontSet
    )
    try:
        wc.generate_from_text(string)
    except Exception:
        print("Find Error! Maybe you should adjust your text file")
        sys.exit(1)
except Exception:
    print("Find Error!")
    sys.exit(1)

#get the colors from img_array
image_colors = ImageColorGenerator(img_array)

#generate output word cloud img
fig = plt.figure(1)
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off') #close axis

#plt.show()     #show the worl cloud img

#save the worl cloud img as file
plt.savefig(outputFile,dpi=500)
