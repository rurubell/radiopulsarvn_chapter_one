image Sea_Midori_Sky = "./images/cg/Green-Haired_Girl/sky.jpg"
image Sea_Midori_Clouds = "./images/cg/Green-Haired_Girl/clouds.png"
image Sea_Midori_Sea_01 = "./images/cg/Green-Haired_Girl/sea_01.png"
image Sea_Midori_Sea_02 = "./images/cg/Green-Haired_Girl/sea_02.png"
image Sea_Midori_Sea_03 = "./images/cg/Green-Haired_Girl/sea_03.png"
image Sea_Midori_Chore = "./images/cg/Green-Haired_Girl/chore.png"
image Sea_Midori = "./images/cg/Green-Haired_Girl/midori.png"


image Sea_Midori_Scene:
    contains:
        subpixel True
        xalign 0.0
        "Sea_Midori_Sky"
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Sea_Midori_Clouds", "Sea_Midori_Clouds" )
        linear 200.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Sea_Midori_Sea_01", "Sea_Midori_Sea_01" )
        linear 200.0 xpos -1.0
        repeat
        
    contains:
        subpixel True
        xalign 0.0
        HBox( "Sea_Midori_Sea_02", "Sea_Midori_Sea_02" )
        linear 200.0 xpos -2.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Sea_Midori_Sea_03", "Sea_Midori_Sea_03" )
        linear 200.0 xpos -3.0
        repeat
        
    contains:
        subpixel True
        xalign 0.0
        "Sea_Midori_Chore"
    
    contains:
        subpixel True
        xalign 0.0
        "Sea_Midori"
