image TV_Strange_Movie_Other = "./images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/TV_Strange_Movie.png"
image TV_Strange_Movie_Mask = "./images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/TV_Mask.png"

image TV_Interference_Line_01 = "./images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/TV_Interference_Line/01.png"
image TV_Interference_Line_02 = "./images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/TV_Interference_Line/02.png"
image TV_Interference_Line_03 = "./images/cg/DAY_01/02a_Kenji_1st_Day_Breakfast/TV/TV_Interference_Line/03.png"

image TV_Interference_Line_Animated:
    "TV_Interference_Line_01"
    0.1
    "TV_Interference_Line_02"
    0.1
    "TV_Interference_Line_03"
    0.1
    repeat


image TV_Interference_Line_Animated_Moved:
    contains:
        "empty_image"
    
    contains:
        xpos 700
        ypos 500
        "TV_Interference_Line_Animated"
        linear 4.0 ypos 100
        repeat

image TV_Interference_Line_Animated_Masked = AlphaMask( "TV_Interference_Line_Animated_Moved", "TV_Strange_Movie_Mask" )

image TV_Strange_Movie:
    contains:
        "TV_Strange_Movie_Other"
    
    contains:
        "TV_Strange_Movie_Mask"
        alpha 0.25
        pause 0.3
        alpha 0.3
        pause 0.3
        repeat
    
    contains:
        "TV_Interference_Line_Animated_Masked"
