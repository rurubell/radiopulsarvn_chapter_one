image Day_Train_Main = "images/bg/Indoor/Train/Day/Train_Main.png"
image Day_Train_Lines = "images/bg/Indoor/Train/Day/Train_Lines.png"
image Day_Train_Shadows = "images/bg/Indoor/Train/Day/Train_Shadows.png"
image Day_Train_Post = "images/bg/Indoor/Train/Day/Train_Post.png"
image Day_Train_Post_Shadow = "images/bg/Indoor/Train/Day/Train_Post_Shadow.png"
image Day_Train_Post_Shadow_Animation_Mask = "images/bg/Indoor/Train/Day/Train_Post_Shadow_Animation_Mask.png"
image Day_Train_Post_Animation_Mask = "images/bg/Indoor/Train/Day/Train_Post_Animation_Mask.png"
image Day_Train_Light_Sfx = "images/bg/Indoor/Train/Day/Train_Light_Sfx.png"
image Day_Train_Light_Sfx_Mask = "images/bg/Indoor/Train/Day/Train_Light_Sfx_Mask.png"
image Day_Train_Handrail = "images/bg/Indoor/Train/Day/Handrail.png"


image Day_Train_bg_01 = "images/bg/Indoor/Train/Day/bg_01.png"
image Day_Train_bg_02 = "images/bg/Indoor/Train/Day/bg_02.png"
image Day_Train_bg_03 = "images/bg/Indoor/Train/Day/bg_03.png"
image Day_Train_bg_04 = "images/bg/Indoor/Train/Day/bg_04.png"
image Day_Train_bg_05 = "images/bg/Indoor/Train/Day/bg_05.png"
image Day_Train_Sky = "images/bg/Indoor/Train/Day/sky.png"
image Day_Train_Clouds = "images/bg/Indoor/Train/Day/clouds.png"


image Day_Train_Post_Shadow_Animation_Masked = AlphaMask( "Day_Train_Post_Shadow_Animation", "Day_Train_Post_Shadow_Animation_Mask" )
image Day_Train_Post_Animation_Masked = AlphaMask( "Day_Train_Post_Animation", "Day_Train_Post_Animation_Mask" )
image Day_Train_Light_Sfx_Masked = AlphaMask( "Day_Train_Light_Sfx", "Day_Train_Sfx_Mask_Animation" )


image Day_Handrail_Animated:
    contains:
        "Day_Train_Handrail"
        rotate -7
        ease 1.5 rotate 7
        ease 1.5 rotate -7
        repeat


image Day_Shaked_Train:
    contains:
        "white_image"
        
    contains:
        #ypos 200
        "Day_Train_Sky"
        
    contains:
        ypos 250
        "Day_Train_Clouds"
        
    contains:
        ypos -50
        "Day_Train_bg_05"
        
    contains:
        subpixel True
        #ypos -100
        xalign 0.0
        HBox( "Day_Train_bg_04", "Day_Train_bg_04" )
        linear 50.0 xpos -1.0
        repeat
        
    contains:
        subpixel True
        ypos -100
        xalign 0.0
        HBox( "Day_Train_bg_03", "Day_Train_bg_03" )
        linear 16.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Train_bg_02", "Day_Train_bg_02" )
        linear 6.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Day_Train_bg_01", "Day_Train_bg_01" )
        linear 3.0 xpos -1.0
        repeat
    
    contains:
        "Day_Train"
        xpos 0
        ease 3 xpos -20
        ease 3 xpos 0
        repeat

image Day_Train:
    
    contains:
        "Day_Train_Post_Animation_Masked"

    contains:
        "Day_Train_Main"
    
    contains:
        alpha 0.6
        "Day_Train_Post_Shadow_Animation_Masked"
    
    contains:
        alpha 0.6
        "Day_Train_Shadows"
    contains:
        "Day_Train_Lines"
    
    contains:
        "Day_Handrail_Animated"
        xpos 0
        ypos 100

    contains:
        "Day_Handrail_Animated"
        xpos 210
        ypos 100

    contains:
        "Day_Handrail_Animated"
        xpos 410
        ypos 100

    contains:
        "Day_Handrail_Animated"
        xpos 1250
        ypos 100

    contains:
        "Day_Handrail_Animated"
        xpos 1430
        ypos 100

    contains:
        "Day_Handrail_Animated"
        xpos 1610
        ypos 100

    contains:
        "Day_Handrail_Animated"
        xpos 1790
        ypos 100


image Day_Train_Post_Shadow_Animation:
    contains:
        "Day_Train_Post_Shadow"
        xpos 2100
        pause 3
        linear 1.0 xpos -200
        repeat


image Day_Train_Post_Animation:
    contains:
        "Day_Train_Post"
        xpos 2040
        pause 3
        linear 1.0 xpos -260
        
        repeat
