# -*- coding = utf-8 -*-
# @Time: 2021/7/12 下午 11:07
# @Software: PyCharm

import jieba    #分詞
from matplotlib import pyplot as plt    #繪圖，數據可視化
from wordcloud import WordCloud         #詞雲
from PIL import Image                   #圖片處理
import numpy as np                      #矩陣運算
import sqlite3                          #數據庫

#準備詞雲所需的詞
con = sqlite3.connect('movie.db')
cur = con.cursor()
sql = 'select introduction from movie250'
data = cur.execute(sql)
text = ""
for item in data:
    text += item[0]
    #print(item[0])
#print(text)
cur.close()
con.close()

#分詞
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

img = Image.open('圖.png')  #打開遮罩圖片
img_array = np.array(img)  #將圖片轉換為數組
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="mingliu.ttc"
)
wc.generate_from_text(string)

#繪製圖片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off') #是否顯示座標軸

#plt.show()  #顯示生成的詞雲圖片

#輸出詞雲圖片到文件
plt.savefig('word.jpg',dpi=500)

