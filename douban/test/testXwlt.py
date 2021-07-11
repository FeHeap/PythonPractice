# -*- coding = utf-8 -*-
# @Time: 2021/7/11 下午 12:13
# @Software: PyCharm


import  xlwt

workbook = xlwt.Workbook(encoding="utf-8")  #創建workbook對象
worksheet = workbook.add_sheet("sheet1")    #創建工作表
worksheet.write(0,0,'hello')        #寫入數據，第一個參數"列"，第二個參數"行"，第三個參數表示內容
workbook.save('student.xls')        #保存數據表