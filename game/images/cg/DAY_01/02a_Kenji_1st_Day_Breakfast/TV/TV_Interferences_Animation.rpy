image TV_Interference_Line_01 = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/TV_Interference_Line/01.png"
image TV_Interference_Line_02 = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/TV_Interference_Line/02.png"
image TV_Interference_Line_03 = "images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/TV_Interference_Line/03.png"

image TV_Interferences_Animation_Masked = AlphaMask ( "TV_Interferences_Animation", "TV_Mask" )


image TV_Interference_Line_Animated:
    "TV_Interference_Line_01"
    0.1
    "TV_Interference_Line_02"
    0.1
    "TV_Interference_Line_03"
    0.1
    repeat


image TV_Interferences_Animation:
    contains:
        "TV_Mask"
        linear 0.1 alpha 0.1
        linear 0.1 alpha 0.2
        repeat
        
    contains:
        "TV_Interference_Line_Animated"
        xpos 20
        ypos 100
        linear 3 ypos 400
        repeat


