# -*- coding = utf-8 -*-
# @Time: 2021/7/15 下午 05:21
# @Software: PyCharm


import pygame
import sys

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
        #self.rect.y -= 1
        #self.rect = self.rect.move(0,-1)
        self.rect.move_ip(0,-2)



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
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(FPS) #按照指定更新速率CLOCK來刷新畫面，沒到時間就讓循環等待