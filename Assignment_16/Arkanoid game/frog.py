import arcade
import random

class Frog(arcade.Sprite) :
    def __init__(self ,game ):
        super().__init__("pics/frog.png")#
        #self.color = arcade.color.WHITE 
        #self.radius = 10
        self.width =  50#self.radius * 2
        self.height = 50 #self.radius * 2
        self.center_x = game.width // 2 
        self.center_y = game.height// 2 -180
        self.change_x = random.choice([-1 , 1])
        self.change_y = random.choice([-1 , 1])
        self.speed = 3
        self._set_collision_radius(1)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed 
