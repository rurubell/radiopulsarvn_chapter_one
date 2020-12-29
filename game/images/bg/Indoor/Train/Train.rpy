image Train_Main = "images/bg/Indoor/Train/Train_Main.png"
image Train_Lines = "images/bg/Indoor/Train/Train_Lines.png"
image Train_Shadows = "images/bg/Indoor/Train/Train_Shadows.png"
image Train_Post = "images/bg/Indoor/Train/Train_Post.png"
image Train_Post_Shadow = "images/bg/Indoor/Train/Train_Post_Shadow.png"
image Train_Post_Shadow_Animation_Mask = "images/bg/Indoor/Train/Train_Post_Shadow_Animation_Mask.png"
image Train_Post_Animation_Mask = "images/bg/Indoor/Train/Train_Post_Animation_Mask.png"
image Train_Light_Sfx = "images/bg/Indoor/Train/Train_Light_Sfx.png"
image Train_Light_Sfx_Mask = "images/bg/Indoor/Train/Train_Light_Sfx_Mask.png"
image Train_Handrail = "images/bg/Indoor/Train/Handrail.png"


image Train_bg_01 = "images/bg/Indoor/Train/bg_01.png"
image Train_bg_02 = "images/bg/Indoor/Train/bg_02.png"
image Train_bg_03 = "images/bg/Indoor/Train/bg_03.png"
image Train_bg_04 = "images/bg/Indoor/Train/bg_04.png"
image Train_bg_05 = "images/bg/Indoor/Train/bg_05.png"
image Train_Sky = "images/bg/Indoor/Train/sky.png"
image Train_Clouds = "images/bg/Indoor/Train/clouds.png"


image Train_Post_Shadow_Animation_Masked = AlphaMask( "Train_Post_Shadow_Animation", "Train_Post_Shadow_Animation_Mask" )
image Train_Post_Animation_Masked = AlphaMask( "Train_Post_Animation", "Train_Post_Animation_Mask" )
image Train_Light_Sfx_Masked = AlphaMask( "Train_Light_Sfx", "Train_Sfx_Mask_Animation" )


image Handrail_Animated:
    contains:
        "Train_Handrail"
        rotate -7
        ease 1.5 rotate 7
        ease 1.5 rotate -7
        repeat


image Shaked_Train:
    contains:
        "white_image"
        
    contains:
        #ypos 200
        "Train_Sky"
        
    contains:
        ypos 250
        "Train_Clouds"
        
    contains:
        ypos -50
        "Train_bg_05"
        
    contains:
        subpixel True
        #ypos -100
        xalign 0.0
        HBox( "Train_bg_04", "Train_bg_04" )
        linear 50.0 xpos -1.0
        repeat
        
    contains:
        subpixel True
        ypos -100
        xalign 0.0
        HBox( "Train_bg_03", "Train_bg_03" )
        linear 16.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Train_bg_02", "Train_bg_02" )
        linear 6.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Train_bg_01", "Train_bg_01" )
        linear 3.0 xpos -1.0
        repeat
    
    contains:
        "Train"
        xpos 0
        ease 3 xpos -20
        ease 3 xpos 0
        repeat

image Train:
    
    contains:
        "Train_Post_Animation_Masked"

    contains:
        "Train_Main"
    
    contains:
        alpha 0.6
        "Train_Post_Shadow_Animation_Masked"
    
    contains:
        alpha 0.6
        "Train_Shadows"
    contains:
        "Train_Lines"
    
    contains:
        "Handrail_Animated"
        xpos 0
        ypos 100

    contains:
        "Handrail_Animated"
        xpos 210
        ypos 100

    contains:
        "Handrail_Animated"
        xpos 410
        ypos 100

    contains:
        "Handrail_Animated"
        xpos 1250
        ypos 100

    contains:
        "Handrail_Animated"
        xpos 1430
        ypos 100

    contains:
        "Handrail_Animated"
        xpos 1610
        ypos 100

    contains:
        "Handrail_Animated"
        xpos 1790
        ypos 100


image Train_Post_Shadow_Animation:
    contains:
        "Train_Post_Shadow"
        xpos 2100
        pause 3
        linear 1.0 xpos -200
        repeat


image Train_Post_Animation:
    contains:
        "Train_Post"
        xpos 2040
        pause 3
        linear 1.0 xpos -260
        
        repeat
