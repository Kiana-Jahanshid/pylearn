import arcade
import random
import time
class Enemy(arcade.Sprite) :
     def __init__(self , w , h ):
          super().__init__(":resources:images/alien/alienBlue_front.png" )
          self.center_x = random.randint(0,w)
          self.center_y = h + 25
          self.height = 35
          self.width = 27
          self.speed = 0.6
          #self.collision_radius(20)


     def move(self) :
          self.center_y -= self.speed