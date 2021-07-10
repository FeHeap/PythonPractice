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
    #3.保存數據
    saveData(savepath)
    askURL("https://movie.douban.com/top250?start=")

#爬取網頁
def getData(baseurl):
    datalist = []
    for i in range(0,10):   #調用獲取葉面信息的函式，次
        url = baseurl + str(i*25)
        html = askURL(url)  #保存獲取到的網頁原碼
        # 2.逐一解析數據
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
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html




#保存數據
def saveData(savepath):
    print("save...")

if __name__ == "__main__":
    main()
