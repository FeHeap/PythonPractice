# -*- coding = utf-8 -*-
# @Time: 2021/7/11 下午 08:41
# @Software: PyCharm

#define class car
class Car:
    energy = "電動" #field

    def mov(self): #method
        print("在移動...")



#declare a car
c = Car()
print("能源類型：",c.energy)
c.mov()