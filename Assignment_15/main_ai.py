import random 
import arcade
from snake import Snake
from apple import Apple
from pear import Pear 
from onion import Onion
import math

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width= 500 , height=500 , title="Snake")
        #self.background = arcade.load_texture("Assignment_15/bg.jpg" )
        arcade.set_background_color(arcade.color.GENERIC_VIRIDIAN)
        self.apple = Apple(self) 
        self.pear  = Pear(self)        
        self.snake = Snake(self)
        self.onion = Onion(self)
        self.flag = 1

    def on_draw(self):
        arcade.start_render()
        self.snake.mydraw()
        self.apple.draw()
        self.pear.draw()
        self.onion.draw()
        arcade.draw_text(f"Score : {self.snake.score}", 390, 15, arcade.color.WHITE, font_size= 17 ,font_name= 'arial', bold=True)
        if self.flag == 0 :
            arcade.draw_text("Game Over", 20 , 210  , arcade.color.RED , 80 ,  bold=True)



    def on_key_press(self , symbol : int , modifiers : int):
        if symbol == arcade.key.UP or symbol == arcade.key.W :
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D :
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif symbol == arcade.key.DOWN or symbol == arcade.key.S :
            self.snake.change_x = 0
            self.snake.change_y = -1 

    
    def on_update(self, delta_time : float) :


        x_difference_as =float(self.snake.center_x  - self.apple.center_x )
        y_difference_as =float(self.snake.center_y - self.apple.center_y )
        x_difference_ps =float(self.snake.center_x  - self.pear.center_x )
        y_difference_ps =float(self.snake.center_y - self.pear.center_y  ) 
        
        snake_apple_dist = math.hypot(x_difference_as, y_difference_as)
        snake_pear_dist = math.hypot(x_difference_ps , y_difference_ps)
        
        if snake_apple_dist < snake_pear_dist:
            snake_choice = self.apple
        else : 
            snake_choice = self.pear

        if  snake_choice.center_x > self.snake.center_x \
            and self.snake.change_x != -1 :
            self.snake.change_x = 1 
            self.snake.change_y = 0 
        elif snake_choice.center_x < self.snake.center_x \
            and self.snake.change_x != 1 :
            self.snake.change_x =  -1
            self.snake.change_y =  0
        elif snake_choice.center_y < self.snake.center_y \
            and self.snake.change_y != 1  : 
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif snake_choice.center_y > self.snake.center_y \
            and self.snake.change_y != -1   :
            self.snake.change_x = 0
            self.snake.change_y = 1
            

        self.snake.move()
        if arcade.check_for_collision(self.snake , self.apple ):
            self.snake.eat_apple(self.apple)
            self.apple = Apple(self)

        if arcade.check_for_collision(self.snake , self.pear ):
            self.snake.eat_pear(self.pear)
            self.pear = Pear(self)

        if arcade.check_for_collision(self.snake , self.onion ):
            self.snake.eat_onion(self.onion)
            self.onion = Onion(self)

        # GAME OVER IN CASE OF GAME BORDER COLLISION
        if self.snake.center_x <-10 or self.snake.center_y < -10 or self.snake.center_x >self.width+10  or self.snake.center_y > self.height+10:
            self.flag = 0

        # GAME OVER IN CASE OF SELF BODY COLLISION
        # for i in range(0 , len(self.snake.body)-1 ):
        #     if arcade.check_for_collision(self.snake , self.snake.body[i]):
        #         self.flag = 0

        # GAME OVER IN CASE OF NEGATIVE SCORE 
        if self.snake.score == 0 and len(self.snake.body)>0 : 
            self.flag = 0        


window = Game()
arcade.run()