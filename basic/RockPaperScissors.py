# -*- coding = utf-8 -*-
# @Time: 2021/7/7 下午 11:59
# @Software: PyCharm
import random
user = input("Input: Rock(0), Paper(1), Scissor(2):")
if(user != "0" and user != "1" and user != "2"):
    print("Input error!")
else:
    user = int(user)
    robot = random.randint(0,2)
    print("robot chose number:%d" % robot)
    if user == robot:
        print("--Tie--")
    else:
        if user == 0:   #user:Rock
            if robot == 1:      #Paper
                print("haha, you lose.")
            elif robot == 2:    #Scissor
                print("You win.")
        elif user == 1: #user:Paper
            if robot == 2:      #Scissor
                print("haha, you lose.")
            elif robot == 0:    #Rock
                print("You win.")
        elif user == 2: #user:Scissor
            if robot == 0:      #Rock
                print("haha, you lose.")
            elif robot == 1:    #Paper
                print("You win.")

