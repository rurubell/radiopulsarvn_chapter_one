image That_Fucking_Cat_Mask = "images/cg/DAY_02/02a_Way_To_Dump/That_Fucking_Cat/That_Fucking_Cat_Mask.png"
image That_Fucking_Cat_Cat = "images/cg/DAY_02/02a_Way_To_Dump/That_Fucking_Cat/That_Fucking_Cat_Cat.png"


image That_Fucking_Cat_Moved:
    contains:
        pause 1.0
        "That_Fucking_Cat_Cat"
        xpos 100
        ease 0.5 xpos 0

image That_Fucking_Cat_Moved_Masked = AlphaMask( "That_Fucking_Cat_Moved", "That_Fucking_Cat_Mask" )


image That_Fucking_Cat:
    contains:
        "That_Fucking_Cat_Moved_Masked"
    
    contains:
        pause 1.0
        alpha 0.0
        "That_Fucking_Cat_Cat"
        pause 0.6
        linear 0.3 alpha 1.0
