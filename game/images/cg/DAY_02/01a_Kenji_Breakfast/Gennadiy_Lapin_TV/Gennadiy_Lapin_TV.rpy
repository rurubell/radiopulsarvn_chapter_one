image Gennadiy_Lapin_TV_Other = "images/cg/DAY_02/01a_Kenji_Breakfast/Gennadiy_Lapin_TV/tv_gennadiy_lapin.png"
image Gennadiy_Lapin_TV_Other_Masked = AlphaMask( "Gennadiy_Lapin_TV_Other", "TV_Mask" )


image Gennadiy_Lapin_TV:
    contains:
        "empty_image"
    
    contains:
        "TV"
        xpos 100
        ypos 0
        
    contains:
        "Gennadiy_Lapin_TV_Other_Masked"
        xpos 100
        ypos 0
        
    contains:
        "TV_Interferences_Animation_Masked"
        xpos 100
