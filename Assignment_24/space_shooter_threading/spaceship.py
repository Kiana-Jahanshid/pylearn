import arcade 
from bullet import Bullet

class Spaceship(arcade.Sprite) :
    def __init__(self ,w  , name):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.center_x = w // 2
        self.center_y = 80
        self.height = 36
        self.width = 35
        self.name  = name 
        self.speed = 7
        self.change_x = 0
        self.change_y = 0
        self.game_width = w 
        self.bullet_list =[]

    def move(self ) :
        if self.change_x == -1 :
            if self.center_x > 0 :
                self.center_x -= self.speed 
        
        elif self.change_x  == 1 :
            if self.center_x < self.game_width :
                self.center_x += self.speed


    def fire(self):
        new_bullet = Bullet(self)
        self.bullet_list.append(new_bullet)