image Day_Clouds_02_Layer_01 = "images/bg/Outdoor/Clouds/Day/Clouds_02/Layer_01.png"
image Day_Clouds_02_Layer_02 = "images/bg/Outdoor/Clouds/Day/Clouds_02/Layer_02.png"


image Day_Clouds_02:
    contains:
        subpixel True
        xalign 0.0
        alpha 0.3
        HBox( "Day_Clouds_02_Layer_01", "Day_Clouds_02_Layer_01" )
        linear 2000.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Clouds_02_Layer_02", "Day_Clouds_02_Layer_02" )
        linear 1000.0 xpos -1.0
        repeat
