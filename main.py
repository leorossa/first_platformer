#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Импортируем библиотеку pygame
import pygame
from pygame import *


#Объявляем переменные
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) #группа для обозначения дисплея
BACKGROUND_COLOR = "#f3f2f3"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"


def main():
    pygame.init()# инициация PyGame, обязательная строка
    screen = pygame.display.set_mode(DISPLAY)# Создаем окно
    pygame.display.set_caption("Very white") # пишем шапку
    bg = Surface((WIN_WIDTH, WIN_HEIGHT)) # Создание видимой поерхности
                                          # будем использовать как фон
    bg.fill(Color(BACKGROUND_COLOR))      # заливаем поверхность сплошным цветом


    level = [
       "----------------------------------",
       "-                                -",
       "-                       --       -",
       "-                                -",
       "-            --                  -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                   ----     --- -",
       "-                                -",
       "--                               -",
       "-                                -",
       "-                            --- -",
       "-                                -",
       "-                                -",
       "-      ---                       -",
       "-                                -",
       "-   -------         ----         -",
       "-                                -",
       "-                         -      -",
       "-                            --  -",
       "-                                -",
       "-                                -",
       "----------------------------------"]
    x=y=0 # координаты
    for row in level: # вся строка
        for col in row: # каждый символ
            if col == "-":
                pf = Surface((PLATFORM_WIDTH,PLATFORM_HEIGHT))
                pf.fill(Color(PLATFORM_COLOR))
                screen.blit(pf,(x,y))

            x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT    #то же самое и с высотой
        x = 0                   #на каждой новой строчке начинаем с нуля
    while 1: #основной цикл программы
        for e in pygame.event.get(): #обрабатываем события
            if e.type == QUIT:
                raise SystemExit, "QUIT"
        screen.blit(bg, (0,0))  #каждую итерацию необходимо все перерисовывать
        pygame.display.update() #обновление и вывод всех изменений на экран


if __name__ == '__main__':
    main()
