import arcade 


class Bee(arcade.Sprite):
    def __init__(self , x , y):
        super().__init__(":resources:images/enemies/bee.png" )
        self.width = 47
        self.height = 47 
        self.center_x = x
        self.center_y = y

class Bug(arcade.Sprite):
    def __init__(self , x , y):
        super().__init__(":resources:images/enemies/ladybug.png")
        self.width = 47
        self.height = 47 
        self.center_x = x
        self.center_y = y

class Fish(arcade.Sprite):
    def __init__(self , x , y):
        super().__init__(":resources:images/enemies/fishPink.png")
        self.width = 48
        self.height = 48 
        self.center_x = x
        self.center_y = y

class Worm(arcade.Sprite):
    def __init__(self , x , y):
        super().__init__(":resources:images/enemies/wormGreen.png")
        self.width = 48
        self.height = 48 
        self.center_x = x
        self.center_y = y
 
