# -*- coding = utf-8 -*-
# @Time: 2021/7/15 下午 05:32
# @Software: PyCharm

import pygame
import sys
from pygame.locals import *

pygame.init()

size = width , height = (400,600)
pygame.display.set_caption("draw image")
screen = pygame.display.set_mode(size)

#設置圖像的幀數率
FPS = 60
clock = pygame.time.Clock()

# - 定義用戶事件類型名稱及編碼
# - 定義用戶事件觸發條件
# - 定義用戶事件處理過程

#添加用戶自訂義事件
OUT_OF_RANGE = pygame.USEREVENT + 1


#定義玩家的類
class Player:
    def __init__(self):
        x,y = (width/2,height/2)
        self.image = pygame.image.load("Player.png")
        #self.rect = self.image.get_rect(top=200,left=200)   #(0,0)
        self.rect = self.image.get_rect(center = (x,y))

    def move(self):
        mouseX,mouseY = pygame.mouse.get_pos()

        #觸發用戶自訂義的事件
        if self.rect.left < 40 or self.rect.left > 360:
            pygame.event.post(pygame.event.Event(OUT_OF_RANGE))

        ##鼠標位置默認定在rect的左上角座標處
        # self.rect.x = mouseX
        # self.rect.y = mouseY
        #if 22 <= mouseX <= width-22 and  48 <= mouseY <= height-48:
        if self.rect.width/2 <= mouseX <= width - self.rect.width/2 \
                and self.rect.height/2 <= mouseY <= height - self.rect.height/2:
            self.rect.center = (mouseX,mouseY)



#加載背景圖片
background = pygame.image.load("AnimatedStreet.png")

#定義玩家對象
player = Player()

while True:
    #繪製圖片
    screen.blit(background,(0,0))
    screen.blit(player.image,player.rect)
    player.move()

    #從事件隊列中取出事件對象，根據類型進行事件處理
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 對用戶自訂義事件進行處理
        if event.type == OUT_OF_RANGE:
            print("超過範圍啦...")

    # pressed_keys = pygame.key.get_pressed()
    # if pressed_keys[pygame.K_DOWN]:
    #     player.rect.move_ip(0,5)

    pygame.display.update()
    clock.tick(FPS) #按照指定更新速率CLOCK來刷新畫面，沒到時間就讓循環等待