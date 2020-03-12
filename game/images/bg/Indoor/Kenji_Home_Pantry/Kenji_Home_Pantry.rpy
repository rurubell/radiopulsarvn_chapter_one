image Day_Kenji_Home_Pantry_Other_01 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_01.jpg"
image Day_Kenji_Home_Pantry_Other_02 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_02.jpg"
image Day_Kenji_Home_Pantry_Other_03 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_03.jpg"
image Day_Kenji_Home_Pantry_Other_04 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_04.jpg"

image Day_Kenji_Home_Pantry_Blink_01 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_01.png"
image Day_Kenji_Home_Pantry_Blink_02 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_02.png"
image Day_Kenji_Home_Pantry_Blink_03 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_03.png"
image Day_Kenji_Home_Pantry_Blink_04 = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_04.png"

image Day_Kenji_Home_Pantry_Mask = "./images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Mask.png"
image Day_Kenji_Home_Pantry_Dust = AlphaMask( "dust", "Day_Kenji_Home_Pantry_Mask" )


image Day_Kenji_Home_Pantry_01:
    contains:
        "Day_Kenji_Home_Pantry_Other_01"
    
    contains:
        "Day_Kenji_Home_Pantry_Dust"

image Day_Kenji_Home_Pantry_02:
    contains:
        "Day_Kenji_Home_Pantry_Other_02"
    
    contains:
        "Day_Kenji_Home_Pantry_Dust"

image Day_Kenji_Home_Pantry_03:
    contains:
        "Day_Kenji_Home_Pantry_Other_03"
    
    contains:
        "Day_Kenji_Home_Pantry_Dust"

image Day_Kenji_Home_Pantry_04:
    contains:
        "Day_Kenji_Home_Pantry_Other_04"
    
    contains:
        "Day_Kenji_Home_Pantry_Dust"


image Day_Kenji_Home_Pantry_Blink_01_Animated:
    contains:
        "Day_Kenji_Home_Pantry_Blink_01"
        alpha 0.2
        linear 1.0 alpha 0.6
        linear 1.0 alpha 0.2
        repeat

image Day_Kenji_Home_Pantry_Blink_02_Animated:
    contains:
        "Day_Kenji_Home_Pantry_Blink_02"
        alpha 0.2
        linear 1.0 alpha 0.6
        linear 1.0 alpha 0.2
        repeat

image Day_Kenji_Home_Pantry_Blink_03_Animated:
    contains:
        "Day_Kenji_Home_Pantry_Blink_03"
        alpha 0.2
        linear 1.0 alpha 0.6
        linear 1.0 alpha 0.2
        repeat

image Day_Kenji_Home_Pantry_Blink_04_Animated:
    contains:
        "Day_Kenji_Home_Pantry_Blink_04"
        alpha 0.2
        linear 1.0 alpha 0.6
        linear 1.0 alpha 0.2
        repeat

