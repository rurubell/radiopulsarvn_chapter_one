image Main_Menu_other = "./images/bg/Main_Menu/other.png"
image Main_Menu_sky = "./images/bg/Main_Menu/sky.jpg"
image Main_Menu_clouds = "./images/bg/Main_Menu/clouds.png"
image Main_Menu_sub_clouds = "./images/bg/Main_Menu/sub_clouds.png"
image Main_Menu_sfx = "./images/bg/Main_Menu/sfx.png"

image Main_Menu_flare_00 = "./images/bg/Main_Menu/screen_flare_00.png"
image Main_Menu_flare_01 = "./images/bg/Main_Menu/screen_flare_01.png"
image Main_Menu_flare_02 = "./images/bg/Main_Menu/screen_flare_02.png"


image Main_Menu_BG:
    contains:
        subpixel True
        xalign 0.0
        "Main_Menu_sky"
    
    contains:
        "Right_To_Left_Jet"
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Main_Menu_sub_clouds", "Main_Menu_sub_clouds" )
        linear 1200.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Main_Menu_clouds", "Main_Menu_clouds" )
        linear 600.0 xpos -1.0
        repeat
    
    contains:
        "Main_Menu_wires"
    
    contains:
        "Main_Menu_other"
    
    contains:
        choice:
            alpha 0.0
            "Main_Menu_flare_00"
            linear renpy.random.randint( 1, 5 ) alpha 0.2
            linear renpy.random.randint( 1, 5 ) alpha 0.0
        
        choice:
            alpha 0.0
            "Main_Menu_flare_00"
            linear renpy.random.randint( 1, 5 ) alpha 0.2
            linear renpy.random.randint( 1, 5 ) alpha 0.0
        
        choice:
            alpha 0.0
            "Main_Menu_flare_00"
            linear renpy.random.randint( 1, 5 ) alpha 0.2
            linear renpy.random.randint( 1, 5 ) alpha 0.0
        
        repeat
    
    contains:
        choice:
            alpha 0.0
            "Main_Menu_flare_01"
            linear renpy.random.randint( 1, 10 ) alpha 0.2
            linear renpy.random.randint( 1, 10 ) alpha 0.0
        
        choice:
            alpha 0.0
            "Main_Menu_flare_01"
            linear renpy.random.randint( 1, 10 ) alpha 0.2
            linear renpy.random.randint( 1, 10 ) alpha 0.0
        
        choice:
            alpha 0.0
            "Main_Menu_flare_01"
            linear renpy.random.randint( 1, 10 ) alpha 0.2
            linear renpy.random.randint( 1, 10 ) alpha 0.0
        
        repeat
    
    contains:
        choice:
            alpha 0.0
            "Main_Menu_flare_02"
            linear renpy.random.randint( 1, 10 ) alpha 0.2
            linear renpy.random.randint( 1, 10 ) alpha 0.0
        
        choice:
            alpha 0.0
            "Main_Menu_flare_02"
            linear renpy.random.randint( 1, 10 ) alpha 0.2
            linear renpy.random.randint( 1, 10 ) alpha 0.0
        
        choice:
            alpha 0.0
            "Main_Menu_flare_02"
            linear renpy.random.randint( 1, 10 ) alpha 0.2
            linear renpy.random.randint( 1, 10 ) alpha 0.0
        
        repeat
