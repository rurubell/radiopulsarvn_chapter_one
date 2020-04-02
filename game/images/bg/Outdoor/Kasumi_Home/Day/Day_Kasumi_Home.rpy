image Day_Kasumi_Home_Other = "images/bg/Outdoor/Kasumi_Home/Day/Other.png"
image Day_Kasumi_Home_Sky = "images/bg/Outdoor/Kasumi_Home/Day/Sky.jpg"

image Day_Kasumi_Home:
    contains:
        subpixel True
        xalign 0.0
        "Day_Kasumi_Home_Sky"
    
    contains:
        "Day_Right_To_Left_Jet"
    
    contains:
        yoffset -100
        "Day_Clouds"
    
    contains:
        "Day_Kasumi_Home_Other"
