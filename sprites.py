import pygame as pg
from config import *
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pg.image.load(file).convert_alpha()

    def get_sprite(self, x, y, width, height):
        sprite = pg.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x,y,width,height))
        sprite.set_colorkey(YELLOW)
        return sprite


class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.x_change = 0
        self.y_change = 0
        self.facing = 'right'
        self.jump = False
        self.up_v = 0
        self.pressed = False

        self.image = self.game.character_spritesheet.get_sprite(0,0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        

    def update(self):
        self.movement()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pg.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'

        if keys[pg.K_UP]:
            self.jump = True
            if self.pressed is False:
                self.up_v = JUMP_SPEED
            self.pressed = True
        
        if self.jump is True:
            self.y_change -= self.up_v
            self.up_v-=GRAVITY
            #temperary setup, in future, if it has a collision with anything
            if self.up_v<=(JUMP_SPEED*-1):
                self.y_change = 0
                self.jump = False
                self.up_v = 0
                self.pressed = False
            

class Block(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pg.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE


        self.image = self.game.terrain_spritesheet.get_sprite(0,0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


