image Trash_Place_In_Kenji_Mind_Other = "images/cg/DAY_02/03a_First_Trash_Place/Trash_Place_In_Kenji_Mind/Trash_Place_In_Kenji_Mind.png"
image Trash_Place_In_Kenji_Mind_Fire_Glares = "images/cg/DAY_02/03a_First_Trash_Place/Trash_Place_In_Kenji_Mind/fire_glares.png"


image Trash_Place_In_Kenji_Mind_Animated:
    contains:
        "Trash_Place_In_Kenji_Mind_Other"

    contains:
        xpos 1600
        ypos 550
        zoom 0.4
        #rotate -25
        "Trash_Place_In_Kenji_Mind_Other_Fire_Animated_Triple"

    contains:
        xpos 1700
        ypos 600
        zoom 0.5
        #rotate -25
        "Trash_Place_In_Kenji_Mind_Other_Fire_Animated_Single"

    contains:
        xpos 1770
        ypos 350
        zoom 0.4
        #rotate -25
        "Trash_Place_In_Kenji_Mind_Other_Fire_Animated_Double"

    contains:
        xpos 1800
        ypos 500
        zoom 0.4
        #rotate -25
        "Trash_Place_In_Kenji_Mind_Other_Fire_Animated_Triple"

    contains:
        xpos 1500
        ypos 600
        zoom 0.2
        #rotate -25
        "Trash_Place_In_Kenji_Mind_Other_Fire_Animated_Single"

    contains:
        xpos 1700
        ypos 400
        zoom 0.2
        #rotate -25
        "Trash_Place_In_Kenji_Mind_Other_Fire_Animated_Single"
    
    contains:
        "Trash_Place_In_Kenji_Mind_Fire_Glares"
        alpha 0.4
        linear 0.7 alpha 0.7
        linear 0.7 alpha 0.4
        repeat
        
    contains:
        #pause 2
        "TPIKM_Smoke_Animated"
        ypos -100
        xpos 1550
        alpha 0.0
        pause 2
        linear 3 alpha 1.0

    contains:
        #pause 2
        "TPIKM_Smoke_Animated"
        ypos -150
        xpos 1750
        alpha 0.0
        pause 2
        linear 3 alpha 1.0
