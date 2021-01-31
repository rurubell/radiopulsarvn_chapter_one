image Day_Clouds_01_Layer_01 = "images/bg/Outdoor/Clouds/Day/Clouds_01/day_clouds_00.png"
image Day_Clouds_01_Layer_02 = "images/bg/Outdoor/Clouds/Day/Clouds_01/day_clouds_01.png"
image Day_Clouds_01_Layer_03 = "images/bg/Outdoor/Clouds/Day/Clouds_01/day_clouds_02.png"


image Day_Clouds_01:
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Clouds_01_Layer_03", "Day_Clouds_01_Layer_03" )
        linear 2000.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Clouds_01_Layer_02", "Day_Clouds_01_Layer_02" )
        linear 1000.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Clouds_01_Layer_01", "Day_Clouds_01_Layer_01" )
        linear 600.0 xpos -1.0
        repeat
