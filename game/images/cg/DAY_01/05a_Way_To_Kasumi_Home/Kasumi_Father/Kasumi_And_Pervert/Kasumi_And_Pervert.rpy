image Kasumi_And_Pervert_Other = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Kasumi_And_Pervert/Other.png"
image Kasumi_And_Pervert_Sky = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Kasumi_And_Pervert/Sky.jpg"

image Kasumi_And_Pervert_Sun_01 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Kasumi_And_Pervert/Sun_01.png"
image Kasumi_And_Pervert_Sun_02 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Kasumi_And_Pervert/Sun_02.png"

image Kasumi_And_Pervert_Clouds_01 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Kasumi_And_Pervert/Clouds_01.png"
image Kasumi_And_Pervert_Clouds_02 = "./images/cg/DAY_01/05a_Way_To_Kasumi_Home/Kasumi_Father/Kasumi_And_Pervert/Clouds_02.png"


image Kasumi_And_Pervert_Clouds_Animated:
    "Kasumi_And_Pervert_Clouds_01"
    0.5
    "Kasumi_And_Pervert_Clouds_02"
    0.5
    repeat


image Kasumi_And_Pervert:
    contains:
        "Kasumi_And_Pervert_Sky"
    
    contains:
        "Kasumi_And_Pervert_Sun_01"
        0.8
        "Kasumi_And_Pervert_Sun_02"
        0.8
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Kasumi_And_Pervert_Clouds_Animated", "Kasumi_And_Pervert_Clouds_Animated" )
        linear 200.0 xpos -1.0
        repeat
        
    contains:
        "Kasumi_And_Pervert_Other"
