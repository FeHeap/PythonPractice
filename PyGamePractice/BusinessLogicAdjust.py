# -*- coding = utf-8 -*-
# @Time: 2021/7/15 下午 05:32
# @Software: PyCharm

#技術僅僅是遊戲的基礎
#遊戲最重要的是【體驗】

#1.角色不能超出邊界
#2.碰撞畫面不真實(縮小rect的範圍)
#3.難度隨著時間增加(敵人的速度變快)




import pygame
import sys
from pygame.locals import *
import time
import random

pygame.init()

size = width , height = (400,600)
pygame.display.set_caption("逆行飆車")
screen = pygame.display.set_mode(size)

#定義顏色
BLACK = (0,0,0)
RED = "#FF0000"

SCORE = 0
SPEED = 5   #敵人的運動速度

#設置圖像的幀數率
FPS = 60
clock = pygame.time.Clock()

#定義用戶事件
SPEED_UP = pygame.USEREVENT + 1
pygame.time.set_timer(SPEED_UP,1000)    #每隔1000毫秒就將事件編碼放到事件隊列中1次

#設置字體和文字
font_big = pygame.font.SysFont("Californian FB",60)
font_small = pygame.font.SysFont("華康兒風體W4",20)
game_over = font_big.render("Game Over",True,BLACK)

#播放BGM
pygame.mixer.Sound("background.wav").play(-1) #背景音樂默認執行1遍，參數loop莫認為0，-1表示無限循環



#定義敵人的類
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()  #調用父類的__init__方法初始化對象
        x,y = (random.randint(22,378),0)
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (x,y))

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if self.rect.top > height:
            SCORE += 1
            self.rect.top = 0
            self.rect.top = 0
            self.rect.left = random.randint(22,378)


#定義玩家的類
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        x,y = (width/2,height/2)
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40,75))
        self.rect = self.surf.get_rect(left=178,bottom=height-21)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom <= height - 21:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right <= width-4:
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
    scores = font_small.render(str(SCORE),True,BLACK)
    screen.blit(scores,(10,10))

    #統一對所有的精靈進行圖像繪製，角色移動的方法調用
    for sprite in all_sprites:
        screen.blit(sprite.image, sprite.rect)
        sprite.move()

    #從事件隊列中取出事件對象，根據類型進行事件處理
    for event in pygame.event.get():
        if event.type == SPEED_UP:
            SPEED += 0.5
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 撞擊後，遊戲結束
    if pygame.sprite.spritecollideany(player, enemies):

        pygame.mixer.Sound("crash.wav").play()
        time.sleep(1)

        screen.fill(RED)
        screen.blit(game_over, (80, 150))

        pygame.display.update()
        time.sleep(2)

        pygame.quit()
        sys.exit()


    pygame.display.update()
    clock.tick(FPS) #按照指定更新速率CLOCK來刷新畫面，沒到時間就讓循環等待