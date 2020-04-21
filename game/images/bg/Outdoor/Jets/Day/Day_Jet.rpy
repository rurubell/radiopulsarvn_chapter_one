image right_to_left_jet = "images/bg/Outdoor/Jets/Day/right_to_left_jet.png"
image left_to_right_jet = "images/bg/Outdoor/Jets/Day/left_to_right_jet.png"


image Day_Jet:
    choice:
        contains:
            "empty_image"
        contains:
            xpos 1920
            ypos 100
            "right_to_left_jet"
            linear 200 xpos - 1920
            repeat

    choice:
        contains:
            "empty_image"
        contains:
            xpos -400
            ypos 100
            "left_to_right_jet"
            linear 200 xpos 3000
            repeat
            
    choice:
        contains:
            "empty_image"

    choice:
        contains:
            "empty_image"
