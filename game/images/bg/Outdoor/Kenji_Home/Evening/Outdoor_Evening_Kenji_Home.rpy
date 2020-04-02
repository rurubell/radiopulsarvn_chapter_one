image Evening_Kenji_Home_Other = "images/bg/Outdoor/Kenji_Home/Evening/Other.png"
image Evening_Kenji_Home_Sky = "images/bg/Outdoor/Kenji_Home/Evening/Sky.jpg"

image Outdoor_Evening_Kenji_Home:
    contains:
        subpixel True
        xalign 0.0
        "Evening_Kenji_Home_Sky"
    
    contains:
        "Day_Right_To_Left_Jet"
    
    contains:
        yoffset -100
        "Evening_Clouds"
    
    contains:
        "Evening_Kenji_Home_Other"
