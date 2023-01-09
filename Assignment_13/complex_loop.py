import arcade

col_space = 27
row_space = 27
left_padding = 115
bottom_padding = 115

arcade.open_window(470, 470, "Complex Loops")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

for row in range(10):
    for column in range(10):
        x = left_padding + column * col_space 
        y = bottom_padding + row * row_space 
        if row % 2 == 0 :
            if column % 2 == 0 :
                arcade.draw_rectangle_filled(x, y, 14 , 14, arcade.color.WHITE , tilt_angle=45)
            else :
                arcade.draw_rectangle_filled(x, y, 14 , 14, arcade.color.RED , tilt_angle=45)
        else :
            if column % 2 == 0 :
                arcade.draw_rectangle_filled(x, y, 14 , 14, arcade.color.RED , tilt_angle=45)
            else :
                arcade.draw_rectangle_filled(x, y, 14 , 14, arcade.color.WHITE , tilt_angle=45)


arcade.finish_render()
arcade.run()