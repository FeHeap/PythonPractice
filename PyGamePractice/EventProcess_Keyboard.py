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

#定義玩家的類
class Player:
    def __init__(self):
        x,y = (width/2,height/2)
        self.image = pygame.image.load("Player.png")
        #self.rect = self.image.get_rect(top=200,left=200)   #(0,0)
        self.rect = self.image.get_rect(center = (x,y))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)



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

    # pressed_keys = pygame.key.get_pressed()
    # if pressed_keys[pygame.K_DOWN]:
    #     player.rect.move_ip(0,5)

    pygame.display.update()
    clock.tick(FPS) #按照指定更新速率CLOCK來刷新畫面，沒到時間就讓循環等待