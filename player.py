#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *

MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 26.5
COLOR = "#7cdbef"


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


    def update(self, left, right):
        if left:
            self.xvel = -MOVE_SPEED # Лево = x - n


        if right:
            self.xvel = MOVE_SPEED # Право = x + n


        if not(left or right): # Стоим когда нет указаний идти
            self.xvel = 0


        self.rect.x += self.xvel # переносим свое положение на xvel


    def draw(self, screen): # Выводим себя на экран
        screen.blit(self.image, (self.rect.x,self.rect.y))
