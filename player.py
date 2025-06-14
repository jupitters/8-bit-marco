from settings import *
import pygame as pg
from object_handler import *
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.holding_ticket = True
    
    def giving_ticket(self):
        if self.holding_ticket and (self.game.player.map_pos == (5, 4)):
            self.holding_ticket = False
            # self.game.object_handler.add_sprite(SpriteObject(self.game, path=self.game.object_handler.static_sprite_path + 'banner.png', pos=(5, 4.5), shift=0.08))

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pg.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pg.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pg.K_d]:
            dx += -speed_sin
            dy += speed_cos 

        self.check_wall_collision(dx, dy)

        # if keys[pg.K_LEFT]:
        #     self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        # if keys[pg.K_RIGHT]:
        #     self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau
    
    def draw(self):
        # draw for debug
        # pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100), (self.x * 100 + WIDTH * math.cos(self.angle), self.y * 100 + WIDTH * math.sin(self.angle)), 2)
        pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)
    
    def check_wall(self, x, y):
        if x == 4 and y == 3:
            return not self.holding_ticket
        else:
            return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def mouse_control(self):
            mx, my = pg.mouse.get_pos()
            if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
                pg.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
            self.rel, self.rely = pg.mouse.get_rel()
            self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
            self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)