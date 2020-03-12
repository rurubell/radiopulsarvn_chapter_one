image Day_Trash_Place_Sfx = "./images/bg/Outdoor/Trash_Place/Day/sfx.png"
image Day_Trash_Place_Other = "./images/bg/Outdoor/Trash_Place/Day/other.png"
image Day_Trash_Place_Sky = "./images/bg/Outdoor/Trash_Place/Day/sky.jpg"


image Day_Trash_Place:
    contains:
        subpixel True
        xalign 0.0
        "Day_Trash_Place_Sky"

    contains:
        "Day_Right_To_Left_Jet"

    contains:
        yoffset -100
        "Day_Clouds"
        
    contains:
        "Day_Trash_Place_Other"
        
    contains:
        "Say_Trash_Place_Wires"
        
    contains:
        "Day_Trash_Place_Sfx"
        
        choice:
            linear 1 alpha 0.9
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
            
        choice:
            linear 1 alpha 0.8
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
        
        choice:
            linear 1 alpha 0.7
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
        
        choice:
            linear 1 alpha 0.6
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
        
        choice:
            linear 1 alpha 0.5
            #"Main_Menu_sfx"
            linear 1 alpha 1.0
        
        pause 0.5
        repeat
