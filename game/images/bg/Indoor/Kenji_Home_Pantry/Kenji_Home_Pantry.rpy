image Day_Kenji_Home_Pantry_Other_01 = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_01.png"
image Day_Kenji_Home_Pantry_Other_02 = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_02.png"
image Day_Kenji_Home_Pantry_Other_03 = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_03.png"
image Day_Kenji_Home_Pantry_Other_04 = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Other_04.png"

image Day_Kenji_Home_Pantry_Blink_01 = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_01.png"
image Day_Kenji_Home_Pantry_Blink_01a = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_01a.png"
image Day_Kenji_Home_Pantry_Blink_02 = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_02.png"
image Day_Kenji_Home_Pantry_Blink_03 = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_03.png"
image Day_Kenji_Home_Pantry_Blink_04 = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Blink_04.png"

image Day_Kenji_Home_Pantry_Mask = "images/bg/Indoor/Kenji_Home_Pantry/Day_Kenji_Home_Pantry_Mask.png"
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
        "Pointer_01"
        rotate 45/2
        xpos 400
        ypos 500
        alpha 0.0
        pause 0.5
        alpha 1.0
        pause 0.5
        repeat
    contains:
        "Pointer_01"
        rotate -45/2
        xpos 400
        ypos 620
        alpha 0.0
        pause 0.5
        alpha 1.0
        pause 0.5
        repeat

image Day_Kenji_Home_Pantry_Blink_01a_Animated:
    contains:
        "Pointer_01"
        rotate -45/2
        xpos 400
        ypos 620
        alpha 0.0
        pause 0.5
        alpha 1.0
        pause 0.5
        repeat

image Day_Kenji_Home_Pantry_Blink_02_Animated:
    contains:
        "Pointer_01"
        rotate 45/2
        xpos 400
        ypos 500
        alpha 0.0
        pause 0.5
        alpha 1.0
        pause 0.5
        repeat

image Day_Kenji_Home_Pantry_Blink_03_Animated:
    contains:
        "Pointer_01"
        rotate -45/2
        xpos 700
        ypos 170
        alpha 0.0
        pause 0.5
        alpha 1.0
        pause 0.5
        repeat

image Day_Kenji_Home_Pantry_Blink_04_Animated:
    contains:
        "Pointer_01"
        rotate 45/2
        xpos 850
        ypos 550
        alpha 0.0
        pause 0.5
        alpha 1.0
        pause 0.5
        repeat

