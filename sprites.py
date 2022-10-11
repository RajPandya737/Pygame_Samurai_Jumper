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

        self.frame = 0
        

    def update(self):
        self.movement()
        self.animate()
        self.collide_blocks_y()
        self.rect.y += self.y_change
        self.collide_blocks_x()
        self.rect.x += self.x_change

        self.x_change = 0
        self.y_change = 0
        
    def movement(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x+=PLAYER_SPEED
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pg.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x-=PLAYER_SPEED
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


    def collide_blocks_y(self):
        hits = pg.sprite.spritecollide(self, self.game.blocks, False)
        if hits:
            if self.y_change > 0:
                self.rect.y = hits[0].rect.top - self.rect.height
                self.y_change = 0
                self.jump = False
                self.up_v = 0
                self.pressed = False
            if self.y_change < 0:
                self.rect.y = hits[0].rect.bottom


    def collide_blocks_x(self):
        
        hits = pg.sprite.spritecollide(self, self.game.blocks, False)
        if hits and self.jump is False:
            if self.x_change > 0:
                self.rect.x = hits[0].rect.left - self.rect.width

            if self.x_change < 0 :
                self.rect.x = hits[0].rect.right


    def animate(self):
        left = [self.game.character_spritesheet.get_sprite(0,0, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(0,80, self.width, self.height),
                    self.game.character_spritesheet.get_sprite(160,0, self.width, self.height) ]
        right = [self.game.character_spritesheet.get_sprite(80,0, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(80,80, self.width, self.height), 
                    self.game.character_spritesheet.get_sprite(160,80, self.width, self.height)]
        if self.jump is True and self.facing == 'left':
            self.image = left[2]
        elif self.jump is True and self.facing == 'right':
            self.image = right[2]
        elif self.facing == 'left':
            if self.x_change == 0:
                self.image = left[0]
            else:
                self.image = left[self.frame]
                if self.frame == 0:
                    self.frame = 1
                else:
                    self.frame = 0
        elif self.facing == 'right':
            if self.x_change == 0:
                self.image = right[0]
            else:
                self.image = right[self.frame]
                print(self.frame)
                if self.frame == 0:
                    self.frame = 1
                else:
                    self.frame = 0


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


