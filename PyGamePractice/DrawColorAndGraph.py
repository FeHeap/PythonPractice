# -*- coding = utf-8 -*-
# @Time: 2021/7/15 下午 12:09
# @Software: PyCharm

import pygame
import sys

pygame.init()

pygame.display.set_caption("Draw graph")
size = width , heught = 300 , 300
screen = pygame.display.set_mode(size)

#定義顏色變量
WHITE = pygame.color.Color(255,255,255) #定義一個顏色常量white，表示白色
BLACK = pygame.color.Color(0,0,0,a=255) #定義黑色，alpha通道默認微255(不透明)
RED = "#FF0000"
GREEN = "0x00FF00"
BLUE = (0,0,255)    #Python2.0後支持元組、列表和對象，例如:[0,0,255]

screen.fill(WHITE)

while True:
    # 在座標(100,50)處，畫一個半徑為30像素的黑色的圓
    pygame.draw.circle(screen, BLACK, (100,50), 30)
    # 在座標(200,50)處，畫一個半徑為30像素的黑色的圓
    pygame.draw.circle(screen, BLACK, (200, 50), 30, 3, False, False, True, True)
    # 畫一條藍色的，以座標(150,130)處為起點，座標(130,170)處為終點的線
    pygame.draw.line(screen, BLUE, (150,130), (130,170))
    # 畫一條藍色的，以座標(150,130)處為起點，座標(170,170)處為終點的線
    pygame.draw.line(screen, BLUE, (150, 130), (170, 170), 1)
    # 畫一條綠色的，以座標(130,170)處為起點，座標(170,170)處為終點的線
    pygame.draw.line(screen, GREEN, (130, 170), (170, 170), 5)
    # 畫一條紅色的，左上方的座標點為(100,200)，寬100，高50的，邊框寬度為2(空心)的矩形
    pygame.draw.rect(screen, RED, (100, 200, 100, 50), 2)
    # 默認為0，表是實心的矩形
    pygame.draw.rect(screen, BLACK, (110, 260, 80, 5))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()