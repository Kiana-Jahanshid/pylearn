import random 
import arcade 
from spaceship import Spaceship
from enemy import Enemy
from heart import Heart
import time
import threading

class Game(arcade.Window) :
    def __init__(self):
        super().__init__(width= 600 , height= 600 , title= "Interstellar Game")       
        self.background = arcade.load_texture("pics/space1.jpg" )
        self.Bullet_sound = arcade.load_sound("q.wav")
        self.explosion_sound = arcade.load_sound("ex.wav")
        self.me = Spaceship(self.width , "arc")
        self.enemies = [] 
        self.hearts = []
        self.score  = 0 
        self.game_over = False
        self.last_enemy_entrance = 0.0
        self.enemy_entrance_period = 3.0
        self.inc = 0.2

        new_heart = Heart()
        self.hearts.append(new_heart)
        new_heart.center_x += 25
        new_heart1 = Heart()
        self.hearts.append(new_heart1)
        new_heart1.center_x += 55
        new_heart2 = Heart()
        self.hearts.append(new_heart2)
        new_heart2.center_x += 85

        self.mythread = threading.Thread(target= self.create_enemy)
        self.mythread.start()
        

    #show
    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width  , self.height  , self.background)
        self.me.draw()
        
        for enemy in self.enemies :
            enemy.draw()
            
        for bullet in self.me.bullet_list :
            bullet.draw()
            
        for heart in self.hearts :          
            heart.draw()
            if self.game_over == True :
                self.clear()
                self.background = arcade.load_texture("pics/game-over (2).png")
                arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width  , self.height  , self.background)

        arcade.draw_text(f"Score : {self.score}", 460, 20, arcade.color.WHITE, 17 ,font_name= 'arial', bold=True)


    def on_key_press(self  , symbol :int , modifiers :int ):
        print(symbol)
        if symbol == arcade.key.RIGHT  or symbol == arcade.key.D : 
            self.me.change_x = 1
        elif symbol == arcade.key.LEFT  or symbol == arcade.key.A:  
            self.me.change_x = -1
        elif symbol == arcade.key.DOWN :
            self.me.change_x = 0
        elif symbol == arcade.key.F  or symbol ==  arcade.key.SPACE :
            self.me.fire()
            arcade.play_sound(self.Bullet_sound  , volume =0.1 )



    def on_key_release(self , symbol : int , modifiers : int) :
        self.me.change_x = 0



    def on_update(self , delta_time : float = 1/60 ): 
        
        for enemy in self.enemies :
             if arcade.check_for_collision(self.me , enemy ) :
                 self.game_over = True
                 print("GAME OVER")
                 exit(0)

        for enemy in self.enemies :
            for bullet in self.me.bullet_list :
                if arcade.check_for_collision(enemy , bullet )  :
                    self.enemies.remove(enemy)
                    arcade.play_sound(self.explosion_sound , volume= 0.3 )
                    self.me.bullet_list.remove(bullet)
                    self.score += 1

        self.me.move()

        for enemy in self.enemies :
            enemy.move()
            
        for bullet in self.me.bullet_list :
            bullet.move()
        
        index = 0 
        if len(self.hearts) != 0 :
            for enemy in self.enemies :
                if enemy.center_y <= 0 :
                    self.enemies.remove(enemy)
                    self.hearts.remove(self.hearts[index])               
                    index += 1
        
        elif len(self.hearts) == 0 :
            self.clear()
            GameOverView()          
            self.background = arcade.load_texture("pics/game-over (2).png")           
            arcade.draw_lrwh_rectangle_textured(0 , 0 , self.width  , self.height  , self.background)                        

        #self.last_enemy_entrance += delta_time
        #if self.last_enemy_entrance >= self.enemy_entrance_period:
            #self.last_enemy_entrance = 0
            # self.new_enemy = Enemy(self.width , self.height )
            # self.enemies.append(self.new_enemy)
            # self.new_enemy.speed = self.new_enemy.speed + self.inc
            # self.inc += 0.1

    def create_enemy(self):
        while True :
            self.new_enemy = Enemy(self.width , self.height )
            self.enemies.append(self.new_enemy)            
            time.sleep(3)


class GameOverView(arcade.View): 
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("pics/game-over (2).png")
        arcade.set_viewport(0, 600 - 1, 0, 600 - 1)

    def on_draw(self , Game):
        arcade.start_render()
        self.texture.draw_sized(600/2, 600/2, 600, 600)

    def on_update(self, delta_time):
        view = GameOverView()
        self.window.show_view(view)         



window = Game()
arcade.run()
over = GameOverView()