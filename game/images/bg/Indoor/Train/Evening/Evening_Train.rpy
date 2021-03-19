image Evening_Train_Main = "images/bg/Indoor/Train/Evening/Train_Main.png"
image Evening_Train_Lines = "images/bg/Indoor/Train/Evening/Train_Lines.png"
image Evening_Train_Shadows = "images/bg/Indoor/Train/Evening/Train_Shadows.png"
image Evening_Train_Post = "images/bg/Indoor/Train/Evening/Train_Post.png"
image Evening_Train_Post_Shadow = "images/bg/Indoor/Train/Evening/Train_Post_Shadow.png"
image Evening_Train_Post_Shadow_Animation_Mask = "images/bg/Indoor/Train/Evening/Train_Post_Shadow_Animation_Mask.png"
image Evening_Train_Post_Animation_Mask = "images/bg/Indoor/Train/Evening/Train_Post_Animation_Mask.png"
image Evening_Train_Light_Sfx = "images/bg/Indoor/Train/Evening/Train_Light_Sfx.png"
image Evening_Train_Light_Sfx_Mask = "images/bg/Indoor/Train/Evening/Train_Light_Sfx_Mask.png"
image Evening_Train_Handrail = "images/bg/Indoor/Train/Evening/Handrail.png"


image Evening_Train_bg_01 = "images/bg/Indoor/Train/Evening/bg_01.png"
image Evening_Train_bg_02 = "images/bg/Indoor/Train/Evening/bg_02.png"
image Evening_Train_bg_03 = "images/bg/Indoor/Train/Evening/bg_03.png"
image Evening_Train_bg_04 = "images/bg/Indoor/Train/Evening/bg_04.png"
image Evening_Train_bg_05 = "images/bg/Indoor/Train/Evening/bg_05.png"
image Evening_Train_Sky = "images/bg/Indoor/Train/Evening/sky.png"
image Evening_Train_Clouds = "images/bg/Indoor/Train/Evening/clouds.png"


image Evening_Train_Post_Shadow_Animation_Masked = AlphaMask( "Evening_Train_Post_Shadow_Animation", "Evening_Train_Post_Shadow_Animation_Mask" )
image Evening_Train_Post_Animation_Masked = AlphaMask( "Evening_Train_Post_Animation", "Evening_Train_Post_Animation_Mask" )
image Evening_Train_Light_Sfx_Masked = AlphaMask( "Evening_Train_Light_Sfx", "Evening_Train_Sfx_Mask_Animation" )


image Evening_Handrail_Animated:
    contains:
        "Evening_Train_Handrail"
        rotate -7
        ease 1.5 rotate 7
        ease 1.5 rotate -7
        repeat


image Evening_Shaked_Train:
    contains:
        "white_image"
        
    contains:
        #ypos 200
        "Evening_Train_Sky"
        
    contains:
        ypos 250
        "Evening_Train_Clouds"
        
    contains:
        ypos -50
        "Evening_Train_bg_05"
        
    contains:
        subpixel True
        #ypos -100
        xalign 0.0
        HBox( "Evening_Train_bg_04", "Evening_Train_bg_04" )
        linear 50.0 xpos -1.0
        repeat
        
    contains:
        subpixel True
        ypos -100
        xalign 0.0
        HBox( "Evening_Train_bg_03", "Evening_Train_bg_03" )
        linear 16.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Evening_Train_bg_02", "Evening_Train_bg_02" )
        linear 6.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Evening_Train_bg_01", "Evening_Train_bg_01" )
        linear 3.0 xpos -1.0
        repeat
    
    contains:
        "Evening_Train"
        xpos 0
        ease 3 xpos -20
        ease 3 xpos 0
        repeat

image Evening_Train:
    
    contains:
        "Evening_Train_Post_Animation_Masked"

    contains:
        "Evening_Train_Main"
    
    contains:
        alpha 0.8
        "Evening_Train_Post_Shadow_Animation_Masked"
    
    contains:
        alpha 0.8
        "Evening_Train_Shadows"
    contains:
        "Evening_Train_Lines"
    
    contains:
        "Evening_Handrail_Animated"
        xpos 0
        ypos 100

    contains:
        "Evening_Handrail_Animated"
        xpos 210
        ypos 100

    contains:
        "Evening_Handrail_Animated"
        xpos 410
        ypos 100

    contains:
        "Evening_Handrail_Animated"
        xpos 1250
        ypos 100

    contains:
        "Evening_Handrail_Animated"
        xpos 1430
        ypos 100

    contains:
        "Evening_Handrail_Animated"
        xpos 1610
        ypos 100

    contains:
        "Evening_Handrail_Animated"
        xpos 1790
        ypos 100


image Evening_Train_Post_Shadow_Animation:
    contains:
        "Evening_Train_Post_Shadow"
        xpos 2100
        pause 3
        linear 1.0 xpos -200
        repeat


image Evening_Train_Post_Animation:
    contains:
        "Evening_Train_Post"
        xpos 2040
        pause 3
        linear 1.0 xpos -260
        
        repeat
