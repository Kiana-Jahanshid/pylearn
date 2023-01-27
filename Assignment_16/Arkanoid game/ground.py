import arcade


class Ground(arcade.Sprite):
    def __init__(self , game):
        super().__init__(":resources:images/tiles/grassHalf.png")
        self.width = 120
        self.height = 50 
        self.center_x = game.width // 2
        self.center_y = game.height // 2 - 250
        self.speed = 3
        self._set_collision_radius(60)

    def move(self ,game ,  frog):
        if frog.center_y < game.height// 2 +50:
            if self.center_x > frog.center_x :
                self.change_x = -1 
            if self.center_x < frog.center_x :
                self.change_x = 1

            self.center_x += self.change_x * self.speed 

            if self.center_x < 50 :
                self.center_x  = 50
            if self.center_x > game.width - 50 :
                self.center_x = game.width - 50 