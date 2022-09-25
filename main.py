import pygame as pg
from config import *
from sprites import *
from sys import exit

class Game:
    def __init__(self):
        #Initialise the screen and basic functions
        pg.init()
        self.SCREEN = pg.display.set_mode((WIDTH, HEIGHT))
        self.caption = pg.display.set_caption('Samurai Jumper')
        self.clock = pg.time.Clock()
        #self.font = pg.font.Font('Ariel', 32)
        self.running = True

    def new(self):
        #When a new game starts
        self.playing = True
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.blocks = pg.sprite.LayeredUpdates()
        self.player = Player(self, 5,30)
    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False
    def update(self):
        self.all_sprites.update()
    def draw(self):
        self.SCREEN.fill((0,0,0))
        self.all_sprites.draw(self.SCREEN)
        self.clock.tick(FPS)
        pg.display.update()

    def main(self):
        while self.playing is True:
            self.events()
            self.update()
            self.draw()
        self.running = False
            
    def game_over(self):
        pass

    def intro_screen(self):
        pass




if __name__ == '__main__':
    game = Game()
    game.intro_screen
    game.new()
    while game.running:
        game.main()
        game.game_over()

    pg.quit()
    exit()

