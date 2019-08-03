import pygame
import sys
import random
import time
#这个模块包含各种pygame所使用的常量
from pygame.locals import *


#定义颜色
redcolor = pygame.Color(255,0,0)#color大小写不能错
blackcolor = pygame.Color(0,0,0)
whitecolor = pygame.Color(255,255,255)
print('redcolor:',type(redcolor))
print('blackcolor:',type(blackcolor))
print('whitecolor:',type(whitecolor))
pygame.init()
# 创建pygame 显示界面
playSurface = pygame.display.set_mode((640, 480))  # 注意这里是两个（）
print('playSurface:',type(playSurface))

pygame.display.set_caption('贪吃蛇')

#定义游戏结束函数
def gameOver(playSurface):
    pygame.init()  # 初始化pygame
    # DISPLAYSURF = pygame.display.set_mode((640, 480))  # 设置窗口的大小，单位为像素
    # pygame.display.set_caption('贪吃蛇')  # 设置窗口的标题
    # 定义几个颜色
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 128)
    fontObj = pygame.font.Font(None, 48)  # 通过字体文件获得字体对象
    textSurfaceObj = fontObj.render("Game Over", True, GREEN, BLUE)  # 配置要显示的文字
    textRectObj = textSurfaceObj.get_rect()  # 获得要显示的对象的rect
    textRectObj.center = (320, 240)  # 设置显示对象的坐标
    # DISPLAYSURF.fill(WHITE)  # 设置背景
    # DISPLAYSURF.blit(textSurfaceObj, textRectObj)  # 绘制字体
    playSurface.blit(textSurfaceObj, textRectObj)
    pygame.display.flip()
    time.sleep(1)
    pygame.quit()
    sys.exit()

#定义main 函数 定义我们的入口函数
def main():
    DISPLAYSURF = pygame.display.set_mode((640, 480))  # 设置窗口的大小，单位为像素
    pygame.display.set_caption('贪吃蛇')  # 设置窗口的标题
    #初始化pygame
    #pygame.init()
    #定义一个变量开控制速度
    fpsClock=pygame.time.Clock()
    print('fpsClock:', type(fpsClock))
    #初始化变量
    #初始化贪吃蛇的起始坐标位置 我们（100，100）
    snakePosition=[100,100]
    #初始化贪吃蛇长度list 中有几个元素代表有几段身体
    snakeBody=[[80,100],[60,100],[40,100]]
    #初始化目标方块的位置
    targetPosition=[300,300]
    #目标放开的标记 目的：判断是否吃掉了这个目标方块 1就是没有吃掉 0就是吃掉
    targetfalg=1
    #初始化方向
    direction='right'
    #定义一个方向变量（人为控制 按键有关系）
    changeDirction=direction
    speed=15

    while True:

        for event in pygame.event.get():#从队列当中获取事件
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key == K_RIGHT:
                    changeDirction='right'
                if event.key == K_LEFT:
                    changeDirction='left'
                if event.key == K_UP:
                    changeDirction = 'up'
                if event.key == K_DOWN:
                    changeDirction = 'down'
                    #对应该键盘上的Esc键
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        #确定方向
        if changeDirction=='left' and not direction=='right':
            direction=changeDirction
        if changeDirction == 'right' and not direction == 'left':
            direction = changeDirction
        if changeDirction == 'up' and not direction == 'down':
            direction = changeDirction
        if changeDirction == 'down' and not direction == 'up':
            direction = changeDirction

        if direction == 'right':
            snakePosition[0] += 20  # snakePosition[0] = snakePosition[0] +20 snakePosition[0]是snakePosition数列中的第一个数字
        if direction == 'left':
            snakePosition[0] -= 20  # snakePosition[0] = snakePosition[0] -20
        if direction == 'up':
            snakePosition[1] -= 20  # snakePosition[1] = snakePosition[1] -20 snakePosition[1]是snakePosition数列中的第二个数字
        if direction == 'down':
            snakePosition[1] += 20  # snakePosition[1] = snakePosition[1] +20 snakePosition[1]是snakePosition数列中的第二个数字

        #判断是否咬到自己必须在增加蛇的长度之前
        for postion1 in snakeBody:
            if snakePosition[0]== postion1[0] and snakePosition[1] == postion1[1]:
                gameOver()

        #增加蛇的长度
        snakeBody.insert(0,list(snakePosition))
        #如果我们的贪吃蛇的位置和目标方块的位置重合
        if snakePosition[0] == targetPosition[0] and snakePosition[1] == targetPosition[1] :
            targetfalg = 0
            speed=speed+10
        else :
            snakeBody.pop()

        if targetfalg == 0:
            locationTF= True
            while locationTF:
                x = random.randrange(1,32)
                y = random.randrange(1,24)
                targetPosition=[int(x*20),int(y*20)]
                for postion2 in snakeBody:#判断新生成的点不在蛇身上
                    if snakePosition[0] != postion2[0] or snakePosition[1] != postion2[1]:
                        locationTF=False
            targetfalg =1
        # 填充背景颜色
        playSurface.fill(blackcolor)

        for postion in snakeBody:
            #画蛇
            pygame.draw.rect(playSurface,whitecolor,Rect(postion[0],postion[1],20,20))  #???
            #画目标方块
            pygame.draw.rect(playSurface,redcolor,Rect(targetPosition[0],targetPosition[1],20,20))
            #pygame.draw.rect(playSurface,redcolor,Rect(targetPosition[0],targetPosition[1],20,20)
            #第一个参数surface：指定一个surface编辑区，在这个区域内绘制，界面
            #第二个参数color 颜色
            #第三个参数 Rect：返回一个矩形（（x,y),(width，height））
            #第四个参数 width： 表示线条的粗细 width=0 填充 实心 width =1 空心
        # for postion1 in snakeBody:
        #
        #     if snakePosition[0]== postion1[0] and snakePosition[1] == postion1[1]:
        #         gameOver()


            #更新显示
            pygame.display.flip()
            #判断是否游戏结束
            if snakePosition[0]> 620 or snakePosition[0]<0:
                gameOver(playSurface)
            elif snakePosition[1]> 460 or snakePosition[1]<0:
                gameOver(playSurface)
            # for snakebody in snakeBody[1:]:
            #     if snakePosition[0] == snakebody[0] and snakePosition[1] == snakebody[1]:
            #         gameOver()

            #控制游戏速度
            fpsClock.tick(speed)

if __name__== '__main__':
    main()
