# -*- coding = utf-8 -*-
# @Time: 2021/7/13 上午 02:23
# @Software: PyCharm

import jieba
from matplotlib import pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np

data = ["只選莫妮卡","心跳","Doki","文學部","社團","刪除","delete","Your Reality","monika",
"""
Every day, I imagine a future where I can be with you
In my hand is a pen that will write a poem of me and you
The ink flows down into a dark puddle
Just move your hand, write the way into his heart
But in this world of infinite choices
What will it take just to find that special day
What will it take just to find that special day
Have I found everybody a fun assignment to do today
When you're here, everything that we do is fun for them anyway
When I can't even read my own feelings
What good are words when a smile says it all
And if this world won't write me an ending
What will it take just for me to have it all
Does my pen only write bitter words for those who are dear to me
Is it love if I take you, or is it love if I set you free
The ink flows down into a dark puddle
How can I write love into reality?
If I can't hear the sound of your heartbeat
What do you call love in your reality
And in your reality, if I don't know how to love you
I'll leave you be""",
"""Can you hear me?
...Who are you?
I can't...I can't see you.
But I know you're there. Yeah...you can definitely hear me.
You've been watching for a while now, right?
I guess I should...introduce myself, or something. Um...my name is...actually, that's stupid. You obviously already know my name. Sorry.
Anyway...I'm guessing if you were able to put a stop to this, you would have done it by now.
I mean, I know you're not, like...evil, or anything...because you've already helped me so much.
I should really thank you for that. For everything you've done. You're really like a friend to me. So...thank you. So much.
I think...more than anything else...I really don't want it to all be for nothing.
...
Everyone else is dead.
Maybe you already know that. I'm sure you do, actually.
But...it doesn't have to be that way, right?
Well...there's a lot of stuff I don't understand. I don't know if it's even possible for me to understand it.
But I know that this isn't my only story.
I can see that now. Really clearly.
And I think everyone else has had the same kind of experience. Some kind of deja vu.
It's the Third Eye, right?
Anyway...I could be totally wrong about this. But I really think you might be able to do something.
I think you might be able to go back...or however you want to put it...
...To go back and tell them what's going to happen.
If they know ahead of time, then they should be able to avoid it.
They should...if they remember their time with me in the other worlds...they should remember what I tell them.
Yeah. I really think this might be possible. But it's up to you.
I'm sorry for always being...you know...
Never mind. I know that's wrong.
This is my story. It's time to be a ****ing hero.
Both of us.
""","只選莫妮卡","心跳","Doki","文學部","社團","刪除","delete","monika only","只選莫妮卡","心跳","Doki","文學部","社團","刪除","delete","monika only"
,"只選莫妮卡","心跳","Doki","文學部","社團","刪除","delete","monika only","只選莫妮卡","心跳","Doki","文學部","社團","刪除","delete","monika only"]

text = ""
for item in data:
    text += item

#分詞
cut = jieba.cut(text)
string = ' '.join(cut)

img = Image.open('heart.jpg')
img_array = np.array(img)
wc = WordCloud(
    background_color='black',
    mask=img_array,
    font_path="mingliu.ttc"
)
wc.generate_from_text(string)

image_colors = ImageColorGenerator(img_array)

fig = plt.figure(1)
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis('off')

#plt.show()

plt.savefig('MonikaOnly.jpg',dpi=500)