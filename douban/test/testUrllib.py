# -*- coding = utf-8 -*-
# @Time: 2021/7/10 上午 09:43
# @Software: PyCharm

import urllib.request

#獲取一個get請求
response = urllib.request.urlopen("http://www.baidu.com")
print(response)
print(response.read().decode('utf-8')) #對獲取到的網頁原碼進行utf-8解碼

#獲取一個post請求
import urllib.parse
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode("utf-8"))

#超時處理
try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("time out!")


response = urllib.request.urlopen("http://www.baidu.com")
print(response.status) #(404:找不到),(418:我是一個茶壺),更多參間：https://zh.wikipedia.org/wiki/HTTP%E7%8A%B6%E6%80%81%E7%A0%81
print(response.getheaders())
print(response.getheader("Server"))


url = "http://httpbin.org/post"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
data = bytes(urllib.parse.urlencode({'name':'eric'}),encoding='utf-8')
req = urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))


url = "https://www.douban.com"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))