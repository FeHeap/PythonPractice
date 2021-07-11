# -*- coding = utf-8 -*-
# @Time: 2021/7/11 下午 12:23
# @Software: PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet("MultiplicationTable")

for i in range(0,9):
    for j in range(0,i+1):
        content = ""
        worksheet.write(i,j,"%d x %d = %d"%(i+1,j+1,(i+1)*(j+1)))

workbook.save("MultiplicationTable.xls")