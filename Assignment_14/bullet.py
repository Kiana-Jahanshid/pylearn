import arcade
class Bullet(arcade.Sprite) :
    def __init__(self , host):
        super().__init__(":resources:images/space_shooter/laserRed01.png")
        self.center_x = host.center_x
        self.center_y = host.center_y
        self.speed = 10
        self.change_x = 0
        self.center_y = 85


    def move(self) :
        self.center_y += self.speed 
