image Night_Street_01_Base = "./images/bg/Outdoor/Street_01/Night/Other.png"
image Night_Street_01_Sky = "./images/bg/Outdoor/Street_01/Night/Sky.jpg"

image Night_Street_01_TV = "./images/bg/Outdoor/Street_01/Night/tv.png"

image Night_Street_01_Window_Light_01 = "./images/bg/Outdoor/Street_01/Night/window_light_01.png"
image Night_Street_01_Window_Light_02 = "./images/bg/Outdoor/Street_01/Night/window_light_02.png"
image Night_Street_01_Window_Light_03 = "./images/bg/Outdoor/Street_01/Night/window_light_03.png"
image Night_Street_01_Window_Light_04 = "./images/bg/Outdoor/Street_01/Night/window_light_04.png"
image Night_Street_01_Window_Light_05 = "./images/bg/Outdoor/Street_01/Night/window_light_05.png"

image Night_Street_01_Street_Light_01 = "./images/bg/Outdoor/Street_01/Night/street_light_01.png"
image Night_Street_01_Street_Light_02 = "./images/bg/Outdoor/Street_01/Night/street_light_02.png"


image Night_Street_01_Street_Lights:
    contains:
        "Night_Street_01_Street_Light_01"
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            pause renpy.random.randint( 5, 20 )
            
        repeat
        
            
    contains:
        "Night_Street_01_Street_Light_02"
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.8
            pause renpy.random.uniform( 0.1, 0.3 )
            alpha 1.0
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            pause renpy.random.randint( 5, 20 )
        
        repeat


image Night_Street_01:
    contains:
        "Night_Street_01_Sky"
        
    contains:
         "Meteors"
    
    contains:
        "Night_Sky_Stars"
        
    contains:
        "Night_Jets_Right_To_Left"
    
    contains:
        "Night_Street_01_Base"
    
    contains:
        "Night_Street_01_Windows_Lights"
        
    contains:
        "Night_Street_01_TV_Animation"
    
    contains:
        "Night_Street_01_Street_Lights"


image Night_Street_01_TV_Animation:
    contains:
        "Night_Street_01_TV"
        
        choice:
            alpha 0.55
            pause renpy.random.uniform( 0.1, 0.5 )
        
        choice:
            alpha 0.5
            pause renpy.random.uniform( 0.1, 0.5 )
        
        choice:
            alpha 0.6
            pause renpy.random.uniform( 0.5, 0.6 )
        
        choice:
            alpha 0.55
            pause renpy.random.uniform( 0.1, 0.5 )

        choice:
            alpha 0.55
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.5
            pause renpy.random.uniform( 0.1, 0.3 )
        
        choice:
            alpha 0.6
            pause renpy.random.uniform( 0.5, 0.6 )
        
        choice:
            alpha 0.55
            pause renpy.random.uniform( 0.1, 0.3 )

        repeat


image Night_Street_01_Windows_Lights:
    contains:
        "Night_Street_01_Window_Light_01"
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        repeat

    contains:
        "Night_Street_01_Window_Light_02"
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        repeat

    contains:
        "Night_Street_01_Window_Light_03"
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        repeat

    contains:
        "Night_Street_01_Window_Light_04"
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        repeat

    contains:
        "Night_Street_01_Window_Light_05"
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 0.0
            pause renpy.random.randint( 5, 15 )
        
        choice:
            alpha 1.0
            pause renpy.random.randint( 5, 15 )
        
        repeat
