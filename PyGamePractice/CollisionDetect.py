# -*- coding = utf-8 -*-
# @Time: 2021/7/15 下午 05:32
# @Software: PyCharm

import pygame
import sys
from pygame.locals import *

pygame.init()

size = width , height = (400,600)
pygame.display.set_caption("逆行飆車")
screen = pygame.display.set_mode(size)

#設置圖像的幀數率
FPS = 60
clock = pygame.time.Clock()

# 1.角色類繼承Sprite
# 2.應用父類__init__方法初始化對象
# 3.定義精靈組
# 4.碰撞檢測和處理

#定義敵人的類
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()  #調用父類的__init__方法初始化對象
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect(left=width/2-22,top=0)

    def move(self):
        self.rect.move_ip(0,5)

#定義玩家的類
class Player(pygame.sprite.Sprite):
    def __init__(self):
        #super(Player, self).__init__()  #調用父類的__init__方法初始化對象
        super().__init__()
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
enemy = Enemy()

#定義敵人精靈組
enemies = pygame.sprite.Group()
enemies.add(enemy)

#將所有的精靈放到一個組中
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

while True:
    #繪製圖片
    screen.blit(background,(0,0))

    #統一對所有的精靈進行圖像繪製，角色移動的方法調用
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.move()



    # screen.blit(player.image,player.rect)
    # screen.blit(enemy.image,enemy.rect)
    #
    # #角色移動
    # player.move()
    # enemy.move()

    #從事件隊列中取出事件對象，根據類型進行事件處理
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 1.敵人和玩家都存在
    # if pygame.sprite.spritecollide(player,enemies,False):
    #     print("撞車啦...")

    # 2.敵人消失
    # if pygame.sprite.spritecollide(player,enemies,True):    #True表示將敵人碰撞到的對象從組中清除掉
    #     print("撞車啦...")

    # 3.敵人和玩家都消失
    # if pygame.sprite.spritecollide(player,enemies,True):
    #     player.kill()   #單獨控制某個精靈對象消失
    #     print("撞車啦...")

    # 4.玩家消失
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()   #單獨控制某個精靈對象消失
        print("撞車啦...")

    # 從每個組中刪除精靈。不影響精靈的狀態，還是可以重新添加到Group中。
    if player not in all_sprites:
        all_sprites.add(player)

    pygame.display.update()
    clock.tick(FPS) #按照指定更新速率CLOCK來刷新畫面，沒到時間就讓循環等待