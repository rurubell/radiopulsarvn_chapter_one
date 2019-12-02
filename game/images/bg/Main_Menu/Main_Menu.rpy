image Main_Menu_other = "./images/bg/Main_Menu/other.png"
image Main_Menu_sky = "./images/bg/Main_Menu/sky.jpg"
image Main_Menu_clouds = "./images/bg/Main_Menu/clouds.png"
image Main_Menu_sub_clouds = "./images/bg/Main_Menu/sub_clouds.png"


image Main_Menu_BG:
    contains:
        subpixel True
        xalign 0.0
        "Main_Menu_sky"
        
    contains:
        subpixel True
        xalign 0.0
        HBox( "Main_Menu_sub_clouds", "Main_Menu_sub_clouds" )
        linear 1000.0 xpos -1.0
        repeat
    
    contains:
        subpixel True
        xalign 0.0
        HBox( "Main_Menu_clouds", "Main_Menu_clouds" )
        linear 600.0 xpos -1.0
        repeat
    
    contains:
        "Main_Menu_wires"
    
    contains:
        "Main_Menu_other"
