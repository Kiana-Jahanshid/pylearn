import random 
import arcade 

class Ninja(arcade.Sprite) :
     def __init__(self ,w ):
         super().__init__("Assignment_13/images/ninja.png")
         self.center_x = 580
         self.center_y = 140
         self.height = 105
         self.width = 100
         self.speed = 5

class Dragon(arcade.Sprite) :
    def __init__(self , w , h):
         super().__init__("Assignment_13/images/final-boss (1).png")
         global x
         self.center_x = random.randint(0,w)
         self.center_y = 500
         self.height = 130
         self.width = 110
         self.speed = 0.5
         x = self.center_x

class Rock(arcade.Sprite):
    def __init__(self  , h):
         super().__init__(":resources:images/space_shooter/meteorGrey_big1.png")
         self.center_x = 0
         self.center_y = 90
         self.height = 50
         self.width = 50
         self.speed = 0.3

class Rock2(arcade.Sprite):
    def __init__(self  , h):
         super().__init__(":resources:images/space_shooter/meteorGrey_big1.png")
         self.center_x = 700
         self.center_y = 400
         self.height = 30
         self.width = 30
         self.speed = 0.2
         self.angle = 45

class Fire(arcade.Sprite):
    def __init__(self  , h):
         super().__init__("Assignment_13/images/fire.png")
         self.center_x = x
         self.center_y = 500
         self.height = 35
         self.width = 45
         self.speed = 0.6

class Game(arcade.Window) :
    def __init__(self):
        super().__init__(width= 1100 , height= 500 , title= "DRAGON FIGHT")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("Assignment_13/images/—Pngtree—rock background of cartoon mountains_1591283.png")
        self.ninja = Ninja(self.width)
        self.dragon = Dragon(self.width , self.height)
        self.rock = Rock(self.height)
        self.rock2 = Rock2(self.height)
        self.fire = Fire(self.height)


    #show
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width  , self.height  , self.background)
        self.ninja.draw()
        self.dragon.draw()
        self.rock.draw()
        self.rock2.draw()
        self.fire.draw()


    def on_key_press(self  , symbol :int , modifiers :int ):
        print("a key has been pressed")
        print(symbol)
        if symbol == 65363 : #right key on keyboard
            self.ninja.center_x += self.ninja.speed
        elif symbol == 65361: #left key 
            self.ninja.center_x -= self.ninja.speed
        elif symbol == 65362 : #up key
            self.ninja.center_y += self.ninja.speed
        elif symbol == 65364 : #down key
            self.ninja.center_y -= self.ninja.speed


    def on_update(self , delta_time : float):
        self.dragon.center_y -= self.dragon.speed
        self.rock.center_x += self.rock.speed
        self.rock.center_y += self.rock.speed
        self.rock2.center_x -= self.rock2.speed
        self.rock2.center_y -= self.rock2.speed
        self.fire.center_x += self.fire.speed
        self.fire.center_y -= self.fire.speed

window = Game()
arcade.run()