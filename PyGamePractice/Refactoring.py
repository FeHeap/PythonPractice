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


class Constant:

    SCREEN_WIDTH = 400
    SCREEN_HEIGHT = 600

    # 定義顏色
    BLACK = (0, 0, 0)
    RED = "#FF0000"

    SCORE = 0
    SPEED = 5  # 敵人的運動速度

    # 設置圖像的幀數率
    FPS = 60



#定義敵人的類
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()  #調用父類的__init__方法初始化對象
        x,y = (random.randint(22,378),0)
        self.image = pygame.image.load("Enemy.png")
        self.surf = pygame.Surface((42, 70))
        self.rect = self.surf.get_rect(center = (x,y))

    def move(self):
        #global SCORE
        self.rect.move_ip(0,Constant.SPEED)
        if self.rect.top > Constant.SCREEN_HEIGHT:
            Constant.SCORE += 1
            self.rect.top = 0
            self.rect.top = 0
            self.rect.left = random.randint(22,378)


#定義玩家的類
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.surf = pygame.Surface((40,75))
        self.rect = self.surf.get_rect(left=178,bottom=Constant.SCREEN_HEIGHT-21)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] and self.rect.top >= 0:
            self.rect.move_ip(0, -5)
        if pressed_keys[pygame.K_DOWN] and self.rect.bottom <= Constant.SCREEN_HEIGHT - 21:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT] and self.rect.left >= 0:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT] and self.rect.right <= Constant.SCREEN_WIDTH-4:
            self.rect.move_ip(5, 0)





class Game:
    def __init__(self):
        pygame.init()

        # 定義用戶事件
        self.SPEED_UP = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SPEED_UP, 1000)  # 每隔1000毫秒就將事件編碼放到事件隊列中1次

        self.clock = pygame.time.Clock()

        size = width, height = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        pygame.display.set_caption("逆行飆車")
        self.screen = pygame.display.set_mode(size)

        # 設置字體和文字
        self.font_big = pygame.font.SysFont("Californian FB", 60)
        self.font_small = pygame.font.SysFont("Bauhaus 93", 30)
        self.game_over = self.font_big.render("Game Over", True, Constant.BLACK)

        # 加載背景圖片
        self.background = pygame.image.load("AnimatedStreet.png")


    def run(self):
        # 定義玩家對象
        player = Player()
        enemy = Enemy()

        # 定義敵人精靈組
        enemies = pygame.sprite.Group()
        enemies.add(enemy)

        # 將所有的精靈放到一個組中
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(enemy)

        # 播放BGM
        pygame.mixer.Sound("background.wav").play(-1)  # 背景音樂默認執行1遍，參數loop莫認為0，-1表示無限循環

        while True:
            # 繪製圖片
            self.screen.blit(self.background, (0, 0))
            scores = self.font_small.render(str(Constant.SCORE), True, Constant.BLACK)
            self.screen.blit(scores, (10, 10))

            # 統一對所有的精靈進行圖像繪製，角色移動的方法調用
            for sprite in all_sprites:
                self.screen.blit(sprite.image, sprite.rect)
                sprite.move()

            # 從事件隊列中取出事件對象，根據類型進行事件處理
            for event in pygame.event.get():
                if event.type == self.SPEED_UP:
                    Constant.SPEED += 0.5
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # 撞擊後，遊戲結束
            if pygame.sprite.spritecollideany(player, enemies):
                pygame.mixer.Sound("crash.wav").play()
                time.sleep(1)

                self.screen.fill(Constant.RED)
                self.screen.blit(self.game_over, (80, 150))
                score_display = self.font_big.render("score:%d" % Constant.SCORE, True, Constant.BLACK)
                self.screen.blit(score_display, (120, 300))

                pygame.display.update()
                time.sleep(2)

                pygame.quit()
                sys.exit()

            pygame.display.update()
            self.clock.tick(Constant.FPS)  # 按照指定更新速率CLOCK來刷新畫面，沒到時間就讓循環等待


if __name__ == '__main__':
    game = Game()
    game.run()