                        # MAIN PART OF GAME

import time
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
        self.enemy_speed = 3
        self.timer = time.time ()


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
#---------------------------------------------------------------------------حرکت اجسام
        self.me.move ()

        for bullet in self.me.bullet_list :
            bullet.move ()
        
        for enemy in self.enemy_list :
            enemy.move ()
#-----------------------------------------------------------------------------حذف اجسام خارج شده از صفحه از لیست ها 
        for enemy in self.enemy_list :
            if enemy.center_y <= 0 :
                self.enemy_list.remove ( enemy )
        
        for bullet in self.me.bullet_list :
            if bullet.center_y >= self.height :
                self.me.bullet_list.remove ( bullet )
#-----------------------------------------------------------------------------زمان
        if time.time () >= self.timer + 3 :
            new_enemy = Enemy ( self , self.enemy_speed )
            self.enemy_list.append ( new_enemy )
            self.enemy_speed += 0.1
            self.timer = time.time ()
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------برخورد اجسام 
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