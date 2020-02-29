image Evening_Clouds_00 = "./images/bg/Outdoor/Clouds/Evening/evening_clouds_00.png"
image Evening_Clouds_01 = "./images/bg/Outdoor/Clouds/Evening/evening_clouds_01.png"
image Evening_Clouds_02 = "./images/bg/Outdoor/Clouds/Evening/evening_clouds_02.png"


image Evening_Clouds:
    contains:
        subpixel True
        xalign 0.0
        HBox( "Evening_Clouds_02", "Evening_Clouds_02" )
        linear 1200.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Evening_Clouds_01", "Evening_Clouds_01" )
        linear 600.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Evening_Clouds_00", "Evening_Clouds_00" )
        linear 400.0 xpos -1.0
        repeat
