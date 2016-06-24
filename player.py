#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 26.5
COLOR = "#7cdbef"
JUMP_POWER = 10
GRAVITY = 0.35 # Сила которая удет тянуть наш прямоугольник


class Player(sprite.Sprite):
    """класс нашего прямоугольника"""
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  #скорость нашего прямоугольника, 0 стояние на месте
        self.startX = x #начальная позиция
        self.startY = y
        self.image = Surface((WIDTH, HEIGHT)) #его изображение
        self.image.fill(Color(COLOR)) #заливка цветом
        self.rect = Rect(x, y, WIDTH, HEIGHT) #прямоугольные объект
        self.yvel = 0 # скорость вертикального перемещения
        self.onGround = False # на земле ли я?


    def update(self, left, right, up):
        if up:
            if self.onGround: # прыгаем только тогда когда можно оттолкнуться от земли
                self.yvel = -JUMP_POWER


        if left:
            self.xvel = -MOVE_SPEED # Лево = x - n


        if right:
            self.xvel = MOVE_SPEED # Право = x + n


        if not(left or right): # Стоим когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += GRAVITY


        self.onGround = False; # мы не знаем когда мы на земле
        self.rect.y += self.yvel # переносим положение на yvel
        self.rect.x += self.xvel # переносим свое положение на xvel


    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))
