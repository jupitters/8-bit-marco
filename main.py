import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from sound import *
from ticket import *
from dialogs import *
class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.static_sprite = SpriteObject(self)
        self.object_handler = ObjectHandler(self)
        self.ticket = Ticket(self)
        self.inicio = AvisoInicial(self)

        self.dialogs = Dialogs(self)
        self.dialogsArte = DialogsArte(self)
        self.dialogsMundo = DialogsMundo(self)
        self.dialogsHistoria = DialogsHistoria(self)
        self.dialogsBrasil = DialogsBrasil(self)
        self.dialogsCriacoes = DialogsCriacoes(self)

        self.sound = Sound(self)
        pg.mixer.music.play(-1)

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.static_sprite.update()
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')

    def draw(self):
        self.object_renderer.draw()
        self.ticket.draw()
        self.inicio.draw()

        self.dialogs.draw()
        self.dialogsArte.draw()
        self.dialogsMundo.draw()
        self.dialogsHistoria.draw()
        self.dialogsBrasil.draw()
        self.dialogsCriacoes.draw()

        # self.map.draw()
        # self.player.draw()
    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.player.giving_ticket()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    game.run()