image Day_Kenji_Home_Other = "./images/bg/Outdoor/Kenji_Home/Day/Day_Kenji_Home_Other.png"
image Day_Kenji_Home_Sky = "./images/bg/Outdoor/Kenji_Home/Day/Day_Kenji_Home_Sky.jpg"

image Outdoor_Day_Kenji_Home:
    contains:
        subpixel True
        xalign 0.0
        "Day_Kenji_Home_Sky"
    
    contains:
        "Day_Right_To_Left_Jet"
    
    contains:
        yoffset -100
        "Day_Clouds"
    
    contains:
        "Day_Kenji_Home_Other"
