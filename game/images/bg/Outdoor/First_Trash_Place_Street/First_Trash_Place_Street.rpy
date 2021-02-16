image First_Trash_Place_Street = "images/bg/Outdoor/First_Trash_Place_Street/First_Trash_Place_Street.png"
image First_Trash_Place_Blured = "images/bg/Outdoor/First_Trash_Place_Street/First_Trash_Place_Street_Blured.png"

image First_Trash_Place_Street_Kenji_Run:
    contains:
        "First_Trash_Place_Street"
        zoom 1.05anchor (48,27)
        ease 0.20pos (0, 0)
        ease 0.20pos (25,25)
        ease 0.20pos (0, 0)
        ease 0.20pos (-25,25)
        repeat 
    
    contains:
        "Run_Stripes"


image First_Trash_Place_Blured_Animated:
    contains:
        "First_Trash_Place_Blured"

    contains:
        "black_image"
        alpha 1.0
        pause 1.0
        linear 3.0 alpha 0.0
