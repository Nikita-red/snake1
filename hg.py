import dis
import random

import pygame
import time

pygame.init()

blue=(0, 0, 139)#цвет фона
black=(0, 0, 0)#цвет фона
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

dis_width = 800
dis_height = 600
display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Змейка Никита')
def gameLoop():
    game_over = False
    game_close = False
    x1 = dis_width / 2  # начальная координата
    y1 = dis_height / 2  # начальная координата
    snake_block = 10

    x1_change = 0  # на сколько изменится наша координата
    y1_change = 0  # на сколько изменится наша координата

    # еда
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    clock = pygame.time.Clock()  # скорость нашей игрв
    snake_speed = 15
    font_style = pygame.font.SysFont('Arial', 30)

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        display.blit(mesg, [dis_width / 2, dis_height / 2])

    while not game_over:
        while game_close == True:
            display.fill(green)
            message("Вы проиграли :(, нажмите Q для выхода или С для повторной игры", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        if (x1 >= dis_width or x1 <= 0) or (y1 >= dis_height or y1 <= 0):
            game_over = True
        x1 += x1_change
        y1 += y1_change
        display.fill(blue)
        pygame.draw.rect(display, white, [food_x, food_y, snake_block, snake_block])
        pygame.draw.rect(display, black, [x1, y1, snake_block, snake_block])
        pygame.display.update()
        clock.tick(snake_speed)


    pygame.quit()
    quit()
gameLoop()