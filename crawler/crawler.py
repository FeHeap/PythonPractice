import encodings.utf_8
import json
import urllib.request, urllib.error
import re

# 異步爬取解析
def main():
    url = "https://www3.nhk.or.jp/news/json16/word/0000967_002.json"
    #askURL(url)
    result = open('result.json', 'r')
    data = result.read()
    jsonObj = json.loads(data)
    #print(jsonObj)
    for item in jsonObj['channel']['item']:
        print(item['title'],'\n',item['pubDate'])

    # 防BAN:
    # 1.間隔時間爬取
    # 2.代理


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('gbk')
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == '__main__':
    main()