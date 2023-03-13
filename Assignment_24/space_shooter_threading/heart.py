import arcade 

class Heart(arcade.Sprite) :
    def __init__(self ):
        super().__init__("pics/love-always-wins.png")
        self.center_x = 0
        self.center_y = 25 
        self.height = 34
        self.width = 34
