# -*- coding = utf-8 -*-
# @Time: 2021/7/15 下午 12:01
# @Software: PyCharm

import pygame
import sys

pygame.init()   #pygame初始化

screen = pygame.display.set_mode((500,500))

while True:
    pygame.display.update() #遊戲就是不斷重新繪製畫面的過程
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  #如果系統再pygame.quit()前終止，IDLE會掛起。所以一般會在最後調用sys.exit()