image Cats_Paw_Shrine_Stairs_stairs = "images/cg/DAY_03/Cats_Paw_Shrine_Stairs/stairs.png"
image Cats_Paw_Shrine_Stairs_tower = "images/cg/DAY_03/Cats_Paw_Shrine_Stairs/tower.png"
image Cats_Paw_Shrine_Stairs_grass_01 = "images/cg/DAY_03/Cats_Paw_Shrine_Stairs/grass_01.png"
image Cats_Paw_Shrine_Stairs_grass_02 = "images/cg/DAY_03/Cats_Paw_Shrine_Stairs/grass_02.png"
image Cats_Paw_Shrine_Stairs_bg = "images/cg/DAY_03/Cats_Paw_Shrine_Stairs/bg.png"
image Cats_Paw_Shrine_Stairs_Sky = "images/cg/DAY_03/Cats_Paw_Shrine_Stairs/Sky.png"


image Cats_Paw_Shrine_Stairs_border_01_right_moved:
    contains:
        "border_01_right"
        xpos 1000
    
image Cats_Paw_Shrine_Stairs_border_01_right_mask_moved:
    contains:
        "border_01_right_mask"
        xpos 1000
        
image Cats_Paw_Shrine_Stairs_Masked = AlphaMask( "Cats_Paw_Shrine_Stairs_CG", "Cats_Paw_Shrine_Stairs_border_01_right_mask_moved" )
    

#Мини цгха - анимированные ступени подъема в гору до храма, показывается справа ( show Cats_Paw_Shrine_Stairs_With_Border_01 with ... )
image Cats_Paw_Shrine_Stairs_With_Border_01:
    contains:
        "Cats_Paw_Shrine_Stairs_Masked"
    contains:
        "Cats_Paw_Shrine_Stairs_border_01_right_moved"




init python:
    import math
    
    #y_start_pos - стартовая позиция башни-фанаря по вертикали
    #x_triangle_leg_lenght - катет, или длинна перемещения башни по горизонтали
    #triangle_angle - угол перемещения башни
    def Cats_Paw_Shrine_Stairs_tower_y_move_func( y_start_pos, x_triangle_leg_lenght, triangle_angle ):
        return int( y_start_pos + ( x_triangle_leg_lenght * ( math.tan( math.radians( triangle_angle ) ) ) ) )



image Cats_Paw_Shrine_Stairs_CG:
    contains:
        "Cats_Paw_Shrine_Stairs_Sky"
        
    contains:
        "Cats_Paw_Shrine_Stairs_bg"

    contains:
        "Cats_Paw_Shrine_Stairs_grass_02"
        xpos 150
        ypos 150
        linear 3 ypos 206 xpos 63
        repeat

    contains:
        "Cats_Paw_Shrine_Stairs_grass_01"
        xpos 200
        ypos 200
        linear 1.5 ypos 256 xpos 113
        repeat

    contains:
        "Cats_Paw_Shrine_Stairs_tower"
        xpos 1920
        ypos -50
        linear 5 xpos ( 1920 - 400 ) ypos Cats_Paw_Shrine_Stairs_tower_y_move_func( -50.0, 400.0, 32.7 )
        repeat
        
    contains:
        "Cats_Paw_Shrine_Stairs_tower"
        xpos 1520
        ypos 206
        linear 5 xpos ( 1520 - 400 ) ypos Cats_Paw_Shrine_Stairs_tower_y_move_func( 206.0, 400.0, 32.7 )
        repeat
        
    contains:
        "Cats_Paw_Shrine_Stairs_tower"
        xpos 1120
        ypos 462
        linear 5 xpos ( 1120 - 400 ) ypos Cats_Paw_Shrine_Stairs_tower_y_move_func( 462.0, 400.0, 32.7 )
        repeat
    
    contains:
        "Cats_Paw_Shrine_Stairs_stairs"
        xpos 200
        ypos 200
        linear 1 ypos 256 xpos 113
        repeat
