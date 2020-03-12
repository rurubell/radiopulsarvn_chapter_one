image Midori_Sea_BG_Other = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Other.png"
image Midori_Sea_BG_Sky = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Sky.jpg"

image Midori_Sea_BG_Sea_Blinks_01 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Sea_Blinks_01.png"
image Midori_Sea_BG_Sea_Blinks_02 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Sea_Blinks_02.png"
image Midori_Sea_BG_Sea_Blinks_03 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Sea_Blinks_03.png"

image Midori_Sea_BG_Sea_Colors_01 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Sea_colors_01.png"
image Midori_Sea_BG_Sea_Colors_02 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Sea_colors_02.png"
image Midori_Sea_BG_Sea_Colors_03 = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Sea_colors_03.png"

image Midori_Sea_BG_Sea_Foam = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Sea_Foam.png"

image Midori_Sea_BG_Clouds = "./images/cg/DAY_01/01a_Green-Haired_Girl/Midori_Sea_BG/Clouds.png"


image Midori_Sea_BG:
    contains:
        "Midori_Sea_BG_Sky"
        
    contains:
        subpixel True
        xalign 0.0
        HBox( "Midori_Sea_BG_Clouds", "Midori_Sea_BG_Clouds" )
        linear 300.0 xpos -1.0
        repeat
        
    contains:
        "Midori_Sea_BG_Sea_Colors"
    
    contains:
        "Midori_Sea_BG_Other"
    
    #contains:
    #    "Midori_Sea_BG_Sea_Foam_Animated"
        
    contains:
        ypos 30
        "Midori_Sea_BG_Sea_Foam"
        
    contains:
        "Midori_Sea_BG_Sea_Blinks"


image Midori_Sea_BG_Sea_Foam_Animated:
    contains:
        "Midori_Sea_BG_Sea_Foam"
        pause 1.0
        ease 2.0 ypos 30
        pause 1.0
        ease 2.0 ypos 0
        repeat


image Midori_Sea_BG_Sea_Colors:
    contains:
        "Midori_Sea_BG_Sea_Colors_03"
        
    contains:
        "Midori_Sea_BG_Sea_Colors_01"
        linear 2.0 alpha 1.0
        linear 2.0 alpha 0.0
        repeat
        
    contains:
        "Midori_Sea_BG_Sea_Colors_02"
        linear 2.0 alpha 0.0
        linear 2.0 alpha 1.0
        repeat

image Midori_Sea_BG_Sea_Blinks:
    contains:
        "Midori_Sea_BG_Sea_Blinks_01"
        linear 2.0 alpha 1.0
        linear 2.0 alpha 0.0
        repeat
        
    contains:
        "Midori_Sea_BG_Sea_Blinks_02"
        linear 2.0 alpha 0.0
        linear 2.0 alpha 1.0
        repeat
