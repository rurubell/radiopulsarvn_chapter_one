image Bee_On_Ice_Cream_Base = "/images/cg/DAY_02/02a_Way_To_Dump/Bee_On_Ice_Cream/Bee_On_Ice_Cream_Base.png"
image Bee_On_Ice_Cream_Hand = "/images/cg/DAY_02/02a_Way_To_Dump/Bee_On_Ice_Cream/Bee_On_Ice_Cream_Hand.png"
image Bee_On_Ice_Cream_Yay = "/images/cg/DAY_02/02a_Way_To_Dump/Bee_On_Ice_Cream/Bee_On_Ice_Cream_Yay.png"


image Bee_On_Ice_Cream:
    contains:
        "Bee_On_Ice_Cream_Base"
    
    contains:
        "Bee_On_Ice_Cream_Hand"
        xpos 439
        ypos 389
        ease 0.1 ypos 395
        pause 0.5
        ease 1.5 ypos 389
        repeat
        
    
    contains:
        alpha 0.0
        "Bee_On_Ice_Cream_Yay"
        xpos 520
        ypos 188
        
        parallel:
            ease 0.3 xpos 577
        parallel:
            ease 0.3 ypos 166
        parallel:
            ease 0.3 alpha 1.0
        
        pause 0.9
        linear 0.9 alpha 0.0
        repeat 
