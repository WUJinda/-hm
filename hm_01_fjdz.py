import pygame
from plane_sprites import *  # *是通配符 ， 表示所有
# 使用from导入工具不需要.调用

# 游戏的初始化
pygame.init()
# 绘制游戏窗口
screen = pygame.display.set_mode((480, 700))

# 加载游戏背景图片
img_bg = pygame.image.load("C:\\Users\\DAREWIN\\PycharmProjects\\TCS\\images\\background.png")
screen.blit(img_bg, (0, 0))

# 加载英雄飞机图片
img_hero1 = pygame.image.load("./images/me1.png")
# screen.blit(img_hero1, (100, 500))

# 更新游戏绘制
pygame.display.update()
# 创建一个时钟对象
clock = pygame.time.Clock()

# 定义Rect记录飞机的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机的精灵
enemy = GameSprite("./images/enemy1.png")

# 创建敌机的精灵组
enemy_group = pygame.sprite.Group(enemy)

# 游戏循环 -> 游戏的开始
while True:
    # 指定循环内部代码执行频率
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Quit game..")

            pygame.quit()

            exit() # 终止当前程序
    # 修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y <= -int(hero_rect.height):
        hero_rect.y = 700
    screen.blit(img_bg, (0, 0))
    screen.blit(img_hero1, hero_rect)

    # 精灵组的update and draw 方法
    enemy_group.update()  # 让组中的所有精灵更新位置
    enemy_group.draw(screen)  # 绘制所有敌机
    pygame.display.update()


pygame.quit()
