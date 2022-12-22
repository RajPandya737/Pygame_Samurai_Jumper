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
        self.font = pg.font.Font('assets/sprites/Minecraft.ttf', 32)
        self.running = True
        self.character_spritesheet = Spritesheet('assets/sprites/Samurai_Sprites.png')
        self.terrain_spritesheet = Spritesheet('assets//template/Terrain_Sprites.jpg')
        self.bg = pg.image.load('assets/template/background.jpg').convert()
        self.intro_background = pg.image.load('assets/template/SamuraiJumperOP.png').convert()

    def createTilemap(self):
        #displays the tiles according to the map written in the config file
        for i , row in enumerate(tilemap):
            for j, col in enumerate(row):
                if col == 'B' or col == 'G' or col == 'S':
                    Block(self, j, i)
                if col == 'P':
                    Player(self, j, i)

    def new(self):
        #When a new game starts
        self.playing = True
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.blocks = pg.sprite.LayeredUpdates()
        self.createTilemap()
    
    def events(self):
        #gets key presses
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        #draws characters and other sprites on screen
        self.SCREEN.blit(self.bg, (0,0))
        self.all_sprites.draw(self.SCREEN)
        self.clock.tick(FPS)
        pg.display.update()

    def main(self):
        #runs the game
        while self.playing is True:
            self.events()
            self.update()
            self.draw()
        self.running = False
            



if __name__ == '__main__':
    game = Game()
    game.new()
    while game.running:
        game.main()

    pg.quit()
    exit()

