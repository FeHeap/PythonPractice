# -*- coding = utf-8 -*-
# @Time: 2021/7/9 上午 05:07
# @Software: PyCharm

products = [["iphone",6888],["MacPro",14800],["Mi6",2499],["Coffee",31],["Book",60],["Nike",699]]
print("----- product list -----")
for index,product in enumerate(products):
    if(len(product[0]) < 6):
        print("%d %s\t\t%d"%(index,product[0],product[1]))
    else:
        print("%d %s\t%d"%(index, product[0], product[1]))
print("-"*24)

shoppingCart = [0,0,0,0,0,0]
choose = ""
while choose != "q":
    choose = input("What do you want to buy now？\ninput(0~5):")
    if not (choose.isdigit() or choose == "q"):
        print("input error!")
    elif choose.isdigit():
        if(int(choose) >= 0 and int(choose) <= 5):
            shoppingCart[int(choose)] += 1;
        else:
            print("input error!")

sum = 0
print("----- shopping list -----")
for product in products:
    if (len(product[0]) < 4):
        print("%s\t\t%d"%(product[0], shoppingCart[products.index(product)]))
    else:
        print("%s\t%d"%(product[0], shoppingCart[products.index(product)]))
    sum += product[1] * shoppingCart[products.index(product)]
print("price =",sum)
print("-"*25)