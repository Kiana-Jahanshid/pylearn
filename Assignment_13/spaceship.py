import random 
import arcade 

class Spaceship(arcade.Sprite) :
     def __init__(self ,w ):
         super().__init__(":resources:images/space_shooter/playerShip1_green.png")
         self.center_x = w // 2
         self.center_y = 80
         self.height = 50
         self.width = 50
         self.speed = 5


class Enemy(arcade.Sprite) :
    def __init__(self , w , h):
         super().__init__(":resources:images/alien/alienBlue_front.png")
         self.center_x = random.randint(0,w)
         self.center_y = h + 25
         self.height = 55
         self.width = 40
         self.speed = 2


class Rock(arcade.Sprite):
    def __init__(self  , h):
         super().__init__(":resources:images/space_shooter/meteorGrey_big1.png")
         self.center_x = 0
         self.center_y = 90
         self.height = 50
         self.width = 50
         self.speed = 1

class Game(arcade.Window) :
    def __init__(self):
        super().__init__(width= 600 , height= 600 , title= "Interstellar Game")
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture("Assignment_13/IrF.gif")
        self.me = Spaceship(self.width)
        self.enemy = Enemy(self.width , self.height)
        self.rock = Rock(self.height)

    #show
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width  , self.height  , self.background)
        self.me.draw()
        self.enemy.draw()
        self.rock.draw()


    def on_key_press(self  , symbol :int , modifiers :int ):
        print("a key has been pressed")
        print(symbol)
        if symbol == 65363 : #right key on keyboard
            self.me.center_x += self.me.speed
        elif symbol == 65361: #left key 
            self.me.center_x -= self.me.speed
        elif symbol == 65362 : #up key
            self.me.center_y += self.me.speed
        elif symbol == 65364 : #down key
            self.me.center_y -= self.me.speed


    def on_update(self , delta_time : float):
        self.enemy.center_y -= self.enemy.speed
        self.rock.center_x += self.rock.speed
        self.rock.center_y += self.rock.speed

window = Game()
arcade.run()