image Ponasenkov_TV_Other = "images/cg/DAY_02/07a_Kenji_Evening_Meal/TV_Ponasenkov/tv_ponasenkov.png"
image Ponasenkov_TV_Other_Masked = AlphaMask( "Ponasenkov_TV_Other", "TV_Mask" )


image Ponasenkov_TV:
    contains:
        "empty_image"
    
    contains:
        "TV"
        xpos 100
        ypos 0
        
    contains:
        "Ponasenkov_TV_Other_Masked"
        xpos 100
        ypos 0
        
    contains:
        "TV_Interferences_Animation_Masked"
        xpos 100
