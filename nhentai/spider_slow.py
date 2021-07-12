# -*- coding = utf-8 -*-
# @Time: 2021/7/12 上午 06:04
# @Software: PyCharm

import re
import urllib.request,urllib.error
import xlwt

search = ""
language = ""

languageDict = {"e":"12227","E":"12227","c":"29963","C":"29963","j":"6346","J":"6346","a":"","A":""}
languageDictrev = {"12227":"E","29963":"C","6346":"J"}

def main():
    global language
    while True:
        try:
            language = input("語言(中文：C,英文：E,日文：J,全語言：A)：")
            L = language.upper()
            language = languageDict[language];
            break
        except KeyError:
            print("Input error!!",end="\n\n")

    global search
    search = input("輸入想要搜尋的關鍵字：")

    baseurl = "https://nhentai.net/?page="

    datalist = getData(baseurl)

    savepath = ".\\nhentai_%s_%s.xls"%(search,L)

    saveData(datalist,savepath)
    print("爬取完畢!!")


last = re.compile(r'<a href="/\?page=(\d*)" class="last">')

id = re.compile(r'<a href="/g/(.*?)">')

name = re.compile(r'<div class="caption">(.*?)</div>',re.S)

parameter = re.compile(r'<div class="gallery" data-tags="(.*?)">')

def getData(baseurl):
    html = askURL(baseurl)
    m = last.search(html)
    lastPage = int(re.search("[\d]+",m[0])[0])
    # lastPage //= 100
    datalist = []
    if(len(language) != 0):
        languageCJE = languageDictrev[language]
        for page in range(1,lastPage+1):
            print("(%d/%d)"%(page,lastPage))
            url = baseurl + str(page)
            html = askURL(url)
            IDs = id.findall(html)
            names = name.findall(html)
            parameters = parameter.findall(html)
            for i in range(5,len(IDs)):
                IDs[i] = re.search("[\d]+",IDs[i])
                if re.search(search,names[i],flags=re.IGNORECASE) is not None and re.search(language,parameters[i]) is not None:
                    data = []
                    data.append(languageCJE)
                    data.append(IDs[i][0])
                    data.append(names[i])
                    datalist.append(data)
    else:
        for page in range(1,lastPage+1):
            print("(%d/%d)"%(page, lastPage))
            url = baseurl + str(page)
            html = askURL(url)
            IDs = id.findall(html)
            names = name.findall(html)
            parameters = parameter.findall(html)
            for i in range(5,len(IDs)):
                IDs[i] = re.search("[\d]+",IDs[i])
                for key,value in languageDictrev.items():
                    if re.search(key, parameters[i]) is not None:
                        languageCJE = value
                        break
                if re.search(search,names[i],flags=re.IGNORECASE) is not None and re.search(language,parameters[i]) is not None:
                    data = []
                    data.append(languageCJE)
                    data.append(IDs[i][0])
                    data.append(names[i])
                    datalist.append(data)
    return datalist


def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    request = urllib.request.Request(url,headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except (urllib.error.HTTPError,urllib.error.URLError) as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(datalist,savepath):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("hentai")

    for i,datas in enumerate(datalist):
        for j,data in enumerate(datas):
            worksheet.write(i,j,data)
    workbook.save(savepath)


if __name__ == "__main__":
    main()