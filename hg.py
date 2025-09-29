import random
import pygame

pygame.init()

blue=(0, 0, 139)
black=(0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

dis_width = 800# переменные размера экрана
dis_height = 600# переменные размер экрана
display = pygame.display.set_mode((dis_width, dis_height))# соз экран
pygame.display.set_caption('Змейка Никита')# имя игры
def gameLoop():# функция с логикой игры, для перезапуска
    game_over = False #обозначение, проигрыша/выигрыша
    game_close = False#обозначение, вышел из программы или нет
    x1 = dis_width / 2# начальное расположение змейки
    y1 = dis_height / 2# начальное расположение змейки
    snake_block = 10#единица игры (размер змеи, яблока, перемещения)

    x1_change = 0#фиксация перемещения змейки на поле, чтобы потом передать изменения в x1
    y1_change = 0#фиксация перемещения змейки на поле, чтобы потом передать изменения в y1

    # еда
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0#местоположение змеи каждый раз будет меняться
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0#местоположение змеи каждый раз будет меняться
    clock = pygame.time.Clock()#скорость нашей игры, создание переменной, но не использование
    snake_speed = 15#скорость змеи
    font_style = pygame.font.SysFont('Arial', 30)#стиль шрифта надписей

    def message(msg, color):#функция для вывода сообщения
        mesg = font_style.render(msg, True, color)#создаем переменную для вывода сообщения
        display.blit(mesg, [dis_width / 2, dis_height / 2])#вывод сообщения на экран

    while not game_over:#пока не проиграли, выполняем игру
        while game_close == True:#пока закрыли игру
            display.fill(green)#фон делаем зеленым
            message("Вы проиграли :(, нажмите Q для выхода или С для повторной игры", red)#выводим сообщение
            pygame.display.update()#обновляем экран для вывода сообщения на экран
            for event in pygame.event.get():# создаем цикл фиксации нажатий пользователя
                if event.type == pygame.KEYDOWN:#если пользователь нажал на клавишу с клавиатуры
                    if event.key == pygame.K_c:#если он нажал на С
                        gameLoop()#перезапускаем игру
                    if event.key == pygame.K_q:#если нажал на Q
                        game_over = True#то проигрываем
                        game_close = False#и выходим из цикла while game_close == True

        #если не проиграли и не закрыли игру
        for event in pygame.event.get():#создаем цикл фиксации нажатий пользователя
            if event.type == pygame.QUIT:#если пользователь нажал на крестик
                game_over = True#проигрываем
            if event.type == pygame.KEYDOWN:#если пользователь нажал на клавишу с клавиатуры
                if event.key == pygame.K_LEFT:#если нажал на клавишу влево
                    x1_change = -snake_block#смешаемся по х
                    y1_change = 0#не смешаемся по у
                elif event.key == pygame.K_RIGHT:#если нажал на клавишу вправо
                    x1_change = snake_block#смешаемся по х
                    y1_change = 0#не смешаемся по у
                elif event.key == pygame.K_UP:#
                    x1_change = 0#
                    y1_change = -snake_block#
                elif event.key == pygame.K_DOWN:#
                    x1_change = 0#
                    y1_change = snake_block#
        if (x1 >= dis_width or x1 <= 0) or (y1 >= dis_height or y1 <= 0):#если пользователь вышел за границы экрана
            game_over = True#то он проиграл
        x1 += x1_change#фиксируем изменения в наши переменные, чтобы потом вывесли их на экран
        y1 += y1_change#фиксируем изменения в наши переменные, чтобы потом вывесли их на экран
        display.fill(blue)#заливаем фон синим цветм
        pygame.draw.rect(display, red, [food_x, food_y, snake_block, snake_block])#создаем еду красного цвета  в положении food_x, food_y, размером snake_block
        pygame.draw.rect(display, green, [x1, y1, snake_block, snake_block])#создаем змею зеленого цвета в положении x1, y1, размером snake_block
        pygame.display.update()#показываем изменения на экран
        clock.tick(snake_speed)#запускаем скорость нашей игры


    pygame.quit()#выходим из игры
    quit()#выходим из цикла
gameLoop()#запускаем нашу основную функцию