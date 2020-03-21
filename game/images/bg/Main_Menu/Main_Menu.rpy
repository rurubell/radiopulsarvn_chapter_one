image Main_Menu_other = "./images/bg/Main_Menu/other.png"
image Main_Menu_sky = "./images/bg/Main_Menu/sky.jpg"
image Main_Menu_sfx = "./images/bg/Main_Menu/sfx.png"
image Main_Menu_Logo = "./images/bg/Main_Menu/logo_jp.png"

image Main_Menu_flare_00 = "./images/bg/Main_Menu/screen_flare_00.png"
image Main_Menu_flare_01 = "./images/bg/Main_Menu/screen_flare_01.png"
image Main_Menu_flare_02 = "./images/bg/Main_Menu/screen_flare_02.png"


image Main_Menu_BG:
    contains:
        subpixel True
        xalign 0.0
        "Main_Menu_sky"
    
    contains:
        "Day_Right_To_Left_Jet"
    
    contains:
        "Day_Clouds"
    
    contains:
        "Main_Menu_other"
    
    contains:
        "Main_Menu_wires"
    
    contains:
        "Main_Menu_sfx"
        
        choice:
            linear 1 alpha 0.9
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
            
        choice:
            linear 1 alpha 0.8
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
        
        choice:
            linear 1 alpha 0.7
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
        
        choice:
            linear 1 alpha 0.6
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
        
        choice:
            linear 1 alpha 0.5
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
        
        pause 0.5
        repeat
    
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
        
    contains:
        "Main_Menu_Logo"
        alpha 0.9
