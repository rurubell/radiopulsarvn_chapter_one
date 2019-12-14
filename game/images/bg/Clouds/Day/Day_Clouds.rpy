image Day_Clouds_00 = "./images/bg/Clouds/Day/day_clouds_00.png"
image Day_Clouds_01 = "./images/bg/Clouds/Day/day_clouds_01.png"
image Day_Clouds_02 = "./images/bg/Clouds/Day/day_clouds_02.png"


image Day_Clouds:
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Clouds_02", "Day_Clouds_02" )
        linear 1200.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Clouds_01", "Day_Clouds_01" )
        linear 600.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Clouds_00", "Day_Clouds_00" )
        linear 400.0 xpos -1.0
        repeat
