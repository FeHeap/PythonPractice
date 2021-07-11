# -*- coding = utf-8 -*-
# @Time: 2021/7/10 上午 09:14
# @Software: PyCharm

from bs4 import BeautifulSoup      #網頁解析，獲取數據
import re       #正規表達式，進行文字匹配
import urllib.request,urllib.error  #制定URL，獲取網頁數據
import xlwt     #進行excel操作
import sqlite3  #進行SQLite數據庫操作

def main():
    baseurl = "https://movie.douban.com/top250?start="
    #1.爬取網頁
    datalist = getData(baseurl)
    savepath = ".\\DoubanMovieTop250.xls"
    dbpath = "movie.db"
    #3.保存數據
    saveData(datalist,savepath)
    saveDataDB(datalist,dbpath)
    #askURL("https://movie.douban.com/top250?start=")

#影片詳情連結的規則
findLink = re.compile(r'<a href="(.*?)">') #創建正規表達式對象，表示規則(字符串的模式)
#影片圖片
findImgSrc = re.compile(r'<img.*src="(.*?)"',re.S)  #re.S 讓換行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#影片評分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#找到評價人數
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概況
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相關內容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)

#爬取網頁
def getData(baseurl):
    datalist = []
    for i in range(0,10):   #調用獲取葉面信息的函式，次
        url = baseurl + str(i*25)
        html = askURL(url)  #保存獲取到的網頁原碼
        # 2.逐一解析數據
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"): #查找符合要求的字符串，形成列表
            #print(item) #測試，查看電影item全部信息
            data = []   #保存一部電影的所有信息
            item = str(item)
            #影片詳情連結
            link = re.findall(findLink,item)[0] #re庫用來通過正規表達式查找指定的字符串
            data.append(link)                   #添加連結
            ImgSrc = re.findall(findImgSrc,item)[0]
            data.append(ImgSrc)                 #添加圖片
            titles = re.findall(findTitle,item) #片名可能只有一個中文名，沒有外國名
            if(len(titles) == 2):
                ctitle = titles[0]
                data.append(ctitle)
                otitle = titles[1].replace("/","")  #去掉無關的符號
                data.append(otitle)                 #添加外國名
            else:
                data.append(titles[0])
                data.append(' ')                    #外國名字留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)                     #添加評分

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)                   #添加評分人數

            inq = re.findall(findInq,item)
            if len(inq) != 0:
                inq = inq[0].replace("。","")
                data.append(inq)                    #添加概述
            else:
                data.append(" ")                    #概述留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub("<br(\s+)?/>(\s+)?"," ",bd) #去掉<br/>
            bd = re.sub('/'," ",bd) #替換/
            data.append(bd.strip()) #去掉前後的空格

            datalist.append(data)   #把處理好的一部電影信息放入datalist

    return datalist

#得到指定一個URL的網頁內容
def askURL(url):
    head = {            #模擬瀏覽器頭部訊息，向豆瓣服務器發送消息
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
                        #用戶代理，表示告訴豆瓣服務器，我們式什麼類型的機器、瀏覽器(本質上是告訴瀏覽器，我們可以接收什麼水平的文件內容)
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#保存數據
def saveData(datalist,savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet = book.add_sheet("豆瓣電影Top250",cell_overwrite_ok=True)
    col = ("電影詳情連結","圖片連結","影片中文名","影片外國名","評分","評價數","概況","相關信息")
    for i in range(0,8):
        sheet.write(0,i,col[i]) #行名

    for i in range(0,250):
        print("第%d條"%i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])  #數據

    book.save(savepath) #保存

def saveDataDB(datalist,dbpath):
   init_db(dbpath)
   conn = sqlite3.connect(dbpath)
   cur = conn.cursor()

   for data in datalist:
       for index in range(len(data)):
           if index == 4 or index == 5:
               continue
           data[index] = '"' + data[index] + '"'
       sql = """
           insert into movie250 (
           info_link,pic_link,cname,ename,score,rated,introduction,info)
           values(%s)
           """%",".join(data)
       print(sql)
       cur.execute(sql)
       conn.commit()
   cur.close()
   conn.close()



def init_db(dbpath):
    sql = """
        create table movie250
        (
        id integer primary key autoincrement,
        info_link text,
        pic_link text,
        cname varchar,
        ename varchar,
        score numeric,
        rated numeric,
        introduction text,
        info text
        )
    """    #創建數據表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
    #init_db("movietest.db")

