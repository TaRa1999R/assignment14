                        # MAIN PART OF GAME

import random
import arcade
from spaceship import Spaceship
from bullet import Bullet
from enemy import Enemy

class Game ( arcade.Window ) :
    def __init__ ( self ) :
        super().__init__ ( title = "INTERSTELLAR GAME" )
        arcade.set_background_color ( arcade.color.DARK_BLUE )
        self.background = arcade.load_texture ( ":resources:images/backgrounds/stars.png" )
        self.me = Spaceship ( self )
        self.enemy_list = []

    def on_draw ( self ) :
        arcade.start_render ()
        arcade.draw_lrwh_rectangle_textured ( 0 , 0 , self.width , self.height , self.background )
        self.me.draw ()
        for bullet in self.me.bullet_list :
            bullet.draw ()
        
        for enemy in self.enemy_list :
            enemy.draw ()

        arcade.finish_render ()
        
    def on_key_press ( self , symbol , modifiers ) :
        if symbol == arcade.key.LEFT or symbol == arcade.key.A :
            self.me.change_x = -1
        
        elif symbol == arcade.key.RIGHT or symbol == arcade.key.D :
            self.me.change_x = 1
        
        elif symbol == arcade.key.SPACE :
            self.me.fire ()

    def on_key_release ( self , symbol , modifiers ) :
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT :
            self.me.change_x = 0

    def on_update ( self , delta_time ) :
        self.me.move ()

        for bullet in self.me.bullet_list :
            bullet.move ()
        
        for enemy in self.enemy_list :
            enemy.move ()
#------------------------------------------------------------change
        i = random.randint ( 0 , 50 )
        if i == 10 :
            new_enemy = Enemy ( self )
            self.enemy_list.append ( new_enemy )
#-----------------------------------------------------------------

        for enemy in self.enemy_list :
            if arcade.check_for_collision ( self.me , enemy ) :
                print (" Game Over ")
                exit (0)

        for enemy in self.enemy_list :
            for bullet in self.me.bullet_list :
                if arcade.check_for_collision ( enemy , bullet ) :
                    self.enemy_list.remove ( enemy )
                    self.me.bullet_list.remove ( bullet )

        


window = Game ()
arcade.run ()