image Splash_Text = "./images/other/splash/text.png"
image Splash_Saw = "./images/other/splash/saw.png"
image Splash_Saw_Mask = "./images/other/splash/mask.png"


image Splash_Saw_Animated:
    contains:
        xpos 0
        "Splash_Saw"
        linear 1.0 xpos -41
        pause 0.5
        repeat


image Splash_Saw_Animated_Masked = AlphaMask( "Splash_Saw_Animated", "Splash_Saw_Mask" )


image Splash:
    contains:
        "black"
    
    contains:
        "Splash_Text"
    
    contains:
        "Splash_Saw_Animated_Masked"
