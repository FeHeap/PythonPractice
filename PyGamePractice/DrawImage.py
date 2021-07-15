# -*- coding = utf-8 -*-
# @Time: 2021/7/15 下午 05:02
# @Software: PyCharm


import pygame
import sys

pygame.init()

size = width , height = (400,600)
pygame.display.set_caption("draw image")
screen = pygame.display.set_mode(size)

#設置圖像的幀數率
FPS = 60
clock = pygame.time.Clock() #返回時鐘對象


background = pygame.image.load("AnimatedStreet.png")
player = pygame.image.load("Player.png")
x,y = 178,504

while True:
    screen.blit(background,(0,0))   #繪製局部圖像，將background圖像顯示在座標(0,0)的位置上。
    screen.blit(player,(x,y))
    y -= 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(FPS) #按照指定更新速率CLOCK來刷新畫面，沒到時間就讓循環等待